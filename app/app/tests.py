"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
  """Test the calc module."""


  def test_add_numbers(self):
    """Test adding numbers together"""
    res = calc.add(3,4)

    self.assertEqual(res, 7)


  def test_substract_numbers(self):
    """Test subtracting numbers"""
    res = calc.subtract(8,3)

    self.assertEqual(res, 5)