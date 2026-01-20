# -*- coding: utf-8 -*-
"""
Unit tests for tasks p1.py ... p10.py (based on TEST3 ZIISS1-1113 PDF).

How to use:
1) Put this file in the same folder as: p1.py, p2.py, ..., p10.py
2) Run:  python unit_tests_t3.py
3) A unittest report will be written to results.txt (same style as the provided example).

Notes:
- The tests include all example assertions from the PDF for each task.
- Additionally, two extra assertions are added for each task.
- Comments inside tests are in English (as requested).
"""

import sys
import unittest


class TestT3(unittest.TestCase):

    # (p1.py) Count people in the room from '+' (enter) and '-' (leave)
    def test_p1(self):
        import p1

        # Examples from the PDF
        self.assertEqual(p1.f(""), 0)
        self.assertEqual(p1.f("+-+"), 1)
        self.assertEqual(p1.f("+-+++-+---"), 0)
        self.assertEqual(p1.f("+-+++++-"), 4)

        # +2 additional assertions
        self.assertEqual(p1.f("++++"), 4)          # only entries
        self.assertEqual(p1.f("++--+-"), 0)        # balanced sequence

    # (p2.py) Reverse Polish Notation (RPN) with non-negative integers and +/-
    def test_p2(self):
        import p2

        # Examples from the PDF
        self.assertEqual(p2.f("2 3 4 5 + - +"), -4)
        self.assertEqual(p2.f("11 7 + 15 - 14 +"), 17)

        # +2 additional assertions
        self.assertEqual(p2.f("0 0 +"), 0)               # 0 + 0
        self.assertEqual(p2.f("10 2 3 + -"), 5)          # 10 - (2 + 3)

    # (p3.py) Validate a variable name: length 1..5, allowed characters by position
    def test_p3(self):
        import p3

        # Examples from the PDF
        self.assertTrue(p3.f("aBC"))
        self.assertTrue(p3.f("_ab_c"))
        self.assertFalse(p3.f("abcdef"))
        self.assertFalse(p3.f("8abc"))
        self.assertTrue(p3.f("_aB8_"))

        # +2 additional assertions
        self.assertTrue(p3.f("A9"))              # uppercase letter then digit
        self.assertFalse(p3.f("-ab"))            # invalid first character

    # (p4.py) Class C: identifier from first 2 letters of name, first 2 letters of surname, and age
    # Format: "XX-YY-age"; lowercase if age < 18, uppercase otherwise
    def test_p4(self):
        import p4

        # Examples from the PDF (we test string representation)
        self.assertEqual(str(p4.C("John", "May", 18)), "JO-MA-18")
        self.assertEqual(str(p4.C("Anna", "Brown", 17)), "an-br-17")

        # +2 additional assertions
        self.assertEqual(str(p4.C("Li", "Xu", 18)), "LI-XU-18")      # exactly 2+2 letters
        self.assertEqual(str(p4.C("Eva", "Stone", 1)), "ev-st-1")    # child -> lowercase

    # (p5.py) Stadium sectors: m1 updates/adds sector, m2 sums fans for sectors listed in a string
    def test_p5(self):
        import p5

        # Examples from the PDF
        stadium = p5.C({"A": 120, "D": 150, "G": 90, "K": 110})
        stadium.m1("G", 130)
        self.assertEqual(stadium.m2("GD"), 280)
        self.assertEqual(stadium.m2("KEJ"), 110)

        # +2 additional assertions
        stadium.m1("E", 50)                       # add a new sector
        self.assertEqual(stadium.m2("EGA"), 300)   # 50 + 130 + 120
        self.assertEqual(stadium.m2("Z"), 0)       # unknown sector contributes 0

    # (p6.py) Filter results by predicate fnc and return max*min among filtered values
    def test_p6(self):
        import p6

        res = [95, 90, 20, 50, 70]

        # Examples from the PDF
        fnc1 = lambda x: x > 50
        fnc2 = lambda x: x > 30 and x < 90
        self.assertEqual(p6.f(fnc1, res), 6650)  # 95 * 70
        self.assertEqual(p6.f(fnc2, res), 3500)  # 70 * 50

        # +2 additional assertions
        fnc3 = lambda x: x >= 90
        fnc4 = lambda x: x % 2 == 0
        self.assertEqual(p6.f(fnc3, res), 8550)  # 95 * 90
        self.assertEqual(p6.f(fnc4, res), 1800)  # 90 * 20

    # (p7.py) Sort file names by extension (ascending, based on the extension substring)
    def test_p7(self):
        import p7

        # Example from the PDF
        files = ["a.txt", "bb.pdf", "ccc.py", "dddd.mpeg4"]
        self.assertEqual(p7.f(files), ["dddd.mpeg4", "bb.pdf", "ccc.py", "a.txt"])

        # +2 additional assertions
        files2 = ["readme.md", "data.csv", "image.png"]
        self.assertEqual(p7.f(files2), ["data.csv", "readme.md", "image.png"])  # csv < md < png

        files3 = ["x.c", "y.a", "z.b"]
        self.assertEqual(p7.f(files3), ["y.a", "z.b", "x.c"])                  # a < b < c

    # (p8.py) Counter class C with methods m1..m4 and __str__ formatting as #value#
    def test_p8(self):
        import p8

        # Example from the PDF
        c = p8.C(5)
        self.assertEqual(c.m1(), 5)
        c.m2(); self.assertEqual(c.m1(), 6)
        c.m4(-8); self.assertEqual(c.m1(), -2)
        c.m3(); self.assertEqual(c.m1(), -3)
        c.m4(10); self.assertEqual(c.m1(), 7)
        self.assertEqual(str(c), "#7#")

        # +2 additional assertions
        c.m4(0); self.assertEqual(c.m1(), 7)      # no change
        c.m2(); c.m2(); self.assertEqual(c.m1(), 9)

    # (p9.py) Car usage list: order=1 -> Krakow plates (KR/KK) alphabetically; order=2 -> all by mileage desc
    def test_p9(self):
        import p9

        cars = [{"KR333": 138}, {"WL555": 497}, {"KK444": 341}, {"KK222": 412}]

        # Examples from the PDF (interpreting the intended output; order=1 filters KR/KK)
        self.assertEqual(p9.f(cars, 1), [{"KK222": 412}, {"KK444": 341}, {"KR333": 138}])

        # The PDF seems to contain a small typo in the example output keys.
        # Intended behavior per task text: order=2 sorts ALL cars by mileage, descending.
        self.assertEqual(p9.f(cars, 2), [{"WL555": 497}, {"KK222": 412}, {"KK444": 341}, {"KR333": 138}])

        # +2 additional assertions
        cars2 = [{"KR1": 10}, {"KK2": 30}, {"PO3": 20}]
        self.assertEqual(p9.f(cars2, 1), [{"KK2": 30}, {"KR1": 10}])                   # only KR/KK, alphabetical
        self.assertEqual(p9.f(cars2, 2), [{"KK2": 30}, {"PO3": 20}, {"KR1": 10}])    # all, by mileage desc

    # (p10.py) Extract full-date format: D Month YYYY (English month with Capitalized first letter)
    def test_p10(self):
        import p10

        # Example from the PDF
        dates = "17 July 1999;05/12/2024;April 7 2014,9 May 2007;;2001-12-07:,1 May 23"
        self.assertEqual(p10.f(dates), ["17 July 1999", "9 May 2007"])

        # +2 additional assertions
        dates2 = "4 January 2025,04 January 2025;4 january 2025"
        self.assertEqual(p10.f(dates2), ["4 January 2025", "04 January 2025"])  # keep originals, both match pattern

        dates3 = "31 June 2010;1 May 2023;0 May 2020"
        self.assertEqual(p10.f(dates3), ["31 June 2010", "1 May 2023", "0 May 2020"])  # pattern-based, not semantic


if __name__ == "__main__":
    # Write the unittest report to results.txt (same approach as in the example file)
    sys.stderr = open("results.txt", "w", encoding="utf-8")
    unittest.main(verbosity=2)
