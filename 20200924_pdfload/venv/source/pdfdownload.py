from dateutil.relativedelta import relativedelta
from datetime import datetime
import os
import requests
import shutil

def download(url : str, downloadfile : str):
    """[summary]
    指定したurlからファイルをダウンロードする
    Args:
        url ([str]): ダウンロード先のurl
        downloadfile ([str]): ダウンロードファイルのフルパス
    Returns:
        ダウンロードしたファイル
    """
    
    if url is None:
        print('URLが指定されていない')
        return
    
    if os.path.exists(downloadfile):
        print('ファイルが既にダウンロードされている')
        return

    try:
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
            with open(downloadfile, mode='wb') as dfile:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, dfile)
        else:
            r.raise_for_status()
    except requests.exceptions.RequestException as ex:
        print(ex)
        raise ex

if __name__ == "__main__":
    one_month_ago = datetime.strftime(datetime.today() - relativedelta(months=2), '%m')
    url = f'https://www.npa.go.jp/safetylife/seianki/jisatsu/R02/zantei02{one_month_ago}.pdf'
    downloadfile = os.getcwd() + f'\\zantei02{one_month_ago}.pdf'
    download(url, downloadfile)