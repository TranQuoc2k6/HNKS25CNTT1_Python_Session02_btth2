student_age = int(input("Nhập vào số tuổi của học sinh: "))
average_score = float(input("Nhập điểm trung bình của học sinh: "))

is_eligible = True
is_passed = True
is_benchmark = True

if student_age >= 18:
    is_eligible = True
else:
    is_eligible = False

if average_score >= 4:
    is_passed = True
else:
    is_passed = False

if average_score >= 7:
    is_benchmark = True
else:
    is_benchmark = False

print("--- THÔNG TIN SINH VIÊN ---")
print(f"Tuổi học sinh: {student_age}")
print(f"Điểm trung bình: {average_score}")
print(f"Đủ tuổi đi thi: {is_eligible}")
print(f"Qua môn: {is_passed}")
print(f"Điểm lớn hơn điểm chuẩn: {is_benchmark}")
