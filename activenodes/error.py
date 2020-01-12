

class MessageError(Exception):
    """Base class for errors in the email package."""


class NotVaildIPAddressError(MessageError):
    """Base class for Not a vaild IPv4 address"""

class AddressRangeError(MessageError):
    """Raise when end address bigger than start address"""