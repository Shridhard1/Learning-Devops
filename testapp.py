import unittest
from app import hello

class TestApp(unittest.TestCase):
def test_hello(self):
self.assertEqual(hello(), "Hello,Jenkins!")

if_name_ "" "_main_":
unittest.main()
