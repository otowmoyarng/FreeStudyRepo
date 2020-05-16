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
        "DEBUG" : 'False', # DEBUG
        "ALLOWED_HOSTS" : '127.0.0.1',   # ALLOWED_HOSTS
        "DATABASES_ENGINE" : 'django.db.backends.mysql', # MySQL Driver
        "DATABASES_NAME" : 'database', # MySQL DatabaseName
        "DATABASES_USER" : 'user', # MySQL Username
        "DATABASES_PASSWORD" : 'password', # MySQL Password
        "DATABASES_HOST" : 'localhost', # MySQL Hostname
        "DATABASES_PORT" : '3300', # MySQL Portno
    }

    def setUp(self) -> None:
        """
        setUp:テスト実行前メソッド
        環境変数に期待値をセットする

        Returns:
            Not Returns
        """

        # 呼び出し元で環境変数UNITTESTが存在する場合は以降の処理を実行しない
        print("＜投入値＞")
        for key, value in self.envstub.items():
            os.environ[key] = value
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
            param = str(env.GetParams(key)) if key == "DEBUG" else env.GetParams(key)
            self.assertEqual(param, value)
            print(f"key:{key}, value:{param}")
    
if __name__ == "__main__":
    unittest.main()