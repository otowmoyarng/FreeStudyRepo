
# 戻り値あり
def getword(name, age):
    return f"私は{name}です。{age}歳です。"

# 戻り値なし
def outputword(name, age):
    print(f"私は{name}です。{age}歳です。")

if __name__ == "__main__":
    print(getword("テスト　太郎", 30))
    outputword("テスト　花子", 25)