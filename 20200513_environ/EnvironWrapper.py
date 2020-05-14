import os

class EnvironWrapper:
    """ 
    class:EnvironWrapper

    概要:環境変数から読み込んだ起動パラメータを保持するクラス
    """

    # 環境変数
    defaultenv_context = {
        "DEBUG" : True, # DEBUG
        "ALLOWED_HOSTS" : None,   # ALLOWED_HOSTS
    }
    # 環境変数
    getenv_context = {}

    def __init__(self):
        """
        コンストラクタ
        os.environから環境変数を読み取る
        """
        for key, value in self.defaultenv_context.items():
            env_value = os.getenv(key, default=value)
            if key == "DEBUG" :
                env_value = env_value == "True"
            self.getenv_context[key] = env_value

    def GetParams(self, key : str) -> object:
        """
        GetParams:環境変数取得処理

        Arguments:
            key {str} -- 環境変数キー

        Returns:
            object -- 環境変数値
        """
        return self.getenv_context[key]