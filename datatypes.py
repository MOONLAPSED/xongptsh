from main import *
# speculative first draft

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