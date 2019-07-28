

class GPIO:
    """
    Simple GPIO class for testing and pretending
    """

    BCM=1

    def __init__(self):
        """ Base constructor for Test GPIO """
        pass

    @classmethod
    def setwarnings(cls, state):
        """ Define warnings for testing """
        cls.state = state

    @classmethod
    def setmode(cls, mode):
        """ Defime mode for testing """
        cls.mode = mode

    def cleanup(self):
        """ Dummy cleanup method """
        pass


