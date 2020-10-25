import functools

from flask import Flask

app = Flask(__name__)

# 1. ↓をタイプ（pylance「なし」から）
# 2. docstringの確認
# @app.route('/')
def func():
    pass

def hoge(s: str, i: int, l: List[str]) -> None:
    """hoge 関数です"""
    # 3. Listをインポート（ctrl + .）
    # 4. sysをインポート（sys.exit()）
    # 5. randomをインポート
    # 6. randomの候補（Intellicode）
    pass

hoge('a', 1, 1)

# 7. 型のエラー
hoge('1', 2, 3)


# 8. 警告出してくれる
# 9. 型を自分で設定すると補完してくれる
a: str = huga()
