@ECHO OFF

ECHO �������l��
REM �ݒ�t�@�C���̓ǂݍ���
FOR /F "usebackq delims== tokens=1,2" %%i IN ("setting.ini") do (
    SET %%i=%%j
    SET %%i
)

ECHO:
ECHO ���擾�l��
python EnvironWrapper.py