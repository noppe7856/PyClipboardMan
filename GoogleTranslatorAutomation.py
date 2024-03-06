import pyperclip
import webbrowser

def translate_clipboard():
    # クリップボードからテキストを取得
    text = pyperclip.paste()
    if not text:
        return  # クリップボードが空の場合は何もしない

    # Google翻訳のURLを構築
    base_url = "https://translate.google.com/?sl=en&tl=ja&text="
    encoded_text = text.replace(" ", "%20")  # スペースをURLエンコード
    url = base_url + encoded_text

    # ブラウザでGoogle翻訳のページを開く
    webbrowser.open(url)

if __name__ == '__main__':
    translate_clipboard()
