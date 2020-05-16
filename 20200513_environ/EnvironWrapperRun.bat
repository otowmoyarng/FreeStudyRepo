@ECHO OFF

ECHO ＜投入値＞
REM 設定ファイルの読み込み
FOR /F "usebackq delims== tokens=1,2" %%i IN ("setting.ini") do (
    SET %%i=%%j
    SET %%i
)

ECHO:
ECHO ＜取得値＞
python EnvironWrapper.py