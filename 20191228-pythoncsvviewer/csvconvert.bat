@ECHO OFF

REM 実行中バッチファイルをカレントディレクトリとする
CD %~dp0

ECHO CSVファイルを指定してください。
SET /P CSVFILE="CSVファイル："

REM CSV変換処理
python main.py %CSVFILE%

REM 変換したhtmlファイルを開く
start csvconverted.html

pause