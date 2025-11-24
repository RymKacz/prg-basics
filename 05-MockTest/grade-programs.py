'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(31),7)
        self.assertEqual(p1.f(8),3)
        self.assertEqual(p1.f(2),1)
        self.assertEqual(p1.f(0),0)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(5,6,7),True)
        self.assertEqual(p2.f(5,7,5),False)
        self.assertEqual(p2.f(5,5,7),False)
        self.assertEqual(p2.f(7,5,5),False)
        self.assertEqual(p2.f(7,7,7),False)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("For Your Information"),"FYI")
        self.assertEqual(p3.f("Hello Poland Krakow university"),"HPKu")

    def test_p4(self):
        import p4
        self.assertEqual(p4.f("5290312400019022"),"52**********9022")
        self.assertEqual(p4.f("1111000022227777"),"11**********7777")

    def test_p5(self):
        import p5
        self.assertEqual(p5.f("101101"),True)
        self.assertEqual(p5.f("1011201"),False)
        self.assertEqual(p5.f("1010b1"),False)
        self.assertEqual(p5.f("0b11"),False)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f(3124,True),6)
        self.assertEqual(p6.f(20576,False),12)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f(5),3)
        self.assertEqual(p7.f(9),21)
        self.assertEqual(p7.f(17),987)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f("radar"),True)
        self.assertEqual(p8.f("12-11-21"),True)
        self.assertEqual(p8.f("book"),False)

    def test_p9(self):
        import p9
        self.assertEqual(p9.f("water"),2)
        self.assertEqual(p9.f("hello world"),3)
        self.assertEqual(p9.f("to be or not to be"),6)

    def test_p10(self):
        import p10
        self.assertEqual(p10.f("hello world"),True)
        self.assertEqual(p10.f("university"),True)
        self.assertEqual(p10.f("student"),False)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
