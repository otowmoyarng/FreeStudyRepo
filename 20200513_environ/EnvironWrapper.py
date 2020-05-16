import os

class EnvironWrapper:
    """ 
    class:EnvironWrapper

    概要:環境変数から読み込んだ起動パラメータを保持するクラス
    """

    # 環境変数
    defaultenv_context = {
        "SECRET_KEY" : 'naishokey', # SECRET_KEY
        "DEBUG_FLG" : 'true', # DEBUG_FLG
        "ALLOWED_HOSTS" : None,   # ALLOWED_HOSTS
        "DATABASES_ENGINE" : 'django.db.backends.mysql', # MySQL Driver
        "DATABASES_NAME" : 'database', # MySQL DatabaseName
        "DATABASES_USER" : 'user', # MySQL Username
        "DATABASES_PASSWORD" : 'password', # MySQL Password
        "DATABASES_HOST" : 'localhost', # MySQL Hostname
        "DATABASES_PORT" : '3300', # MySQL Portno
    }
    # 環境変数
    getenv_context = {}

    def __init__(self):
        """
        コンストラクタ
        os.environから環境変数を読み取る
        """
        for key, value in self.defaultenv_context.items():
            param = os.getenv(key, default=value)
            if key == "DEBUG_FLG" :
                param = False if param.lower().startswith('false') else True
            self.getenv_context[key] = param

    def GetParams(self, key : str) -> object:
        """
        GetParams:環境変数取得処理

        Arguments:
            key {str} -- 環境変数キー

        Returns:
            object -- 環境変数値
        """
        return self.getenv_context[key]

if __name__ == "__main__":
    env = EnvironWrapper()

    for key, value in env.getenv_context.items():
        print(f"key:{key}, value:{value}")