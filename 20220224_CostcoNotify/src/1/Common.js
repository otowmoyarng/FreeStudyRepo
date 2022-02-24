class Common {

    /**
     * 現在日付をyyyy/MM/dd形式で取得する
     * @param date 日付
     * @returns 日付文字列
     */
    static GetCurrentYmd(date) {
        return Utilities.formatDate((date ? date : new Date()), 'Asia/Tokyo', 'yyyy/MM/dd');
    }
}