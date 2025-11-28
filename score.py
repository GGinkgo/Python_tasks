#查成绩
student_score={
    ("Jack","English"):80,
    ("Jack","Math"):89,
    ("Lucy","English"):88,
    ("Lucy","Math"):85,
    ("John","English"):90,
    ("John","Math"):93
}

target_student=input("Enter student name:")
found=False

for(student,subject),score in student_score.items():
    if target_student==student:
        print(f"student:{student} subject:{subject} score:{score}")
        found=True
    if not found:
        print("Not Found")


