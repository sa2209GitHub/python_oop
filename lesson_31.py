#
#   31
#
# 'raise' Statement and Custom Exceptions

# print("When forty winters shall beseige thy brow,")
# print("And dig deep trenches in thy beauty's field,")
# print("Thy youth's proud livery, so gazed on now,")
# print("Will be a tatter'd weed, of small worth held:\n")

# # 1 / 0
# # raise ZeroDivisionError(ZeroDivisionError.__doc__)
# e = ZeroDivisionError(ZeroDivisionError.__doc__)
# raise e

# print()
# print("Then being ask'd where all thy beauty lies,")
# print("Where all the treasure of thy lusty days,")
# print("To say, within thine own deep-sunken eyes,")
# print("Were an all-eating shame and thriftless praise.")
# print("\n. . .\n")

class ExceptionPrint(Exception):
    """Generic printer exception class"""


class ExceptionPrintSendData(ExceptionPrint):
    """Exception class when sending data to printer"""

    def __init__(self, *args: object):
        self.__message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.__message}"


class PrintData:
    def print(self, data):
        self.__send_data(data)
        print(f"Printing: {str(data)}")

    def __send_data(self, data):
        if not self.__send_to_print(data):
            raise ExceptionPrintSendData("The printer is not responding")

    def __send_to_print(self, data):
        print(f"Sending: {str(data)}")
        return False


p = PrintData()

# p.print("123")

try:
    p.print("DATA-DATA-DATA 478-358-3-489")
except ExceptionPrintSendData:
    print("The printer is not responding")
except ExceptionPrint:
    print("Unknown printing error")
