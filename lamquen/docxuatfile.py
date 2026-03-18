# --- PHẦN 1: ĐỌC FILE (IN) ---
# 'r' nghĩa là Read (Đọc)
with open('d:/code/file/input.txt', 'r', encoding='utf-8') as f_in:
    content = f_in.read()  # Đọc toàn bộ nội dung file
    print("Nội dung vừa đọc được là:")
    print(content)

# --- PHẦN 2: GHI FILE (OUT) ---
# 'w' nghĩa là Write (Ghi đè). Nếu file chưa có, Python sẽ tự tạo mới.
with open('d:/code/file/output.txt', 'w', encoding='utf-8') as f_out:
    f_out.write("Đây là nội dung được ghi từ Python.\n")
    f_out.write("Kết quả bài tập của bạn đã được lưu!")

print("\nĐã ghi file thành công vào output.txt")