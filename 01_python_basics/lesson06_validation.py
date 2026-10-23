# Lesson 06：入力値検証＋例外処理

response_times = [12, 18, "不明", -5, 25, "", 300, 15]

valid_times = []
invalid_times = []

for time in response_times:
    try:
        # 数値に変換する
        time = float(time)

        # 正常範囲を確認する
        if 0 <= time <= 120:
            valid_times.append(time)
        else:
            invalid_times.append(time)

    except (ValueError, TypeError):
        # 数値に変換できないデータ
        invalid_times.append(time)

print("正常データ:", valid_times)
print("異常データ:", invalid_times)

print("正常件数:", len(valid_times))
print("異常件数:", len(invalid_times))

# 正常データの平均を計算
if len(valid_times) > 0:
    average = sum(valid_times) / len(valid_times)
    print(f"平均対応時間：{average:.1f}分")
else:
    print("正常データがありません")

# 異常率を計算
total_count = len(response_times)

if total_count > 0:
    invalid_rate = len(invalid_times) / total_count * 100
    print(f"異常率：{invalid_rate:.1f}%")
else:
    print("集計対象データがありません")
