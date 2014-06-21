import unittest
from share import getMaxPriceByCompany
'''import pdb
print " i m here"
class MaxPriceTest(unittest.TestCase):
    def correct(self):
    	print "hgfjhgvbkjhhhj"
        self.assertEqual(getMaxPriceByCompany(),{'company d': {'price': 147, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 245, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}}
	)
    def dorrect(self):
    	print "hgfjhgvbkjhhhj"
        self.assertNotEqual(getMaxPriceByCompany(),{'company d': {'price': 147, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 245, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}}
	)

if __name__ == '__main__':
	#pdb.set_trace()
	unittest.main()

'''

import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def test_correct(self):
     	self.assertEqual(getMaxPriceByCompany(),{'company d': {'price': 247, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 245, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}} )  
    def test_wrong_values(self):
        	self.assertEqual(getMaxPriceByCompany(),{'company d': {'price': 247, 'month': 'december', 'year': '1991'}, 'company e': {'price': 245, 'month': 'june', 'year': '1991'}, 'company a': {'price': 546, 'month': 'march', 'year': '1991'}, 'company b': {'price': 215, 'month': 'jan', 'year': '1990'}, 'company c': {'price': 243, 'month': 'jan', 'year': '1990'}} )  
    
if __name__ == '__main__':
    unittest.main()