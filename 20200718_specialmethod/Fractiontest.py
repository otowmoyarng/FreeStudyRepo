# -*- coding: utf-8 -*-
import unittest
from Fraction import Fraction

class Fractiontest(unittest.TestCase):
    """[summary]
    Fractionクラスのユニットテストクラス
    """

    def test_constructor(self):
        """[summary]
        コンストラクタのテストメソッド
        """
        bunsi, bunbo = 3, 7
        fra = Fraction(bunsi, bunbo)
        self.assertEqual(bunsi, fra.numerator)
        self.assertEqual(bunbo, fra.denominator)

    def test_add(self):
        """[summary]
        __add__と__iadd__のテストメソッド
        """
        fra_base = Fraction(1,2)
        fra_add = Fraction(1,3)
        fra_exp = Fraction(5,6)

        fra_calc = fra_base + fra_add
        self.assertEqual(fra_exp.numerator, fra_calc.numerator)
        self.assertEqual(fra_exp.denominator, fra_calc.denominator)

        fra_base += fra_add
        self.assertEqual(fra_exp.numerator, fra_base.numerator)
        self.assertEqual(fra_exp.denominator, fra_base.denominator)

    def test_sub(self):
        """[summary]
        __sub__と__isub__のテストメソッド
        """
        fra_base = Fraction(1,2)
        fra_sub = Fraction(1,3)
        fra_exp = Fraction(1,6)

        fra_calc = fra_base - fra_sub
        self.assertEqual(fra_exp.numerator, fra_calc.numerator)
        self.assertEqual(fra_exp.denominator, fra_calc.denominator)

        fra_base -= fra_sub
        self.assertEqual(fra_exp.numerator, fra_base.numerator)
        self.assertEqual(fra_exp.denominator, fra_base.denominator)

    def test_mul(self):
        """[summary]
        __mul__と__imul__のテストメソッド
        """
        fra_base = Fraction(1,2)
        fra_mul = Fraction(1,3)
        fra_exp = Fraction(1,6)

        fra_calc = fra_base * fra_mul
        self.assertEqual(fra_exp.numerator, fra_calc.numerator)
        self.assertEqual(fra_exp.denominator, fra_calc.denominator)

        fra_base *= fra_mul
        self.assertEqual(fra_exp.numerator, fra_base.numerator)
        self.assertEqual(fra_exp.denominator, fra_base.denominator)

    def test_truediv(self):
        """[summary]
        __truediv__と__itruediv__のテストメソッド
        """
        fra_base = Fraction(1,2)
        fra_truediv = Fraction(1,3)
        fra_exp = Fraction(3,2)

        fra_calc = fra_base / fra_truediv
        self.assertEqual(fra_exp.numerator, fra_calc.numerator)
        self.assertEqual(fra_exp.denominator, fra_calc.denominator)

        fra_base /= fra_truediv
        self.assertEqual(fra_exp.numerator, fra_base.numerator)
        self.assertEqual(fra_exp.denominator, fra_base.denominator)
