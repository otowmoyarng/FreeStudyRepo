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
    sheetAccessor.Send("テスト件名");
    sheetAccessor.Send("テスト件名", new Date(2022, 1, 23));
    console.log("更新結果:", sheetAccessor.GetLogs());
}