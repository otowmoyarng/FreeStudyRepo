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

    def __mul__(self, newval : object):
        """[summary]
        __mul__オーバーライド
            分数の掛け算を行う
        argument:
            newval   積算する分数
        """
        # a/b * c/d=a*c/b*d
        # 分子を足し算する
        numerator_new = self.numerator * newval.numerator
        denominator_new = self.denominator * newval.denominator

        # 分数の結果を返す
        newfra = Fraction(numerator_new, denominator_new)
        return newfra

    def __truediv__(self, newval : object):
        """[summary]
        __truediv__オーバーライド
            分数の割り算を行う
        argument:
            newval   除算する分数
        """
        # a/b / c/d=a/b * d/c=a*d/b*c
        # 分子と分母を入れ替える
        divcal = Fraction(newval.denominator, newval.numerator)
        newfra = self.__mul__(divcal)
        return newfra

    def __iadd__(self, newval : object):
        """[summary]
        __iadd__オーバーライド
            分数の足し算を行う
        argument:
            newval   加算する分数
        """
        return self.__add__(newval)

    def __isub__(self, newval : object):
        """[summary]
        __isub__オーバーライド
            分数の引き算を行う
        argument:
            newval   減算する分数
        """
        return self.__sub__(newval)

    def __imul__(self, newval : object):
        """[summary]
        __imul__オーバーライド
            分数の掛け算を行う
        argument:
            newval   積算する分数
        """
        return self.__mul__(newval)

    def __itruediv__(self, newval : object):
        """[summary]
        __itruediv__オーバーライド
            分数の割り算を行う
        argument:
            newval   除算する分数
        """
        return self.__truediv__(newval)

    # TODO 
    # TODO 
    # TODO 
    # TODO 
    # TODO 
