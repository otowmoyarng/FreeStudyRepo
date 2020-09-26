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
        with open(downloadfile, mode='wb') as dfile:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, dfile)
    except requests.exceptions.RequestException as ex:
        print(ex)
        raise ex

if __name__ == "__main__":
    print(os.getcwd())
    url = 'https://www.npa.go.jp/safetylife/seianki/jisatsu/R02/202009sokuhouti.pdf'
    downloadfile = os.getcwd() + '\\20200924_pdfload\\downloaded.pdf'
    download(url, downloadfile)