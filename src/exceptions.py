
class NotInGreekException(Exception):
    """
    Exception raised when input is given in non Greek characters
    """

    pass


class NotLegalAdjectiveException(Exception):
    """
    Exception raised when input is not recognized as a possible adjective
    """
    pass


class NotLegalVerbException(Exception):
    """
    Exception raised when input is not recognized as a possible verb form
    """
    pass
