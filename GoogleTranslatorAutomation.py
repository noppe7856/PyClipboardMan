import pyperclip
import webbrowser
import re

def remove_unnecessary_newlines(text):
    # 改行をスペースに置換
    text = text.replace('\n', ' ')
    # 連続するスペースを1つのスペースに置換
    text = re.sub(r'\s+', ' ', text)
    return text

def split_sentences(text):
    # 不要な改行を削除
    text = remove_unnecessary_newlines(text)
    # 文に分割
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

def translate_clipboard():
    # クリップボードからテキストを取得
    text = pyperclip.paste()
    if not text:
        return  # クリップボードが空の場合は何もしない

    # reモジュールを使用して文分割処理
    sentences = split_sentences(text)
    joined_text = '\n'.join(sentences)  # 分割された文を改行で結合

    # Google翻訳のURLを構築
    base_url = "https://translate.google.com/?sl=en&tl=ja&text="
    encoded_text = joined_text.replace(" ", "%20").replace("\n", "%0A")  # スペースと改行をURLエンコード
    url = base_url + encoded_text

    # ブラウザでGoogle翻訳のページを開く
    webbrowser.open(url)

if __name__ == '__main__':
    translate_clipboard()
