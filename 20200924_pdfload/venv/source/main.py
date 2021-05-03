from datetime import datetime
from dateutil.relativedelta import relativedelta
from Downloader import download
import freezegun

datafile: str = None


def main():
    """[summary]
    データファイルをダウンロードファイルする
    """
    global datafile
    datafile, candl = download()

    if candl:
        return

    datafile, candl = download(addmonth=1)


if __name__ == "__main__":
    main()
