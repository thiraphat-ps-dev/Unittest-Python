# -- coding: utf-8 --
import unittest


#สร้าง ฟังชั่น ทีหลัง
def add_num(a, b):
    return a + b

# เขียน unittest ก่อน
class MyTest(unittest.TestCase):
    def test_add(self):
        result = add_num(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
