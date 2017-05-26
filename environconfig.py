import abc
import collections.abc
import os

#
# Abstract classes
#
class EnvironConfigABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getvar(self, name):
        """Return the raw value for this variable."""
        pass


class VarABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _to_python(self, value):
        """Translate the raw value (string) to a python value."""
        pass

#
# Other
#
class NoVarDefault:
    pass


class ClassAndInstanceMethod:
    def __init__(self, fn):
        self.fn = fn
        self.obj = None

    def __call__(self, *args, **kwargs):
        return self.fn(self.obj, *args, **kwargs)

    def __get__(self, instance, owner):
        self.obj = owner if instance is None else instance
        return self

classandinstancemethod = ClassAndInstanceMethod  # A prettier alias

#
# Base classes
#
class EnvironConfig(EnvironConfigABC):

    __varpreffix__ = ""
    environ = os.environ

    def __init__(self, environ=os.environ):
        if not isinstance(environ, collections.abc.Mapping):
            raise TypeError("environ must be a mapping")

        self.environ = environ

    @classandinstancemethod
    def getvar(obj, name):
        try:
            return obj.environ[obj.__varpreffix__ + name]
        except KeyError as exc:
            raise VarUnsetError("Unset var '{}'".format(name))

    @classandinstancemethod
    def verify(obj, name=None):
        if name is None:
            for name in dir(obj):
                try:
                    getattr(obj, name)
                except (VarUnsetError, VarTypeCastError):
                    return False
        else:
            try:
                getattr(obj, name)
            except (VarUnsetError, VarTypeCastError):
                return False

        return True


class BaseVar(VarABC):
    _name = None

    def __init__(self, default=NoVarDefault):
        self.default = default

    def __get_name__(self, owner):
        if self._name is None:
            self.__set_name__(owner)
        return self._name

    def __set_name__(self, owner, name=None):
        if name is None:
            # Explicit call (non-native).
            for name, value in owner.__dict__.items():
                if value is self:
                    self._name = name
                    break
            else:
                raise ValueError("Name not found.")
        else:
            # Called by python >= 3.6 at the time the owning class owner
            # is created.
            self._name = name

    def __get__(self, instance, owner):
        env = owner if instance is None else instance

        if issubclass(owner, EnvironConfig):
            name = self.__get_name__(owner)
            try:
                raw = env.getvar(name)
            except VarUnsetError:
                if self.default is NoVarDefault:
                    raise
                else:
                    return self.default
            else:
                try:
                    return self._to_python(raw)
                except Exception as exc:
                    raise VarTypeCastError(
                        "Cannot convert the value to python") from exc
        else:
            raise TypeError("Invalid environment {}".format(env))


#
# Var definition
#
StringVar = IntVar = None

#
# Custom exceptions
#
class VarUnsetError(KeyError):
    """The environment variable is not set."""
    pass


class VarTypeCastError(ValueError):
    """
    The environment variable can't be casted to the appropiate Python
    type.

    """
    pass
