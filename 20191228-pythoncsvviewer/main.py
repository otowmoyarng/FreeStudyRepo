import os
import pandas as pd
import sys

def main():
    # 引数１からCSVファイルを取得する
    args = sys.argv
    csvfile = ''

    # 引数なしはエラーとする
    if 1 == len(args):
        print("CSVファイルが指定されていません。")
        return
    else:
        csvfile = args[1]

        # ファイル名が不正の場合はエラー
        if os.path.exists(csvfile) == False:
            print("指定したファイルは存在しません。")
            return
        
        # CSVファイルではない場合はエラーとする
        if csvfile.endswith(".csv") == False:
            print("ＣＳＶファイル以外が指定されています。")
            return
        
    print("CSVファイルをhtmlに変換します。")

    # CSVファイル読み込み
    csvdata = pd.read_csv(csvfile, na_filter=False)

    # htmlファイル読み込み
    htmldata = ''
    with open('templete.html',mode='r',encoding='utf-8') as htmlfile:
        htmldata = htmlfile.read()

    # CSVファイルをhtmlに変換
    rpdict = { "filename" : os.path.basename(csvfile), "table" : csvdata.to_html() }
    htmldata = htmldata.format(**rpdict)

    # htmlファイル出力
    with open('csvconverted.html',mode='w',encoding='utf-8') as outputhtml:
        outputhtml.write(htmldata)

if __name__== '__main__':
    main()