function SheetAccessorTest_GetLogs() {
    console.log("GetLogs:", sheetAccessor.GetLogs());
}

function SheetAccessorTest_GetLog() {
    const params = [new Date(2022, 1, 17), new Date(2022, 1, 18)];
    params.forEach(param => {
        console.log(`param:${Common.GetCurrentYmd(param)}, GetLogs:`, sheetAccessor.GetLog(param));
    });
}

function SheetAccessorTest_Recent() {
    console.log("Recent:", sheetAccessor.Recent());
}

function SheetAccessorTest_Send() {
    const url = "https://www.google.com";
    sheetAccessor.Send(new Date(2022, 1, 23), "テスト件名", url);
    console.log("更新結果:", sheetAccessor.GetLogs());
}