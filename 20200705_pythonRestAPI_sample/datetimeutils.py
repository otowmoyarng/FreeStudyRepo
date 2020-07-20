# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class DateTimeUtils:

    @staticmethod
    def responcedate(days : int=0) -> str:
        """[summary]
        APIレスポンスにセットする日付文字列を返す。
        Args:
            datevalue (datetime.date): 戻り値となる日付
        Returns:
            str: APIレスポンスとなる戻り値
        """
        datevalue = datetime.today() + timedelta(days=days)
        return datetime.strftime(datevalue, "%Y/%m/%d")

if __name__ == "__main__":
    day_array = (-1,0,1)
    except_label = ("昨日：","今日：","明日：")
    for count in range(3):
        print(except_label[count] + DateTimeUtils.responcedate(day_array[count]))
