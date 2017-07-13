from environconfig import *


class DBCfg(EnvironConfig):
    """
    Database configuration from the environment.
    """
    __varprefix__ = 'MYAPP_DB_'

    HOSTNAME = StringVar(default='localhost')

# MYAPP_DB_HOSTNAME environment var is accessible through DBCfg.HOSTNAME
print("MYAPP_DB_HOSTNAME =", DBCfg.HOSTNAME)
