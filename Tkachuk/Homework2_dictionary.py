import operator
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

sample_dict['class_a']['student2'] = {}
sample_dict['class_a']['student2'].update({'name': 'Victor'})
sample_dict['class_a']['student2'].update(
   {"marks": {"math": 68, "history": 59}}
)
sample_dict['class_a']['student3'] = {}
sample_dict['class_a']['student3'].update({'name': 'Igor'})
sample_dict['class_a']['student3'].update(
   {"marks": {'math': 98, 'history': 92}}
)
sample_dict['class_b'] = {}
sample_dict['class_b']['student'] = {}
sample_dict['class_b']['student'].update({'name': 'Max'})
sample_dict['class_b']['student'].update(
   {"marks": {'math': 75, 'history': 98}}
)
sample_dict['class_b']['student2'] = {}
sample_dict['class_b']['student2'].update({'name': 'Roman'})
sample_dict['class_b']['student2'].update(
   {'marks': {'math': 45, 'history': 65}}
)
sample_dict['class_b']['student3'] = {}
sample_dict['class_b']['student3'].update({'name': 'Bogdan'})
sample_dict['class_b']['student3'].update(
   {'marks': {'math': 63, 'history': 70}}
)
print(sample_dict)

sample_dict['class_a']['student']['marks'].update({'physics': 80})
sample_dict['class_a']['student2']['marks'].update({'physics': 75})
sample_dict['class_a']['student3']['marks'].update({'physics': 98})
sample_dict['class_b']['student']['marks'].update({'physics': 90})
sample_dict['class_b']['student2']['marks'].update({'physics': 40})
sample_dict['class_b']['student3']['marks'].update({'physics': 59})
print(sample_dict)

arithmetic_mean_marks_of_Misha = round(
    sum((sample_dict['class_a']['student']['marks'].values())) /
    len(sample_dict['class_a']['student']['marks']), 2
)
arithmetic_mean_marks_of_Victor = round(
    sum((sample_dict['class_a']['student2']['marks'].values())) /
    len(sample_dict['class_a']['student2']['marks']), 2
)
arithmetic_mean_marks_of_Igor = round(
    sum((sample_dict['class_a']['student3']['marks'].values())) /
    len(sample_dict['class_a']['student3']['marks']), 2
)
arithmetic_mean_marks_of_Max = round(
    sum((sample_dict['class_b']['student']['marks'].values())) /
    len(sample_dict['class_b']['student']['marks']), 2
)
arithmetic_mean_marks_of_Roman = round(
    sum((sample_dict['class_b']['student2']['marks'].values())) /
    len(sample_dict['class_b']['student2']['marks']), 2
)
arithmetic_mean_marks_of_Bogdan = round(
    sum((sample_dict['class_b']['student3']['marks'].values())) /
    len(sample_dict['class_b']['student3']['marks']), 2
)
arithmetic_mean_marks_of_students = {
    'Misha': arithmetic_mean_marks_of_Misha,
    'Victor': arithmetic_mean_marks_of_Victor,
    'Igor': arithmetic_mean_marks_of_Igor,
    'Max': arithmetic_mean_marks_of_Max,
    'Roman': arithmetic_mean_marks_of_Roman,
    'Bogdan': arithmetic_mean_marks_of_Bogdan
}
print(arithmetic_mean_marks_of_students)

the_best_student = max(
    arithmetic_mean_marks_of_students.items(), key=operator.itemgetter(1))[0]
print('The best student is ' + the_best_student)

arithmetic_mean_marks_of_class_a = round(
    (arithmetic_mean_marks_of_Misha +
     arithmetic_mean_marks_of_Victor +
     arithmetic_mean_marks_of_Igor) / 3, 2
)
print('Arithmetic mean marks of class a is ' +
      str(arithmetic_mean_marks_of_class_a))

arithmetic_mean_marks_of_class_b = round(
    (arithmetic_mean_marks_of_Roman +
     arithmetic_mean_marks_of_Max +
     arithmetic_mean_marks_of_Bogdan) / 3, 2
)
print('Arithmetic mean marks of class b is ' +
      str(arithmetic_mean_marks_of_class_b))

classes_a_and_b = {
    'class A': arithmetic_mean_marks_of_class_a,
    'class B': arithmetic_mean_marks_of_class_b,
}
the_best_class = max(classes_a_and_b.items(), key=operator.itemgetter(1))[0]
print('The best class is ' + the_best_class)
