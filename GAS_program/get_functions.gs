function get_function(e) {
  var return_message = "";
  if (e.parameter == undefined) {
    return_message="failed"
  }
  const app = e.parameter.app
  if (app === "line_send") {
    const to = e.parameter.to;
    const message = e.parameter.message;
    const result = pushMessage_send(to, message);
    const saved_row = LINE_log_save(to, message, "push");
    return_message=`saved in row${saved_row}`
  }
  else if (app === "raspi_log") {
    const time = e.parameter.time;
    const message = e.parameter.message;
    const saved_row = raspi_log_save(time, message);
    return_message=`saved in row${saved_row}`
  }
  else if (app === "control_propaty") {
    const command = e.parameter.command;
    const key = e.parameter.key;
    const value = e.parameter.value;
    if (command === "set") {
      properties.setProperty(key, value);   //保存
      return_message = value;
    }
    else if (command === "get") {
      return_message = properties.getProperty(key);            //取得
      if(return_message.length > 6){
        return_message+=`, ${get_profile(return_message).displayName}`;
      }
    }
    else if (command === "del") {
      return_message = properties.getProperty(key);            //取得
      const userID = return_message;
      pushMessage_send(userID, "ログアウトしました");
      LINE_log_save(userID, "ログアウトしました", "push");
      properties.deleteProperty(key);         //削除
    }
    else {
      return_message=`${app}.command undefined`;
    }
  }
  return return_message;
}
