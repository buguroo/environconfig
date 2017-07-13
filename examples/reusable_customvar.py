from environconfig import *

from ipaddress import IPv4Address

# This creates a new type that can be used multiple times.
IPVar = CustomVar.new(IPv4Address)


class MyConfig(EnvironConfig):
    REMOTE_IP = IPVar(default=IPv4Address('0.0.0.0'))
    LOCAL_IP = IPVar(default=IPv4Address('127.0.0.1'))

print(MyConfig.REMOTE_IP, MyConfig.LOCAL_IP)
