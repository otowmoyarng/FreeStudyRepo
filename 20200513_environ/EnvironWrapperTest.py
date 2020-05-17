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
        "SECRET_KEY" : 'zettaihimitsunisitene', # SECRET_KEY
        "DEBUG_FLG" : False, # DEBUG_FLG
        "ALLOWED_HOSTS" : '127.0.0.1#localhost',   # ALLOWED_HOSTS
        "DATABASES_ENGINE" : 'django.db.backends.mysql', # MySQL Driver
        "DATABASES_NAME" : 'database', # MySQL DatabaseName
        "DATABASES_USER" : 'user', # MySQL Username
        "DATABASES_PASSWORD" : 'password', # MySQL Password
        "DATABASES_HOST" : 'localhost', # MySQL Hostname
        "DATABASES_PORT" : '3300', # MySQL Portno
    }
    # ALLOWED_HOSTS区切り文字
    sprit_word = '#'

    def setUp(self) -> None:
        """
        setUp:テスト実行前メソッド
        環境変数に期待値をセットする

        Returns:
            Not Returns
        """

        print("＜投入値＞")
        for key, value in self.envstub.items():
            os.environ[key] = str(value) if key == "DEBUG_FLG" else value
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
            expect = value
            param = env.GetParams(key)
            if key == "ALLOWED_HOSTS" :
                expect = expect.split(self.sprit_word) if self.sprit_word in expect else [expect]
            self.assertEqual(param, expect)
            print(f"key:{key}, value:{param}")
    
if __name__ == "__main__":
    unittest.main()