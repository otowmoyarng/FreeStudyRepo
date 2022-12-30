function abnormality() {
  const messages = [undefined, null, ""];
  messages.forEach(message => {
    console.log(`mention:${message}, result:${CreateMessageBody(message)}`);
  });
}

function single() {
  const messages = "message1";
  console.log(`mention:${messages}, result:${CreateMessageBody(messages)}`);
}

function multiple() {
  const messages = ["message1", "message2", "message0"];
  console.log(`mention:${messages}, result:${CreateMessageBody(messages)}`);
}
