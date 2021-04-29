import os
import urllib.request


class Downloader:

    url: str
    saveFile: str

    def __init__(self, url: str, savefile: str):
        """[summary]
        コンストラクタ
        Args:
            url ([str]): ダウンロード先のurl
            savefile ([str]): ダウンロードファイル名
        """
        super().__init__()
        self.url = url
        self.saveFile = savefile

    def Do(self):
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

        if os.path.exists(self.saveFile):
            print('ファイルが既にダウンロードされている')
            return

        urllib.request.urlretrieve(self.url, self.saveFile)
        # data = urllib.request.urlopen(self.url).read()
        # with os.open(self.saveFile, mode="wb") as f:
        #     f.write(data)
