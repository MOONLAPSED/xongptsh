"""
This module defines specific data types as subclasses of the Attribute class. 
These data types include TEXT, INTEGER, REAL, BLOB, and VARCHAR. 
Each data type is represented as a separate class with its own initialization and string representation methods.
"""

class TEXT(Attribute_):
    """
    This class represents a TEXT data type attribute. It is a subclass of the Attribute class.

    Attributes:
    name (str): The name of the attribute.
    """
    def __init__(self, name):
        """
        The constructor for the TEXT class.

        Parameters:
        name (str): The name of the attribute.
        """
        super().__init__(name, "TEXT")

    def __str__(self):
        """
        This method returns a string representation of the TEXT object.

        Returns:
        str: A string representation of the TEXT object in the format "name: TEXT".
        """
        return "{}: TEXT".format(self.name)

# Define other data type classes (INTEGER, REAL, BLOB, VARCHAR) with updated docstrings and comments

# ...
