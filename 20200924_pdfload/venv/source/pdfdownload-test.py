from dateutil.relativedelta import relativedelta
from datetime import datetime
from pdfdownload import download
from icecream import ic
import os
import requests
import unittest

def removeOutputfile(filepath : str):
    """[summary]
    指定したファイルが存在する場合は削除する。
    テストメソッド実行前に実行される
    """
    # ファイルを削除する
    if os.path.exists(filepath):
        os.remove(filepath)

class TestPdfdownload(unittest.TestCase):
    """[summary]
    pdfdownloadのテストクラス
    Args:
        unittest ([type]): [description]
    """

    output_dir : str

    def setUp(self):
        """[summary]
        各テスト前に呼び出されるメソッド
        output_dirを初期化する
        Args:
            methodName ([type]): [description]
        """
        self.output_dir = os.getcwd()

    def test_Normal1(self):
        """[summary]
        PDFファイルの正常系テスト
        取得可能なURLからPDFファイルを取得する
        """
        one_month_ago = datetime.strftime(datetime.today() - relativedelta(months=2), '%m')
        url = f'https://www.npa.go.jp/safetylife/seianki/jisatsu/R02/zanteiti02{one_month_ago}.pdf'
        downloadfile = self.output_dir + '\\downloaded\\downloaded_Normal1.pdf'

        removeOutputfile(downloadfile)
        download(url, downloadfile)

        self.assertTrue(os.path.exists(downloadfile))

    def test_Abnormal1(self):
        """[summary]
        PDFファイルの異常系テスト
        取得不可なURLからPDFファイルを取得する
        """
        one_month_ago = datetime.strftime(datetime.today() - relativedelta(months=1), '%m')
        url = f'https://www.npa.go.jp/safetylife/seianki/jisatsu/R03/zanteiti02{one_month_ago}.pdf'
        downloadfile = self.output_dir + '\\downloaded\\downloaded_Normal1.pdf'

        removeOutputfile(downloadfile)
        try:
            download(url, downloadfile)
            self.assertFalse(os.path.exists(downloadfile))
        except Exception as ex:
            print(type(ex))

if __name__ == "__main__":
    unittest.main()