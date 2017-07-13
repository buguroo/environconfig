environconfig
=============

`environconfig` allow you to use environment variables in Python with a
declarative syntax.

A quick example:

.. code-block:: python

    from environconfig import EnvironConfig
    from environconfig import StringVar, IntVar

    class DBCfg(EnvironConfig):
        """Database configuration from the environment."""
        HOSTNAME = StringVar(default='localhost')
        PORT = IntVar(default=3306)
        USERNAME = StringVar()
        PASSWORD = StringVar()
        CHARSET = StringVar(default='utf8mb4')
        NAME = StringVar(default='mydatabase')

    # Now you can start using it
    connection = pymysql.connect(host=DBCfg.HOSTNAME,
                                 user=DBCfg.USERNAME,
                                 password=DBCfg.PASSWORD,
                                 db=DBCfg.NAME,
                                 charset=DBCfg.CHARSET,
                                 cursorclass=pymysql.cursors.DictCursor)

You can check more examples in the `examples` directory.
    

Features
--------

- Built-in basic types: String, Bool, Int, Float...
- Easy Customizable: `CustomVar` (just pass a callable to make the conversion)
- No mocking necessary for testing: Just instantiate your config with a dictionary.
- Easy build complex constructions with environment data: See `MethodVar`


Collaboration
-------------

- We are always open to pull requests and accept new var types.
