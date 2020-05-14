from EnvironWrapper import EnvironWrapper
import os
import unittest

class EnvironWrapperTest(unittest.TestCase):
    """
    EnvironWrapperTestクラス
    EnvironWrapperクラスのテストスイート
    """
    
    # テスト用環境変数定義
    envstub = {
        "DEBUG" : False, # DEBUG
        "ALLOWED_HOSTS" : "127.0.0.1",   # ALLOWED_HOSTS
    }

    def setUp(self) -> None:
        """
        setUp:テスト実行前メソッド
        環境変数に期待値をセットする

        Returns:
            Not Returns
        """
        
        print("＜投入値＞")
        for key, value in self.envstub.items():
            os.environ[key] = str(value)
            print(f"key:{key}, value:{value}")
    
    def testload(self) -> None:
        """
        testload:環境変数取得の取得テスト

        Returns:
            Not Returns
        """

        print("＜取得値＞")
        env = EnvironWrapper()
        
        for key, value in self.envstub.items():
            self.assertEqual(env.GetParams(key), value)
            print(f"key:{key}, value:{value}")
    
if __name__ == "__main__":
    unittest.main()