import config

class Info():
    """This class returns information about the module"""
    def __init__(self):
        """Initializing function"""
        pass


    def name(self):
        """This function returns the name of the module"""
        return config.NAME


    def version(self):
        """This function returns the version of the module"""
        return config.VERSION
