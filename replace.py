import os

# ディレクトリパス
directory_path = 'output_files'

# ディレクトリ内の全てのファイルを処理
for filename in os.listdir(directory_path):
    # ファイルのパスを取得
    file_path = os.path.join(directory_path, filename)

    # テキストファイルのみを処理
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            # ファイルの内容を読み込み、必要な文字を削除
            content = file.read()
            content = content.replace('-', '').replace('_', '').replace(' ', '')

        # 変更を同じファイルに上書き保存
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Processed {filename}")
