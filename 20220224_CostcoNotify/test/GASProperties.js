/**
 * GASProperties用テスト関数
 */
function TestGetProperty() {
    console.log(`key:${GASPropertiesKey.AccessToken},value:${GASProperties.GetProperty(GASPropertiesKey.AccessToken)}`);
}