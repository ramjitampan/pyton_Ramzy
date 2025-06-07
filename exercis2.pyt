# Jawaban benar (kunci jawaban)
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']


with open('student_answers.txt', 'r') as file:
    student_answers = [line.strip() for line in file.readlines()]  

correct_count = 0
incorrect_questions = []

for i in range(20):
    if student_answers[i] == correct_answers[i]: 
        correct_count += 1
    else:
        incorrect_questions.append(i + 1) 

# Hasil

print("PASS" if correct_count >= 15 else "FAIL")
print("Correct answer :", correct_count)
print("Wrong answer :", 20 - correct_count)
print("Wrong question number :", incorrect_questions)
