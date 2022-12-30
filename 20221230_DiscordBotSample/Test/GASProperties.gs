function allProperty() {
    PropertiesService.getScriptProperties().getKeys().forEach(key => {
        console.log(`key:${key},value:${PropertiesService.getScriptProperties().getProperty(key)}`);
    });
}