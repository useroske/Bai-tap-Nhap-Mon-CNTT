import random

so_bi_mat = random.randint(1, 10)
so_lan_doan = 0

print("=== Đoán số bí mật ===")

while True:
    try:
        doan = int(input("Chọn một số từ 1 đến 10: "))
    except ValueError:
        print("Không hợp lệ, vui lòng nhập số nguyên!")
        continue

    if doan < 1 or doan > 10:
        print("Vui lòng nhập số từ 1 đến 10!")
        continue

    so_lan_doan += 1

    if doan == so_bi_mat:
        print("Bingo! Bạn đã chiến thắng!")
        print("Số lần đoán:", so_lan_doan)
        break
    elif doan != so_bi_mat:
        print("Chưa chính xác! Hãy thử lại.")
