# Дан словарь такого типа:
sample_dict = {
   "class_a":{
      "student":{
         "name":"Misha",
         "marks":{
            "math":90,
            "history":85
         }
      }
   }
}

# №1
print(sample_dict["class_a"]["student"]["name"])
# №2
print(sample_dict["class_a"]["student"]["marks"]["history"])
# №3
sample_dict["class_a"].setdefault("student_2" , {"name": "Nikita", "marks":
    {"math":100,"history":100}})
print(sample_dict["class_a"])
# №4
sample_dict.setdefault("class_b", {"student_1": {"name": "Ruslan","marks":
    {"math": 100, "history": 100}}})
sample_dict["class_b"].setdefault("student_2", {'name': 'Serjio','marks':
    {'math': 100, 'history': 100}})
print(sample_dict["class_b"])

# №5
sample_dict["class_a"]["student"]['marks'].setdefault("physics", 94)
sample_dict["class_a"]["student_2"]['marks'].setdefault("physics", 89)
sample_dict["class_b"]["student_1"]['marks'].setdefault("physics", 68)
sample_dict["class_b"]["student_2"]['marks'].setdefault("physics", 70)
print(sample_dict["class_a"])
print(sample_dict["class_b"])
# №6
stud_1 = sample_dict['class_a']['student']['name']
stud_2 = sample_dict['class_a']['student_2']['name']
stud_3 = sample_dict['class_b']['student_1']['name']
stud_4 = sample_dict['class_b']['student_2']['name']
ocenka_1 = str(round(sum(sample_dict["class_a"]["student"]['marks'].values())/\
                     len(sample_dict["class_a"]["student"]['marks']), 2))
ocenka_2 = str(round(sum(sample_dict["class_a"]["student_2"]['marks'].values())/\
                     len(sample_dict["class_a"]["student"]['marks']), 2))
ocenka_3 = str(round(sum(sample_dict["class_b"]["student_1"]['marks'].values())/\
                     len(sample_dict["class_b"]["student_1"]['marks']), 2))
ocenka_4 = str(round(sum(sample_dict["class_b"]["student_2"]['marks'].values())/\
                     len(sample_dict["class_b"]["student_2"]['marks']), 2))
print('Оценка первого = ', ocenka_1 , 'Оценка второго = ', ocenka_2 ,
      'Оценка третьего ', ocenka_3 , 'Оценка третьего ', ocenka_4)

# №7
slovar_e_bal = {stud_1:ocenka_1, stud_2:ocenka_2,
                stud_3:ocenka_3, stud_4:ocenka_4}
print(slovar_e_bal)

# 8
best_studeent = dict(zip(slovar_e_bal.values(), slovar_e_bal.keys()))
print(best_studeent[max(best_studeent.keys())]+' - '+max(best_studeent.keys()))

# 9
sred_bal_clas_1= str(round((sum(sample_dict["class_a"]["student"][
                               'marks'].values())\
            +sum(sample_dict["class_a"]["student_2"]['marks'].values()))\
             /len(sample_dict["class_a"]), 2))
sred_bal_clas_2 = str(round((sum(sample_dict["class_b"]["student_1"][
                              'marks'].values())\
            +sum(sample_dict["class_b"]["student_2"]['marks'].values()))\
             /len(sample_dict["class_b"]), 2))
print('Class_a sredniy bal- '+sred_bal_clas_1+'\n'+'Class_b sredniy bal- '
                                              ''+sred_bal_clas_2)

# 10
slovar_e_clas = {'class_a': sred_bal_clas_1, 'class_b': sred_bal_clas_2}
print(slovar_e_clas)

# 11
best_clas = dict(zip(slovar_e_clas.values(), slovar_e_clas.keys()))
print(best_clas[max(best_clas.keys())]+' - '+max(best_clas.keys()))



# 1. Вывести значение ключа "name";
# 2. Вывести значение ключа "history";
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
# 4. Добавить новый класс со студентами;
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
# 7. Создать словарь со средним баллом за каждого студента;
# 8. Определить лучшего студента по успеваемости;
# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
# 10. Определить лучший класс по успеваемости.
# 11. Создать словарь со средним баллом за классы;
