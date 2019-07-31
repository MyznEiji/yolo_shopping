from flask import Flask
from application.config import Config
import importlib
import os


def create_app():
    # インスタンスの立ち上げ
    _app = Flask(__name__)
    # Flaskのconfigが 設定ファイルを読み込む処理
    _app.config.from_object(Config)

    return _app


# For external
app = create_app()
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
STATICS_PATH = os.path.join(APP_ROUTE, 'static')

# View, Modelのロード(PEP8対策)
## import application.views  <= 通常のimport文は上に書かないとPEP8違反だが、`views.py`の中で`create_app`された後の`app`オブジェクト
##  を使う必要があるため、遅延インポートを行う。
importlib.import_module("application.views")
