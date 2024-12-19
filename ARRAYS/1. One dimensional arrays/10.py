###
# Prints test statistics
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Calculates the number of test questions
question_number = len(test_results)

# Calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

# Calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers

# Calculates the percentage of correct answers
percentage_correct = (correct_answers / question_number) * 100

# Prints the results
print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', f'{percentage_correct:.2f}%')
