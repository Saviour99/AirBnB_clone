#!/usr/bin/python3
"""Testing Filestorage"""

from models.engine.file_storage import FileStorage
import os
import unittest
from models.base_model import BaseModel
import models

class TestFileStorageInitaniation(unittest.TestCase):
    """Testing class"""
    def test_FileStorage_instatiation(self):
        self.assertNotEqual(type(FileStorage), FileStorage)

    def test_storage_instantiation(self):
        self.assertEqual(type(models.storage), FileStorage)



if __name__ == "__main__":
    unittest.main()
