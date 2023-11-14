"""
This module defines specific data types as subclasses of the Attribute class. 
These data types include TEXT, INTEGER, REAL, BLOB, and VARCHAR. 
Each data type is represented as a separate class with its own initialization and string representation methods.
"""
from main import *

# Define the specific data types as subclasses of Attribute # ==============================================================================
class TEXT(Attribute):
    def __init__(self, name):
        super().__init__(name, "TEXT")

    def __str__(self):
        return "{}: TEXT".format(self.name)

class INTEGER(Attribute):
    def __init__(self, name):
        super().__init__(name, "INTEGER")

    def __str__(self):
        return "{}: INTEGER".format(self.name)

class REAL(Attribute):
    def __init__(self, name):
        super().__init__(name, "REAL")

    def __str__(self):
        return "{}: REAL".format(self.name)

class BLOB(Attribute):
    def __init__(self, name):
        super().__init__(name, "BLOB")

    def __str__(self):
        return "{}: BLOB".format(self.name)

class VARCHAR(Attribute):
    def __init__(self, name, length):
        super().__init__(name, "VARCHAR({})".format(length))
        self.length = length

    def __str__(self):
        return "{}: VARCHAR({})".format(self.name, self.length)
class TEXT(Attribute):
    def __init__(self, name):
        super().__init__(name, "TEXT")

    def __str__(self):
        return "{}: TEXT".format(self.name)

class INTEGER(Attribute):
    """
    This class represents an INTEGER data type attribute. It is a subclass of the Attribute class.

    Attributes:
    name (str): The name of the attribute.
    """
    def __init__(self, name):
        """
        The constructor for the INTEGER class.

        Parameters:
        name (str): The name of the attribute.
        """
        super().__init__(name, "INTEGER")

    def __str__(self):
        """
        This method returns a string representation of the INTEGER object.

        Returns:
        str: A string representation of the INTEGER object in the format "name: INTEGER".
        """
        return "{}: INTEGER".format(self.name)

class REAL(Attribute):
    """
    This class represents a REAL data type attribute. It is a subclass of the Attribute class.

    Attributes:
    name (str): The name of the attribute.
    """
    def __init__(self, name):
        """
        The constructor for the REAL class.

        Parameters:
        name (str): The name of the attribute.
        """
        super().__init__(name, "REAL")

    def __str__(self):
        """
        This method returns a string representation of the REAL object.

        Returns:
        str: A string representation of the REAL object in the format "name: REAL".
        """
        return "{}: REAL".format(self.name)

class BLOB(Attribute):
    """
    This class represents a BLOB data type attribute. It is a subclass of the Attribute class.

    Attributes:
    name (str): The name of the attribute.
    """
    def __init__(self, name):
        """
        The constructor for the BLOB class.

        Parameters:
        name (str): The name of the attribute.
        """
        super().__init__(name, "BLOB")

    def __str__(self):
        """
        This method returns a string representation of the BLOB object.

        Returns:
        str: A string representation of the BLOB object in the format "name: BLOB".
        """
        return "{}: BLOB".format(self.name)

class VARCHAR(Attribute):
    """
    This class represents a VARCHAR data type attribute. It is a subclass of the Attribute class.

    Attributes:
    name (str): The name of the attribute.
    length (int): The length of the VARCHAR attribute.
    """
    def __init__(self, name, length):
        """
        The constructor for the VARCHAR class.

        Parameters:
        name (str): The name of the attribute.
        length (int): The length of the VARCHAR attribute.
        """
        super().__init__(name, "VARCHAR({})".format(length))
        self.length = length

    def __str__(self):
        """
        This method returns a string representation of the VARCHAR object.

        Returns:
        str: A string representation of the VARCHAR object in the format "name: VARCHAR(length)".
        """
        return "{}: VARCHAR({})".format(self.name, self.length)