# 問い合わせ対応データ
inquiries = [
    {"id": "001", "category": "契約", "duration": 8},
    {"id": "002", "category": "故障", "duration": 15},
    {"id": "003", "category": "操作案内", "duration": 25},
    {"id": "004", "category": "契約", "duration": 12},
    {"id": "005", "category": "故障", "duration": 20},
    {"id": "006", "category": "操作案内", "duration": 18},
]

# 基準対応時間
standard_time = 15

# 集計用の変数
total_time = 0
over_count = 0

# 各問い合わせを順番に処理
for inquiry in inquiries:
    duration = inquiry["duration"]
    category = inquiry["category"]

    total_time += duration

    if duration > standard_time:
        over_count += 1
        print(f"基準超過：{category}（{duration}分）")

# 集計結果
total_count = len(inquiries)
average_time = total_time / total_count

print("----- 集計結果 -----")
print(f"問い合わせ件数：{total_count}件")
print(f"総対応時間：{total_time}分")
print(f"平均対応時間：{average_time:.1f}分")
print(f"基準超過件数：{over_count}件")
