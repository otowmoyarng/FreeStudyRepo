scriptId = 
rootDir = 
deployId = 

default:
	C:\Windows\System32\cmd.exe /k "C:\Program Files\nodejs\nodevars.bat"

init:
	@make default
	echo exitと入力する
	npm init -y
	npm install @google/clasp
	npm install google-apps-script
	@make login

login:
	@make default
	echo exitと入力する
	clasp login

switch:
	clasp setting scriptId $(scriptId)
	clasp setting rootDir $(rootDir)

push:
	echo gas push start
	clasp push
	echo gas push finish