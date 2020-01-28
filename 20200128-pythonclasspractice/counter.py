class Counter:

    # クラス変数
    counter = 0

    def __init__(self):
        pass

    # クラスメソッド
    def countup(cls):
        cls.counter += 1
        print("現在のカウンター：" + str(cls.counter))
    
    # クラスメソッド
    def getcounter(cls):
        return cls.counter