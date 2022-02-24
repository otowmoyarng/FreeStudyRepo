const url = "https://notify-api.line.me/api/notify"

/**
 * LINENotifyへメッセージ送信する
 * @param {*} messageList 送信メッセージ
 */
function SendNotify(messageList) {

    let message = "";
    messageList.forEach(item => {
        message += `\n${item}`
    });

    const token = GASProperties.GetProperty(GASPropertiesKey.AccessToken);
    let options = {
        "method": "post",
        "headers": {
            "Authorization": "Bearer " + token
        },
        "payload": {
            "message": message
        }
    }
    UrlFetchApp.fetch(url, options)
}