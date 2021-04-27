import os
import urllib.request


class Downloader:

    url: str
    saveDir: str
    saveFile: str
    saveFilePath: str

    def __init__(self, url: str, savedir: str, savefile: str):
        """[summary]
        コンストラクタ
        Args:
            url ([str]): ダウンロード先のurl
            savedir ([str]): ダウンロードファイルの保存先フルパス
            savefile ([str]): ダウンロードファイル名
        """
        super().__init__()
        self.url = url
        self.saveDir = savedir
        self.saveFile = savefile
        self.saveFullpath = savedir + os.sep + savefile

    def download(self):
        """[summary]
        指定したurlからファイルをダウンロードする
        Args:
            url ([str]): ダウンロード先のurl
            downloadfile ([str]): ダウンロードファイルのフルパス
        Returns:
            ダウンロードしたファイル
        """

        if self.url is None:
            print('URLが指定されていない')
            return

        if os.path.exists(self.saveFullpath):
            print('ファイルが既にダウンロードされている')
            return

        data = urllib.request.urlopen(self.url).read()
        with open(self.saveFullpath, mode="wb") as f:
            f.write(data)
