const sheetId = properties.getProperty("sheetId");
const LINE_log_sheet = SpreadsheetApp.openById(sheetId).getSheetByName("LINE_log");
const raspi_log_sheet = SpreadsheetApp.openById(sheetId).getSheetByName("raspi_log");

function LINE_log_save(userID, logString, options) {
  const newRow = LINE_log_sheet.getLastRow() + 1;  // 次の行に入力する
  const userName = get_profile(userID).displayName;
  const logData = [new Date(), userID, userName, logString, options];
  const newRange = LINE_log_sheet.getRange(newRow, 1, 1, logData.length);
  newRange.setValues([logData]);
  return newRow;
}

function raspi_log_save(time, message) {
  const newRow = raspi_log_sheet.getLastRow() + 1;  // 次の行に入力する
  const logData = [new Date(), time, message];
  const newRange = raspi_log_sheet.getRange(newRow, 1, 1, logData.length);
  newRange.setValues([logData]);
  return newRow;
}

function debug() {
  // LINE_log_save("Uaedb10ed004057a7f73606b62ecfc6f7", "logString", "options")
  // console.log(properties.getProperty("onetime_login"));            //取得
  // properties.deleteProperty("onetime_login");         //削除
}