from typing import NoReturn

# 戻り値あり
def getword(name : str, age : int) -> str:
    return f"私は{name}です。{age}歳です。"

# 戻り値なし
def outputword1(name : str, age : int):
    print(f"私は{name}です。{age}歳です。")

# 戻り値なし
def outputword2(name : str, age : int) -> None:
    print(f"私は{name}です。{age}歳です。")

# 戻り値なし
def outputword3(name : str, age : int) -> NoReturn:
    print(f"私は{name}です。{age}歳です。")

if __name__ == "__main__":
    print(getword("テスト　太郎", 30))
    outputword1("テスト　はなこ", 23)
    outputword2("テスト　まなこ", 24)
    outputword3("テスト　やまこ", 25)