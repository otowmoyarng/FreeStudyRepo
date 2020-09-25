import requests
import shutil

def download(url : str):
    """[summary]
    指定したurlからファイルをダウンロードする
    Args:
        url ([str]): ダウンロード先url
    Returns:
        ダウンロードしたファイル
    """
    if url is None:
        print('URLが指定されていない')
    else:
        try:
            r = requests.get(url, stream=True)
            with open('./20200924_pdfload/downloaded.pdf', mode='wb') as dfile:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, dfile)
        except requests.exceptions.RequestException as ex:
            print(ex)
            raise ex

if __name__ == "__main__":
    download('https://www.npa.go.jp/safetylife/seianki/jisatsu/R02/202009sokuhouti.pdf')