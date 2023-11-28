const ACCESS_TOKEN = properties.getProperty("ACCESS_TOKEN");

function reply_send(message, reply_token) {
  let url = "https://api.line.me/v2/bot/message/reply";
  const res = UrlFetchApp.fetch(url, {
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
      Authorization: "Bearer " + ACCESS_TOKEN,
    },
    method: "post",
    payload: JSON.stringify({
      replyToken: reply_token,
      messages: [
        {
          type: "text",
          text: message,
        },
      ],
    }),
    muteHttpExceptions: true,
  });
  return res.getResponseCode();
}

function pushMessage_send(to, message) {
  let url = "https://api.line.me/v2/bot/message/push";
  let headers = {
    "Content-Type": "application/json; charset=UTF-8",
    Authorization: "Bearer " + ACCESS_TOKEN,
  };
  let postData = {
    to: to,
    messages: [
      {
        type: "text",
        text: message,
      },
    ],
  };
  let options = {
    method: "post",
    headers: headers,
    payload: JSON.stringify(postData),
  };
  return UrlFetchApp.fetch(url, options);
}

function broadcastMessage_send(message) {
  let url = "https://api.line.me/v2/bot/message/broadcast";
  let headers = {
    "Content-Type": "application/json; charset=UTF-8",
    Authorization: "Bearer " + ACCESS_TOKEN,
  };
  let postData = {
    messages: [
      {
        type: "text",
        text: message,
      },
    ],
    notificationDisabled: false,
  };
  let options = {
    method: "post",
    headers: headers,
    payload: JSON.stringify(postData),
  };
  return UrlFetchApp.fetch(url, options);
}

function get_profile(userId) {
  const url = `https://api.line.me/v2/bot/profile/${userId}`;
  var options = {
    method: "GET",
    headers: { Authorization: `Bearer ${ACCESS_TOKEN}` },
  };
  const response_json = JSON.parse(UrlFetchApp.fetch(url, options));
  return response_json;
}
