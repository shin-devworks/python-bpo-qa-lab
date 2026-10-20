# Lesson 04：関数の基礎

# 平均対応時間を計算する関数
def calculate_average(times):
    total = sum(times)
    count = len(times)
    average = total / count
    return average


# 問い合わせ対応時間
handling_times = [8, 15, 25, 12, 20, 18]

# 関数を呼び出す
result = calculate_average(handling_times)

# 結果を表示
print(f"平均対応時間：{result:.1f}分")

# 次の日の問い合わせ対応時間

next_day_times = [5, 10, 15, 10]

# 関数を呼び出す
result = calculate_average(next_day_times)

# 結果を表示
print(f"次の日の平均対応時間：{result:.1f}分")

third_day_times = [6, 9, 12, 13]

result = calculate_average(third_day_times)

print(f"3日目の平均対応時間:{result:.1f}分")
