def func(text):
    return text.title()

import unittest

class LetsTest(unittest.TestCase):
    def test1(self):
        test_input = 'temporary'
        self.assertEqual(func(test_input),'Temporary')
    def test2(self):
        test_input = 'EQUILIBRI INFINITIUM'
        self.assertEqual(func(test_input),'Equilibri Infinitium')
    def test3(self):
        test_input = 'the red brown fox jumps over the lazy dog'
        self.assertEqual(func(test_input),'The Red Brown Fox Jumps Over The Lazy Dog')
        
if __name__ == '__main__':
    unittest.main()
