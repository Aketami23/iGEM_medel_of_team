import os
from collections import defaultdict

# ディレクトリパス
directory_path = 'output_files'

# チームのメダル獲得記録を保持する辞書
team_medals = defaultdict(lambda: defaultdict(int))

# ディレクトリが存在するか確認
print("Files in directory:")
for file in os.listdir(directory_path):
    print(file)

# ディレクトリ内のメダルファイルを探索
for filename in os.listdir(directory_path):
    print(f"Found file: {filename}")  # ファイル発見時のデバッグ情報
    if filename.endswith('.txt') and not filename.startswith('.'):
        # Correct the splitting here, it should be based on the period, not underscore
        file_parts = filename.split('.')
        print("file_parts is : ", file_parts)
        name_parts = file_parts[0].split('_')  # Now split the name part on underscore
        if len(name_parts) == 2 and name_parts[1] in ['bronze', 'silver', 'gold']:
            year, medal_type = name_parts[0], name_parts[1]
            print(f"Year: {year}, Medal: {medal_type}")  # 年とメダルタイプのデバッグ情報
            # ...
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                for line_number, team_name in enumerate(file, 1):
                    team_name = team_name.strip()
                    if team_name:
                        print(f"Line {line_number}: '{team_name}'")  # 読み込んだチーム名のデバッグ情報
                        team_medals[team_name][medal_type] += 1
                    else:
                        print(f"Line {line_number}: Empty or whitespace line.")  # 空白行の場合の警告
        else:
            print(f"Skipping file: {filename}")  # メダルファイルではないためスキップ
    else:
        print(f"Skipping file: {filename}")  # メダルファイルではないためスキップ


# 結果の出力とファイルへの保存
print("Medal counts per team:")
with open('medal_counts.txt', 'w', encoding='utf-8') as out_file:
    for team, medals in sorted(team_medals.items()):
        gold_count = medals.get('gold', 0)
        silver_count = medals.get('silver', 0)
        bronze_count = medals.get('bronze', 0)
        print(f"{team}: Gold {gold_count}, Silver {silver_count}, Bronze {bronze_count}")
        out_file.write(f"{team}: Gold {gold_count}, Silver {silver_count}, Bronze {bronze_count}\n")
