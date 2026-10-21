# Lesson 05：例外処理
# 問い合わせ対応時間の安全な集計


def calculate_average(times):
    valid_times = []

    for time in times:
        try:
            number = float(time)
            valid_times.append(number)

        except (ValueError, TypeError):
            print(f"無効なデータを検出：{time}")

    try:
        average = sum(valid_times) / len(valid_times)
        return average

    except ZeroDivisionError:
        print("有効なデータが0件のため、平均を計算できません")
        return None


# 問い合わせ対応時間
handling_times = [8, 15, "不明", 25, 12, 20, 18]

# 関数を呼び出す
result = calculate_average(handling_times)

# 結果を表示
if result is not None:
    print(f"平均対応時間：{result:.1f}分")
