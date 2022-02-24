const SpreadSheet = SpreadsheetApp.getActiveSpreadsheet();

const Sheet = {
    Log: SpreadSheet.getSheetByName('log'),
};

class SheetAccessor {

    GetLogs() {
        const logs = Sheet.Log.getDataRange().getValues();
        logs.shift();
        return logs;
    }

    GetLog(date) {
        const logs = this.GetLogs();
        return logs.filter(log => log[0] === Common.GetCurrentYmd(date));
    }

    Recent() {
        const logs = this.GetLogs();
        if (logs && logs.length > 0) {
            return logs[logs.length - 1];
        } else {
            return undefined;
        }
    }

    Send(subject, date) {
        Sheet.Log.appendRow([Common.GetCurrentYmd(date), subject]);
    }
}

const sheetAccessor = new SheetAccessor();