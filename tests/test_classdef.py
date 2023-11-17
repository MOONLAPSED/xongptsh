# tests/test_classdef.py

import unittest

from app.classd.classdef import Attribute_, SpecificException


class TestAttribute(unittest.TestCase):
    def test_initialization(self):
        attribute = Attribute_("name", "description")
        self.assertEqual(attribute.name, "name")
        self.assertEqual(attribute.description, "description")

    def test_string_representation(self):
        attribute = Attribute_("name", "description")
        self.assertEqual(str(attribute), "['name', 'description']")

    def test_instance_creation(self):
        attribute = Attribute_()
        instance = attribute.create_instance(name="name", description="description")
        self.assertIsInstance(instance, Attribute_)
        self.assertEqual(instance.name, "name")
        self.assertEqual(instance.description, "description")

    def test_invalid_instance_creation(self):
        attribute = Attribute_()
        instance = attribute.create_instance()
        self.assertIsNone(instance)

    def test_exception_handling(self):
        attribute = Attribute_()
        with self.assertRaises(SpecificException):
            attribute.create_instance(name="name", description="description")


if __name__ == "__main__":
    unittest.main()
