
import xlrd
from typing import List, Dict


class DataReader():

    sheet: xlrd.sheet.Sheet

    def __init__(self, datafile: str) -> None:
        """[summary]
        コンストラクタ
        Args:
            datafile (str): 読み込み対象ファイル
        """
        self.sheet = xlrd.open_workbook(datafile).sheets()[0]

    def getTotal(self, meisaititles: List[str], startindex: int) -> Dict:
        """[summary]
        自殺者総数を取得する
        """
        totals = {}

        for columnindex in range(13):
            total = {}
            for rowindex in range(len(meisaititles)):
                value = self.sheet.cell_value(
                    (startindex + rowindex), (2 + columnindex))

                if value == "":
                    total[meisaititles[rowindex]] = 0
                else:
                    total[meisaititles[rowindex]] = int(value)

            totalkey: str = None
            if columnindex == 0:
                totalkey = "合計"
            else:
                totalkey = str(columnindex) + "月"
            totals[totalkey] = total

        return totals

    def getGrandTotal(self) -> Dict:
        """[summary]
        自殺者総数を取得する
        """
        meisaititles = ["total", "mens", "womens"]
        totals = self.getTotal(meisaititles, 3)
        return totals

    def getPrefecture(self) -> Dict:
        """[summary]
        都道府県別自殺者数を取得する
        """
        meisaititles = ["hokkaido", "aomori", "iwate", "miyagi", "akita", "yamagata", "fukushima", "tokyo", "ibaraki", "tochigi", "gunma", "saitama", "chiba",
                        "kanagawa", "niigata", "yamanashi", "nagano", "sizuoka", "toyama", "ishikawa", "fukui", "gifu", "aichi", "mie", "shiga", "kyoto",
                        "osaka", "hyogo", "nara", "wakayama", "tottori", "shimane", "okayama", "hiroshima", "yamaguchi", "tokushima", "kagawa", "ehime",
                        "kochi", "fukuoka", "saga", "nagasaki", "kumamoto", "oita", "miyazaki", "kagoshima", "okinawa"]
        totals = self.getTotal(meisaititles, 9)
        return totals


if __name__ == "__main__":
    datafile = R"C:\Users\ut\Documents\FreeStudyRepo\20200924_pdfload\venv\downloaded\202103zantei.xlsx"
    dr = DataReader(datafile)
    totals = dr.getTotal()
    print(totals)
