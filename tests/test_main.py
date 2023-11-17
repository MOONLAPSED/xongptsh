import unittest

from app.classd.classdef import Entity


class TestMain(unittest.TestCase):
    def test_entity_initialization(self):
        # Test case 1
        entity1 = Entity("Entity 1", "Description 1")
        self.assertEqual(entity1.name, "Entity 1")
        self.assertEqual(entity1.description, "Description 1")

        # Test case 2
        entity2 = Entity("Entity 2", "Description 2")
        self.assertEqual(entity2.name, "Entity 2")
        self.assertEqual(entity2.description, "Description 2")


if __name__ == "__main__":
    unittest.main()
