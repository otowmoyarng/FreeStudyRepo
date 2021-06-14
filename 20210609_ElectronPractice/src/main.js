// アプリケーション定義
const { app, BrowserWindow } = require('electron');

let mainwindow;

function createWindow() {
    // BrowserWindowのインスタンスを生成する
    mainwindow = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
        },
        width: 800,
        height: 600
    });

    // htmlファイルを読み込み
    mainwindow.loadFile('index.html');

    // デベロッパーツールの起動
    mainwindow.webContents.openDevTools();

    // 画面が閉じたときの処理
    mainwindow.on('closed', () => {
        mainwindow = null;
    });
}

// 初期化完了時
app.on('ready', createWindow);

// 全てのウィンドウが閉じた時
app.on('window-all-closed', () => {
    // appを終了する
    app.quit();
});

// アクティブの時
app.on('activate', () => {
    // mainwindowが閉じていれば画面を生成する
    if (mainwindow == null) {
        createWindow();
    }
});