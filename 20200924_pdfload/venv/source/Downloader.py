from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Tuple
from urllib.error import HTTPError
import os
import pathlib
import urllib.request


def getURL() -> str:
    """[summary]
    ダウンロードするURLを取得する

    Returns:
        str: [description]
    """
    reiwaStartYear = 2019
    targetym = datetime.today() - relativedelta(months=1)
    targetNendo = "R" + str(targetym.year - reiwaStartYear + 1).zfill(2)
    dataFilename = getFileName()
    url = f'https://www.npa.go.jp/safetylife/seianki/jisatsu/{targetNendo}/{dataFilename}'
    return url


def getFileName() -> str:
    """[summary]
    ダウンロードするファイル名を取得する

    Returns:
        str: [description]
    """
    targetym = datetime.today() - relativedelta(months=1)
    dataFilename = str(targetym.year * 100 +
                       targetym.month) + "zantei.xlsx"
    return dataFilename


def getSavePath() -> str:
    """[summary]
    ダウンロード先のパスを取得する

    Returns:
        str: [description]
    """
    pwd = pathlib.Path(os.path.abspath(__file__))
    savePath = os.path.join(
        str(pwd.parents[1].resolve()),
        "downloaded",
        getFileName())
    return savePath


def download(url: str = None) -> Tuple[str, bool]:
    """[summary]
    指定したurlからファイルをダウンロードする
    Args:
        url ([str]): ダウンロード先のurl
    Returns:
        ダウンロードしたファイル
        ダウンロードできたか(true/false)
    """

    if url is None:
        url = getURL()

    saveFile = getSavePath()
    if os.path.exists(saveFile):
        print('ファイルが既にダウンロードされている')
        return None, False

    try:
        urllib.request.urlretrieve(url, saveFile)
    except Exception as e:
        if type(e) == HTTPError:
            print('Error code: ', e.code)
            return None, False
        else:
            raise e
    else:
        return saveFile, True


if __name__ == "__main__":
    download(getURL(), getSavePath())
