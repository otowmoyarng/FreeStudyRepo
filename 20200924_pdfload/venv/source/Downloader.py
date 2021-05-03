from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Tuple
from urllib.error import HTTPError
import os
import pathlib
import urllib.request


def getURL(addmonth: int = 0) -> str:
    """[summary]
    ダウンロードするURLを取得する
    Args:
        addmonth ([int]): 
    Returns:
        str: [description]
    """
    reiwaStartYear = 2019
    targetym = datetime.today() - relativedelta(months=(1 + addmonth))
    targetNendo = "R" + str(targetym.year - reiwaStartYear + 1).zfill(2)
    dataFilename = getFileName(addmonth)
    url = f'https://www.npa.go.jp/safetylife/seianki/jisatsu/{targetNendo}/{dataFilename}'
    return url


def getFileName(addmonth: int = 0) -> str:
    """[summary]
    ダウンロードするファイル名を取得する
    Args:
        addmonth ([int]): 
    Returns:
        str: [description]
    """
    targetym = datetime.today() - relativedelta(months=(1 + addmonth))
    dataFilename = str(targetym.year * 100 +
                       targetym.month) + "zantei.xlsx"
    return dataFilename


def getSavePath(addmonth: int = 0) -> str:
    """[summary]
    ダウンロード先のパスを取得する
    Args:
        addmonth ([int]): 
    Returns:
        str: [description]
    """
    pwd = pathlib.Path(os.path.abspath(__file__))
    savePath = os.path.join(
        str(pwd.parents[1].resolve()),
        "downloaded",
        getFileName(addmonth))
    return savePath


def download(url: str = None, addmonth: int = 0) -> Tuple[str, bool]:
    """[summary]
    指定したurlからファイルをダウンロードする
    Args:
        url ([str]): ダウンロード先のurl
        addmonth ([int]): 
    Returns:
        ダウンロードしたファイル
        ダウンロードできたか(true/false)
    """

    if url is None:
        url = getURL(addmonth)

    saveFile = getSavePath(addmonth)
    if os.path.exists(saveFile):
        print('ファイルが既にダウンロードされている')
        return saveFile, True

    print(f'url:{url}')
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
