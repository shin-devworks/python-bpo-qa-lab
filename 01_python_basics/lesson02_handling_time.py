# 問い合わせ対応時間チェックプログラム

reception_id = 1002
category = "契約内容"
handling_time = 12

print("受付番号：", reception_id)
print("問い合わせ種別：", category)
print("対応時間：", handling_time, "分")

if handling_time > 10:
    print("判定：要確認")
elif handling_time > 5:
    print("判定：通常")
else:
    print("判定：良好")
