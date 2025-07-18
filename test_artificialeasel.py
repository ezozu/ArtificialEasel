# test_artificialeasel.py
"""
Tests for ArtificialEasel module.
"""

import unittest
from artificialeasel import ArtificialEasel

class TestArtificialEasel(unittest.TestCase):
    """Test cases for ArtificialEasel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEasel()
        self.assertIsInstance(instance, ArtificialEasel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEasel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
