const SpreadSheet = SpreadsheetApp.getActiveSpreadsheet();

const Sheet = {
    Log: SpreadSheet.getSheetByName('log'),
};

class SheetAccessor {

    GetLogs() {
        const logs = Sheet.Log.getDataRange().getValues();
        logs.shift();
        const list = logs.map(row => {
            return {
                Date: Common.GetCurrentYmd(row[0]),
                Subject: row[1]
            }
        });
        return list;
    }

    GetLog(date) {
        const logs = this.GetLogs();
        return logs.filter(log => log.Date === Common.GetCurrentYmd(date));
    }

    Recent() {
        const logs = this.GetLogs();
        if (logs && logs.length > 0) {
            return logs[logs.length - 1];
        } else {
            return undefined;
        }
    }

    Send(date, subject, url) {
        Sheet.Log.appendRow([date ? date : Common.GetCurrentYmd(), subject, url]);
    }
}

const sheetAccessor = new SheetAccessor();