from DataReader import DataReader
import unittest


class DataReaderTest(unittest.TestCase):

    ins: DataReader

    def setUp(self):
        """[summary]
        setUp:テスト実行前メソッド
        環境変数に期待値をセットする

        Returns:
            Not Returns
        """
        datafile = R"C:\Users\ut\Documents\FreeStudyRepo\20200924_pdfload\venv\downloaded\202103zantei.xlsx"
        self.ins = DataReader(datafile)

    def test_getGrandTotal(self):
        """[summary]
        自殺者総数を取得する
        """
        totals = self.ins.getGrandTotal()
        self.assertEqual(13, len(totals), "自殺者総数")
        for k, v in totals.items():
            self.assertEqual(3, len(v), k)

    def test_getPrefecture(self):
        """[summary]
        都道府県別自殺者数を取得する
        """
        totals = self.ins.getPrefecture()
        self.assertEqual(13, len(totals), "都道府県別自殺者数")
        for k, v in totals.items():
            self.assertEqual(47, len(v), k)


if __name__ == "__main__":
    unittest.main()
