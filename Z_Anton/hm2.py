import random
import copy
sample_dict = {'class-_a':{
                'student':{
                    'name':'Misha',
                    'marks':{
                       'math':90,
                       'history':85
                    }
                }
            }
        }
print(sample_dict['class-_a']['student']['name'])
print(sample_dict['class-_a']['student']['marks']['history'])
sample_dict['class-_a']['new_student'] = {'name': 'Vova', 'marks':{
    'math':100, 'history':95
}}
sample_dict['class_b'] = copy.deepcopy(sample_dict['class-_a'])
v = []
v_a = []
sample_dict['class_b']['student']['marks'].update({'physics': 70})
sample_dict['class_b']['new_student']['marks'].update({'physics': 97})
sample_dict['class_b']['student']['name'] = 'Igor'
sample_dict['class_b']['new_student']['name'] = 'Anton'

v.append(list(sample_dict['class_b']['student']['marks'].values()))
v.append(list(sample_dict['class_b']['new_student']['marks'].values()))
v_a.append(list(sample_dict['class-_a']['student']['marks'].values()))
v_a.append(list(sample_dict['class-_a']['new_student']['marks'].values()))
print(sample_dict['class_b'])
print(sample_dict['class-_a'])
print(v, v_a)
f_sum = round(sum(v[0])/len(v[0]), 2)
print(f_sum)
s_sum = round(sum(v[1])/len(v[1]), 2)
print(s_sum)
sum_all_students = {'student_1': f_sum, 'student_2': s_sum}
best_student = list(sum_all_students.keys())[list(sum_all_students.values()).index(max(sum_all_students.values()))]
print(best_student)
new_v = v[0]+v[1]
sum_all_students_in_all_class = round(sum(new_v)/len(new_v), 2)
print(sum_all_students_in_all_class)
new_v_a = v_a[0]+v_a[1]
sum_all_students_in_all_class_a = round(sum(new_v_a)/len(new_v_a), 2)
print(sum_all_students_in_all_class_a)
class_sum = {'class_a': sum_all_students_in_all_class_a, 'class_b': sum_all_students_in_all_class}
value = list(class_sum.values())
key = list(class_sum.keys())
best = key[value.index(max(class_sum.values()))]
print(best)