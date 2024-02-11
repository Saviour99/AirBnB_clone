#!/usr/bin/python3
"""Base_model Module Testing"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """TestBaseModel Class for testing"""

    def test_init(self):
        MyTest = BaseModel()

        self.assertIsNotNone(MyTest.id)
        self.assertIsNotNone(MyTest.created_at)
        self.assertIsNotNone(MyTest.updated_at)

    def test_save(self):
        MyTest = BaseModel()

        initial_update = MyTest.updated_at
        current_update = MyTest.save()

        self.assertNotEqual(current_update, initial_update)

    def test_inst_to_dict(self):
        MyTest = BaseModel()

        MyTest_dict = MyTest.to_dict()
        self.assertIsInstance(MyTest_dict, dict)

        self.assertEqual(MyTest_dict["__class__"], "BaseModel")
        self.assertEqual(MyTest_dict["id"], MyTest.id)
        self.assertEqual(MyTest_dict["created_at"], MyTest.created_at.isoformat())
        self.assertEqual(MyTest_dict["updated_at"], MyTest.updated_at.isoformat())

    def test_str(self):
        MyTest = BaseModel()

        self.assertTrue(str(MyTest).startswith("[BaseModel]"))
        self.assertIn(MyTest.id, str(MyTest))
        self.assertIn(str(MyTest.__dict__), str(MyTest))

if __name__  == "__main__":
    unittest.main()
