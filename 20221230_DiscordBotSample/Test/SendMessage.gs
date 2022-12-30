function Normal() {
  const targets = "";
  const messages = "メンションなしで送信";
  SendMessage(targets, messages);
}

function MensionByUserId() {
  const targets = "1031000015751106591";
  const messages = "単一メンションでTest送信";
  SendMessage(targets, messages);
}

function MensionByUserIds() {
  const targets = ["1031000015751106591", "822975666734760008"];
  const messages = ["複数メンションでTest送信", "２行目"];
  SendMessage(targets, messages);
}

function MensionToAll() {
  const targets = "everyone";
  const messages = `${targets}メンションでTest送信`;
  SendMessage(targets, messages);
}

function MensionToHere() {
  const targets = "here";
  const messages = `${targets}メンションでTest送信`;
  SendMessage(targets, messages);
}
