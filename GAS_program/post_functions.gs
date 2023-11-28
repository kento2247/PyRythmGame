function post_message_function(userID, message) {
  const key = "onetime_login";
  const now_pin = properties.getProperty(key); //取得
  var reply_message = "";
  if (message === "ログアウト") {
    if (now_pin === userID) {
      properties.deleteProperty(key); //削除
      reply_message = "ログアウトしました";
    } else {
      reply_message = "ログアウトに失敗しました\nログインされていません";
    }
  } else {
    if (now_pin === message) {
      properties.setProperty(key, userID); //保存
      reply_message = "ログインしました";
    } else {
      reply_message = "ログインに失敗しました\nPINコードが違います";
    }
  }
  return reply_message;
}
