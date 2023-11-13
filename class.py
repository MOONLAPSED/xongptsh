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
