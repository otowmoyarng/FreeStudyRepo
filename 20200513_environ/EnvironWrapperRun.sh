#!/bin/bash

# 設定ファイルの読み込み
echo ＜投入値＞
while read line
do
export $line
echo $line
done < setting.ini

echo ＜取得値＞
python3 EnvironWrapper.py