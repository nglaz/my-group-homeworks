sample_dict = {
    "class_a": {
        "student": {
            "name": "Misha",
            "marks": {
                "math": 90,
                "history": 85
            }
        }
    }
}

print(sample_dict['class_a']['student']['name'])

print(sample_dict['class_a']['student']['marks']['history'])

student_2 = {
    'student_2': {
        'name': 'Kolya',
        'marks': {
            'math': 91,
            'history': 86
        }
    }
}
sample_dict['class_a'].update(student_2)

class_b = {
    'class_b': {
        'student_3': {
            'name': 'Vasya',
            'marks': {
                'math': 89,
                'history': 84}},
        'student_4': {
            'name': 'Petya',
            'marks': {
                'math': 92,
                'history': 87
            }
        }
    }
}
sample_dict.update(class_b)

sample_dict['class_a']['student']['marks']['physics'] = 81
sample_dict['class_a']['student_2']['marks']['physics'] = 82
sample_dict['class_b']['student_3']['marks']['physics'] = 83
sample_dict['class_b']['student_4']['marks']['physics'] = 84

avg_mark_1 = round(sum(list(sample_dict['class_a']['student']['marks'].values())) \
             / len(sample_dict['class_a']['student']['marks']), 2)
print(avg_mark_1)
avg_mark_2 = round(sum(list(sample_dict['class_a']['student_2']['marks'].values())) \
             / len(sample_dict['class_a']['student_2']['marks']), 2)
print(avg_mark_2)
avg_mark_3 = round(sum(list(sample_dict['class_b']['student_3']['marks'].values())) \
             / len(sample_dict['class_b']['student_3']['marks']), 2)
print(avg_mark_3)
avg_mark_4 = round(sum(list(sample_dict['class_b']['student_4']['marks'].values())) \
             / len(sample_dict['class_b']['student_4']['marks']), 2)
print(avg_mark_4)
# Изначально вариант нахождения среднего балла для каждого ученика был следующий:
# avg_mark_1 = round((sample_dict['class_a']['student']['marks']['physics'] +
# sample_dict['class_a']['student']['marks']['math'] +
# sample_dict['class_a']['student']['marks']['history']) / 3, 2)
# Какой вариант будет предпочтительнее?

avg_marks = {'Misha': avg_mark_1, 'Kolya': avg_mark_2, 'Vasya': avg_mark_3,
             'Petya': avg_mark_4}

for key, value in avg_marks.items():
    if value == max(avg_marks.values()):
        print('The best student is ' + key + '.')
# Попросту говоря, не нашел как это решить без итерации по словарю

avg_class_a_mark = round(sum(list(sample_dict['class_a']['student']['marks'].values())) \
    + sum(list(sample_dict['class_a']['student_2']['marks'].values())) \
    / len(sample_dict['class_a']['student']['marks']) \
    + len(sample_dict['class_a']['student_2']['marks']), 2)
avg_class_b_mark = round(sum(list(sample_dict['class_b']['student_3']['marks'].values())) \
    + sum(list(sample_dict['class_b']['student_4']['marks'].values())) \
    / len(sample_dict['class_b']['student_3']['marks']) \
    + len(sample_dict['class_b']['student_4']['marks']), 2)

avg_class_mark = {'class_a': avg_class_a_mark, 'class_b': avg_class_b_mark}

for key, value in avg_class_mark.items():
    if value == max(avg_class_mark.values()):
        print('The best class is ' + key + '.')