@ECHO OFF

REM ���s���o�b�`�t�@�C�����J�����g�f�B���N�g���Ƃ���
CD %~dp0

ECHO CSV�t�@�C�����w�肵�Ă��������B
SET /P CSVFILE="CSV�t�@�C���F"

REM CSV�ϊ�����
python main.py %CSVFILE%

REM �ϊ�����html�t�@�C�����J��
start csvconverted.html

pause