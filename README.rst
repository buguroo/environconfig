environconfig
=============

Application configuration from environment variables made easy


.. code-block:: python

   from environconfig import EnvironConfig
   from environconfig import StringVar, IntVar
   from environconfig import VarUnsetError

   class AppConfig(EnvironConfig):
       __varprefix__ = 'MYAPP_'

       DB_NAME = StringVar(default='mydatabase')
       DB_HOSTNAME = StringVar(default='localhost')
       DB_PORT = IntVar(default=3306)
       DB_USERNAME = StringVar()
       DB_PASSWORD = StringVar()

       @CustomVar
       def DB_CONFIG(env):
           return {"hostname": env.DB_HOSTNAME,
                   "port": env.DB_PORT,
                   "user": env.DB_USERNAME,
                   "password": env.DB_PASSWORD,
                   "database": env.DB_NAME,
                   "encoding": "utf-8"}


.. code-block:: python

   # Any environment variable defined will be retrieved and casted to
   # the python value.
   os.environ['MYAPP_DB_NAME'] = 'mydbname'
   assert AppConfig.DB_NAME == 'mydbname'


.. code-block:: python

   try:
       user = AppConfig.DB_USERNAME
   except VarUnsetError:
       # If the environment variable is not set and neither the default
       # value, this exception will be raised when the attribute is
       # accessed.
       pass


.. code-block:: python

   # Of course if you provide a default it will be available as a
   # fallback.
   assert AppConfig.DB_HOSTNAME == 'localhost'


.. code-block:: python

   os.environ['MYAPP_DB_PORT'] = 'this is not a valid integer'
   try:
       port = AppConfig.DB_PORT
   except VarTypeCastError:
       # Verification is made in access time.
       pass


.. code-block:: python

   # But you can verify the whole config
   AppConfig.verify()  # Return `True` if all attributes have a value
                       # (or a default)

   # Or a specific value
   AppConfig.verify('DB_PORT')  # Return `True` if a value or a default is
                                # provided for DB_PORT.
