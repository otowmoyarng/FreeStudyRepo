function SendMessage(targets, messages) {

  // 投稿するチャット内容と設定
  let content = CreateMensions(targets);
  if (content !== "") {
    content += "\n";
  }
  content += CreateMessageBody(messages);
  const message = {
    "content": content, // チャット本文
    "tts": false  // ロボットによる読み上げ機能を無効化
  }

  const param = {
    "method": "POST",
    "headers": { 'Content-type': "application/json" },
    "payload": JSON.stringify(message),
    'muteHttpExceptions': true,
  }

  // discord側で作成したボットのウェブフックURL
  const discordWebHookURL = GASProperties.GetProperty(GASPropertiesKey.WebHookURL);
  UrlFetchApp.fetch(discordWebHookURL, param);
}

function CreateMensions(targets) {
  if (!targets) {
    return "";
  }

  if (!Array.isArray(targets)) {
    targets = [targets];
  }
  let mentions = "";
  targets.forEach(target => {
      if (mentions !== "") {
          mentions += " ";
      }
      if (target === "everyone" || target === "here") {
        mentions += `@${target}`;
      } else {
        mentions += `<@${target}>`;
      }
  });
  return mentions;
}

function CreateMessageBody(messages) {
  if (!messages) {
    return "";
  }

  if (!Array.isArray(messages)) {
    messages = [messages];
  }
  let message = "";
  messages.forEach(msg => {
      if (message !== "") {
          message += "\n";
      }
      message += msg;
  });
  return message;
}