class Person:

    # インスタンス初期化メソッド＝コンストラクタ
    def __init__(self, name):
        self.name = name
    
    # インスタンスメソッド
    def getname(self):
        return self.name
    
    # インスタンスメソッド
    def setname(self,name):
        self.name = name
