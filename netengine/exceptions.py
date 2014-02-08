"""
netengine exception classes.
"""


class NetEngineError(Exception):
    """ net engine related error """
    pass

class SSHNetEngineError(Exception):
    """ ssh net engine related error """

    def __init__(self, error, instance):
        self.msg = error
        instance.disconnect()
         
    def __str__(self):
        return repr(self.msg)

    
