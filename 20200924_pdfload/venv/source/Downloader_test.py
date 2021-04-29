from Downloader import getURL, getFileName, getSavePath, download
from datetime import datetime
from dateutil.relativedelta import relativedelta
import freezegun
import os
import pathlib
import unittest

now = datetime.now()
lastmonth = now - relativedelta(months=1)


def removeOutputfile(filepath: str):
    """[summary]
    指定したファイルが存在する場合は削除する。
    テストメソッド実行前に実行される
    """
    # ファイルを削除する
    if os.path.exists(filepath):
        os.remove(filepath)


class DownloaderTest(unittest.TestCase):
    """[summary]
    Downloaderのテストクラス
    Args:
        unittest ([type]): [description]
    """

    expect_url: str = "https://www.npa.go.jp/safetylife/seianki/jisatsu/R03/202103zantei.xlsx"
    expect_savePath: str = R"C:\Users\ut\Documents\FreeStudyRepo\20200924_pdfload\venv\downloaded\202103zantei.xlsx"

    @freezegun.freeze_time(now)
    def test_getURL1(self):
        """[summary]
        正常系テスト
        取得可能なURLを取得する
        """
        url = getURL()
        self.assertEqual(self.expect_url, url)

    @freezegun.freeze_time(lastmonth)
    def test_getURL2(self):
        """[summary]
        異常系テスト
        取得可能なURLを取得する
        """
        url = getURL()
        self.assertNotEqual(self.expect_url, url)

    @freezegun.freeze_time(now)
    def test_getFileName(self):
        """[summary]
        正常系テスト
        取得可能なURLを取得する
        """
        fileName = getFileName()
        expect_fileName = "202103zantei.xlsx"
        self.assertEqual(expect_fileName, fileName)

    @freezegun.freeze_time(now)
    def test_getSavePath(self):
        """[summary]
        正常系テスト
        取得可能なURLを取得する
        """
        savePath = getSavePath()
        self.assertEqual(self.expect_savePath, savePath)

    @freezegun.freeze_time(now)
    def test_download1(self):
        """[summary]
        正常系テスト
        取得可能なURLからデータファイルを取得する
        """
        removeOutputfile(self.expect_savePath)
        datafile, candl = download()
        self.assertEqual(self.expect_savePath, datafile)
        self.assertTrue(candl)

    @freezegun.freeze_time(lastmonth)
    def test_download2(self):
        """[summary]
        異常系テスト
        取得不可なURLからデータファイルを取得する
        """
        removeOutputfile(self.expect_savePath)
        datafile, candl = download()
        self.assertIsNone(datafile)
        self.assertFalse(candl)


if __name__ == "__main__":
    unittest.main()
