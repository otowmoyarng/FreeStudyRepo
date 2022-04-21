function TestGetCurrentYmd() {
    console.log(`dateなし:${Common.GetCurrentYmd()}`);
    const testdate = new Date();
    testdate.setDate(testdate.getDate() - 1);
    console.log(`dateあり:${Common.GetCurrentYmd(testdate)}`);
}