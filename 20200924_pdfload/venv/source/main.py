from datetime import datetime
from dateutil.relativedelta import relativedelta
from Downloader import download
import freezegun


def main():
    """[summary]
    データファイルをダウンロードファイルする
    """
    datafile, candl = download()

    if candl:
        return

    download(addmonth=1)


if __name__ == "__main__":
    main()
