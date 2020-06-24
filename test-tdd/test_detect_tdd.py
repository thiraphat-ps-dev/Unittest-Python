import unittest
import re

def detectString(text):
    return True if re.findall("[a-zA-Z]", text) else False

def detectNumber(number):
    return True if re.findall("[0-9]", number) else False

class TestCase(unittest.TestCase):

    def test_detect_string_1(self):
        self.assertEqual(True,True)

    def test_detect_string_2(self):
        self.assertEqual(detectString('helloword123'),True)

    def test_detect_string_3(self):
        self.assertEqual(detectString('4254'),False)

    def test_detect_number_1(self):
        self.assertEqual(True,True)

    def test_detect_number_2(self):
        self.assertEqual(detectNumber('helloword'),False)

    def test_detect_number_3(self):
        self.assertEqual(detectNumber('1234'),True)




if __name__ == "__main__":
    unittest.main()