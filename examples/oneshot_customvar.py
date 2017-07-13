from environconfig import *

from ipaddress import IPv4Address


class MyConfig(EnvironConfig):
    REMOTE_IP = CustomVar(IPv4Address,  # This is a callable,
                                        # get `str` and returns `IPv4Address` object
                          default=IPv4Address('0.0.0.0'))

print(MyConfig.REMOTE_IP)
