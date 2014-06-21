import unittest
from share import getMaxPriceByCompany

class TestSequenceFunctions(unittest.TestCase):
    def test_correct(self):
     	self.assertEqual(getMaxPriceByCompany(),{'company d': {'price': 247, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 245, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}} )  
    def test_wrong_values(self):
        	self.assertEqual(getMaxPriceByCompany(),{'company d': {'price': 247, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 215, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}} )  
    
if __name__ == '__main__':
    unittest.main()