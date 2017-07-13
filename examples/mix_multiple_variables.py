from environconfig import *


class DBCfg(EnvironConfig):
    """
    Database configuration from the environment.
    """
    HOSTNAME = StringVar(default='localhost')
    PORT = IntVar(default=3306)
    USERNAME = StringVar()
    PASSWORD = StringVar()
    CHARSET = StringVar(default='utf8mb4')
    NAME = StringVar(default='mydatabase')

    @MethodVar
    def CONNECTION_STRING(env):
        """
        Compose multiple environment variables into a connection string.
        """
        return ("mysql://{env.USERNAME}:{env.PASSWORD}"
                "@{env.HOSTNAME}:{env.PORT}"
                "/{env.NAME}").format(env=env)


print(DBCfg.CONNECTION_STRING)
