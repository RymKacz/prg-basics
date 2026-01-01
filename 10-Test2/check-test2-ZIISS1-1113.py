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
        self.assertEqual(p1.f("{1}{[(2)(3)](4)[(5)]}"),True)
        self.assertEqual(p1.f("{1}{[(2)(3)](4)[(5])}"),False)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(10, 0.95, 5),14)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f(5),"*/*/*/*/*")
        self.assertEqual(p3.f(0),"")
        self.assertEqual(p3.f(1),"*")

    def test_p4(self):
        import p4
        sub_grades = {"prg":[4,4,5,5], "hist":[4,4,5], "econ":[5,4,5,5], "alg":[5,4]}
        self.assertEqual(p4.f(sub_grades),"econ")

    def test_p5(self):
        import p5
        cart = {"juice":4, "cheese":2}
        prices = {"juice":2.99, "bread":2.19, "butter":3.09, "milk":1.29, "cheese":7}
        self.assertEqual(p5.f(cart, prices, 26),True)
        self.assertEqual(p5.f(cart, prices, 25),False)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("za153"),True)
        self.assertEqual(p6.f("zA9999"),True)
        self.assertEqual(p6.f("G12345"),False)
        self.assertEqual(p6.f("AbC2"),False)

    def test_p7(self):
        import p7
        email = "To buy: 3 papers, 12 pencils."
        self.assertEqual(p7.f(email)["pencils"],12)
        self.assertEqual(p7.f(email)["papers"],3)
        self.assertEqual(len(p7.f(email)),2)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f("2KTQ7A"),"AKQT72")

    def test_p9(self):
        import p9
        post1 = "aaa #bb #ccc dddd #eeeee fff #ggg #hhh iii #jjjjj"
        post2 = "#b #jjjjj #eeeee #kk #ggg bbb #hhh #mmmm nnnnnn"
        self.assertEqual(p9.f(post1,post2),["eeeee","ggg","hhh","jjjjj"])

    def test_p10(self):
        import p10
        quiz_answers = "1a,2a,3a,4a,5a,6a,7d,8d,9d,10d,11d,12d"
        student1 = "5a,1b,6a,7d,3a,4a"
        student2 = "1b,5a,6a,7d,3b,10d,11d"
        self.assertEqual(p10.f(quiz_answers,student1,student2),3)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
