"""
This module defines three classes: Entity, Attribute, and Iteration. The Attribute and Iteration classes are subclasses of the Entity class. The module also includes test cases for each class.
"""
# Import necessary packages and modules
import pandas as pd

# Define the Entity class
class Entity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define the Attribute class as a subclass of Entity
class Attribute(Entity):
    def __init__(self, name, description, data_type):
        super().__init__(name, description)
        self.data_type = data_type

# Define the Iteration class as a subclass of Entity
class Iteration(Entity):
    """
    The Iteration class represents an iteration of an entity. It is a subclass of the Entity class.

    Attributes:
    name (str): The name of the iteration.
    description (str): The description of the iteration.
    """
    def __init__(self, name, description):
        """
        The constructor for the Iteration class.

        Parameters:
        name (str): The name of the iteration.
        description (str): The description of the iteration.
        """
        super().__init__(name, description)

# Define test cases for the Entity class
entity_test_cases = [
class Attribute(Entity):
    """
    The Attribute class represents an attribute of an entity. It is a subclass of the Entity class and includes an additional attribute for the data type.

    Attributes:
    name (str): The name of the attribute.
    description (str): The description of the attribute.
    data_type (str): The data type of the attribute.
    """
    def __init__(self, name, description, data_type):
        """
        The constructor for the Attribute class.

        Parameters:
        name (str): The name of the attribute.
        description (str): The description of the attribute.
        data_type (str): The data type of the attribute.
        """
        super().__init__(name, description)
        self.data_type = data_type

# Define the Iteration class as a subclass of Entity
class Iteration(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)

# Define test cases for the Entity class
entity_test_cases = [
class Entity:
    """
    The Entity class represents a general entity with a name and a description.

    Attributes:
    name (str): The name of the entity.
    description (str): The description of the entity.
    """
    def __init__(self, name, description):
        """
        The constructor for the Entity class.

        Parameters:
        name (str): The name of the entity.
        description (str): The description of the entity.
        """
        self.name = name
        self.description = description

# Define the Attribute class as a subclass of Entity
class Attribute(Entity):
    def __init__(self, name, description, data_type):
        super().__init__(name, description)
        self.data_type = data_type

# Define the Iteration class as a subclass of Entity
class Iteration(Entity):
    def __init__(self, name, description):
        super().__init__(name, description)

# Define test cases for the Entity class
entity_test_cases = [
    {
        "name": "Entity 1",
        "description": "Description 1"
    },
    {
        "name": "Entity 2",
        "description": "Description 2"
    }
]

# Test the Entity class
for test_case in entity_test_cases:
    entity = Entity(test_case["name"], test_case["description"])
    print(entity.name)
    print(entity.description)

# Define test cases for the Attribute class
attribute_test_cases = [
    {
        "name": "Attribute 1",
        "description": "Description 1",
        "data_type": "Data Type 1"
    },
    {
        "name": "Attribute 2",
        "description": "Description 2",
        "data_type": "Data Type 2"
    }
]

# Test the Attribute class
for test_case in attribute_test_cases:
    attribute = Attribute(test_case["name"], test_case["description"], test_case["data_type"])
    print(attribute.name)
    print(attribute.description)
    print(attribute.data_type)

# Define test cases for the Iteration class
iteration_test_cases = [
    {
        "name": "Iteration 1",
        "description": "Description 1"
    },
    {
        "name": "Iteration 2",
        "description": "Description 2"
    }
]

# Test the Iteration class
for test_case in iteration_test_cases:
    iteration = Iteration(test_case["name"], test_case["description"])
    print(iteration.name)
    print(iteration.description)
