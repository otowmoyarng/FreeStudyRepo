from typing import Type, NoReturn

class Words:

    # コンストラクタ
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age

    # 戻り値あり
    def getword(self) -> str:
        return f"私は{self.name}です。{self.age}歳です。"

    # 戻り値なし
    def setword(self, name : str, age : int) -> NoReturn:
        self.name = name
        self.age = age

if __name__ == "__main__":
    words = Words("テスト　太郎", 30)
    print(words.getword())
    words.setword("テスト　はなこ", 23)
    print(words.getword())