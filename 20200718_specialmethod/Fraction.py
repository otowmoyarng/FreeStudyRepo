# -*- coding: utf-8 -*-

class Fraction(object):
    """[summary]
    Fraction
        分数クラス
    """

    numerator = 0   # 分子
    denominator = 0 # 分母

    def __init__(self, numerator : int, denominator : int):
        """[summary]
        コンストラクタ
            プロパティをセットする
        argument:
            numerator   分子
            denominator 分母
        """
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, newval : object):
        """[summary]
        __add__オーバーライド
            分数の足し算を行う
        argument:
            newval   加算する分数
        """
        # 通分する
        denominator_new = self.denominator * newval.denominator

        # 分子を足し算する
        numerator_new1 = self.numerator * newval.denominator
        numerator_new2 = newval.numerator * self.denominator

        # 分数の結果を返す
        newfra = Fraction(numerator_new1 + numerator_new2, denominator_new)
        return newfra

    def __sub__(self, newval : object):
        """[summary]
        __sub__オーバーライド
            分数の引き算を行う
        argument:
            newval   減算する分数
        """
        # 通分する
        denominator_new = self.denominator * newval.denominator

        # 分子を足し算する
        numerator_new1 = self.numerator * newval.denominator
        numerator_new2 = newval.numerator * self.denominator

        # 分数の結果を返す
        newfra = Fraction(numerator_new1 - numerator_new2, denominator_new)
        return newfra

if __name__ == "__main__":
    fra1 = Fraction(1,2)
    print('{}/{}'.format(fra1.numerator, fra1.denominator))

    fra2 = Fraction(1,3)
    print('{}/{}'.format(fra2.numerator, fra2.denominator))

    fra11 = fra1 + fra2
    print('{}/{}'.format(fra11.numerator, fra11.denominator))

    fra12 = fra1 - fra2
    print('{}/{}'.format(fra12.numerator, fra12.denominator))
