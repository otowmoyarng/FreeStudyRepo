from Downloader import Downloader
import os
import pathlib
import unittest


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

    output_dir: str
    baseurl: str

    def setUp(self):
        """[summary]
        各テスト前に呼び出されるメソッド
        output_dirを初期化する
        Args:
            methodName ([type]): [description]
        """
        self.baseurl = "https://www.npa.go.jp/safetylife/seianki/jisatsu"

        pwd = pathlib.Path(__file__)
        self.output_dir = os.path.join(
            str(pwd.parents[1].resolve()), "downloaded")

    def test_Normal1(self):
        """[summary]
        正常系テスト
        取得可能なURLからデータファイルを取得する
        """
        downloadFinename = "202103zantei.xlsx"

        url = f'{self.baseurl}/R03/{downloadFinename}'
        # print(f'url:{url}')
        savefile = os.path.join(self.output_dir, downloadFinename)
        # print(f'savefile:{savefile}')
        removeOutputfile(savefile)

        ins = Downloader(url, savefile)
        ins.Do()

        self.assertTrue(os.path.exists(savefile))

    def test_Abnormal1(self):
        """[summary]
        異常系テスト
        取得不可なURLからデータファイルを取得する
        """
        downloadFinename = "202100zantei.xlsx"

        url = f'{self.baseurl}/R03/{downloadFinename}'
        savefile = os.path.join(self.output_dir, downloadFinename)
        removeOutputfile(savefile)

        ins = Downloader(url, savefile)
        ins.Do()

        self.assertTrue(os.path.exists(savefile))


if __name__ == "__main__":
    unittest.main()
