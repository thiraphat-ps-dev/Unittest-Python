# -- coding: utf-8 --
import unittest           #อิมพอร์ตไลบรารี่ unittest สำหรับใช้สร้างเทสเคส

def add(x, y):            # สร้าง ฟังชั่น ชื่อว่า แอด รับตัวแปร x และ y
    return x + y          # ส่งค่า x บวก y กลับไป เมื่อเรียกใช้งานฟังชั่น


def multipy(x, y):     
    return x * y       


def divi(x, y):  
    return x / y      


def minus(x, y):
    return x - y 


class TestCase(unittest.TestCase):          #สร้าง คลาส เทสเคส โดยเรียกใช้ ไลบรารี่ unittest.TestCase

    def test_add(self):             #สร้างเทสเคสในรูปแบบฟังชั่น ชื่อ test_add
        result = add(4, 6)          #สร้างตัวแปร result เก็บค่า ที่ได้จากการ เรียกใช้ฟังชั่น add โดยใส่ค่า x , y เป็น 4 , 6 ก็คือ 4+6
        act = 10                    #คำตอบที่ควรจะได้ คือ 10 4+6=10
        self.assertEqual(           #ใช้ assertEqual เพื่อเปรียบเทียบค่า 
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))          
            #ternary operator การเขียน condition แบบ true or false เช่น ถ้าคำตอบถูก เป็น true เทสผ่าน ถ้าผิด เป็น false แสดงข้อความ เกิดข้อผิดพลาด
    
    def test_multiply(self):
        result = multipy(4, 2)
        act = 8
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
            

    def test_divi(self):
        result = divi(4, 2)
        act = 2
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))

    def test_minus(self):
        result = minus(14, 2)
        act = 12
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))


if __name__ == '__main__':
    unittest.main()
