function Main() {
    const lastSend = sheetAccessor.Recent();
    let targetDate = new Date();
    if (lastSend) {
        let dateSplit = lastSend[0].split("/");
        targetDate = new Date(dateSplit[0], dateSplit[1] - 1, dateSplit[2]);
        targetDate.setDate(targetDate.getDate() + 1);
    }
    const query = `from:コストコ会員限定メールマガジン after:${Common.GetCurrentYmd(targetDate)}`;
    const threads = GmailApp.search(query);
    threads.forEach(thread => {
        const gmails = thread.getMessages();
        gmails.forEach(gmail => {
            const bodylist = gmail.getPlainBody().split('\r\n');
            // ３行目と４行目の条件が一致したらリンクを送信する
            const findIndex = bodylist.indexOf('画像付ﾒﾙﾏｶﾞはこちらでご覧いただけます。');
            if (findIndex === 2) {
                const sliced = bodylist.slice(findIndex, findIndex + 1);
                const url = sliced[sliced.length - 1].replace(' (PC専用ｻｲﾄ)', '');
                SendNotify(["メールマガジンが届きました。", url]);

                sheetAccessor.Send(gmail.getSubject());
            }
        });
    });
}