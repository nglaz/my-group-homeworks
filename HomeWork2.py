# import json

sample_dict = {
   "class_a": {
      "student1": {
         "name": "Misha",
         "marks": {
            "math": 90,
            "history": 85
         }
      }
   }
}


print(sample_dict["class_a"]["student1"]["name"], ' - task 1')
print(sample_dict["class_a"]["student1"]["marks"]["history"], ' - task 2')

sample_dict["class_a"]["student2"] = {
         "name": "Petya",
         "marks": {
            "math": 14,
            "history": 88
         }
      }

sample_dict["class_b"] = {
      "student1": {
         "name": "Vasya",
         "marks": {
            "math": 42,
            "history": 21
         }
      }
   }

sample_dict['class_a']['student1']['marks']['physics'] = 15
sample_dict['class_a']['student2']['marks']['physics'] = 67
sample_dict['class_b']['student1']['marks']['physics'] = 77

marks_number = len(sample_dict['class_a']['student1']['marks'])


misha = list(sample_dict['class_a']['student1']['marks'].values())
petya = list(sample_dict['class_a']['student2']['marks'].values())
vasya = list(sample_dict['class_b']['student1']['marks'].values())
misha = round((sum(misha) / marks_number), 2)
petya = round((sum(petya) / marks_number), 2)
vasya = round((sum(vasya) / marks_number), 2)

average_score = {'misha_score': misha, 'petya_score': petya, 'vasya_score': vasya}
average_score_values = list(average_score.values())
average_score_keys = list(average_score.keys())
print(average_score_keys[average_score_values.index(max(average_score_values))], 'task 8')


print(max(average_score))
print((misha, petya, vasya))


average_class_a = (misha + petya) / len(sample_dict["class_a"])
average_class_b = vasya / len(sample_dict['class_b'])
print(average_class_a)
print(average_class_b)

average_classes = {'class_a': average_class_a, 'class_b': average_class_b}
print(max(average_classes), '-----------')

a = list(average_classes.keys())
b = list(average_classes.values())

print(a, b)
print(a[b.index(max(b))])


# print(json.dumps(sample_dict, indent=2))
# 1. Вывести значение ключа "name";
# 2. Вывести значение ключа "history";
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
# 4. Добавить новый класс со студентами;
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
# 6. Подсчитать средний бал по каждому студенту
# (результат округлить до 2 знаков после запятой);
# 7. Создать словарь со средним баллом за каждого студента;
# 8. Определить лучшего студента по успеваемости;
# 9. Подсчитать средний бал по каждому классу
# (результат округлить до 2 знаков после запятой);
# 10. Создать словарь со средним баллом за классы;
# 11. Определить лучший класс по успеваемости.
