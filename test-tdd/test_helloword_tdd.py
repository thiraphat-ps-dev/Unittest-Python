import unittest

def helloword():
    return 'helloword'

class TestCase(unittest.TestCase):
    def test_helloword(self):
        self.assertEqual(helloword(),'helloword')

if __name__ == '__main__':
    unittest.main()
