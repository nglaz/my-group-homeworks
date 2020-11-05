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
print(sample_dict)
#1
print(sample_dict['class_a']['student']['name'])
#2
print(sample_dict['class_a']['student']['marks']['history'])
#3
sample_dict['class_a'].setdefault('student2', {'name': 'Dima', 'marks': {'math': 60, 'history': 95}})
print(sample_dict)
#4
sample_dict.setdefault('class_b', {'student': {'name': 'Masha', 'marks': {'math': 80, 'history': 90}}})
sample_dict['class_b'].setdefault('student2', {'name': 'Vasya', 'marks': {'math': 60, 'history': 65}})
print(sample_dict)
#5
sample_dict['class_a']['student']['marks'].setdefault('physics', 80)
sample_dict['class_a']['student2']['marks'].setdefault('physics', 65)
sample_dict['class_b']['student']['marks'].setdefault('physics', 85)
sample_dict['class_b']['student2']['marks'].setdefault('physics', 70)
print(sample_dict)
#6
avg_mark1 = (round(sum(sample_dict['class_a']['student']['marks'].values())/(len(sample_dict['class_a']['student']['marks'])), 2))
avg_mark2 = (round(sum(sample_dict['class_a']['student2']['marks'].values())/(len(sample_dict['class_a']['student2']['marks'])), 2))
avg_mark3 = (round(sum(sample_dict['class_b']['student']['marks'].values())/(len(sample_dict['class_b']['student']['marks'])), 2))
avg_mark4 = (round(sum(sample_dict['class_b']['student2']['marks'].values())/(len(sample_dict['class_b']['student2']['marks'])), 2))
print(avg_mark1, avg_mark2, avg_mark3, avg_mark4)
#7
avg_mark = {1: avg_mark1, 2: avg_mark2, 3: avg_mark3, 4: avg_mark4}
print(avg_mark)
#8
