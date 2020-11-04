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
sample_dict["class_a"]["student"]['marks'].setdefault("physics", 100)
sample_dict["class_a"]["student_2"]['marks'].setdefault("physics", 100)
sample_dict["class_b"]["student_1"]['marks'].setdefault("physics", 100)
sample_dict["class_b"]["student_2"]['marks'].setdefault("physics", 100)
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
print('Оценка первого = ', ocenka_1 , 'Оценка второго = ', ocenka_2 , 'Оценка третьего ', ocenka_3 , 'Оценка третьего ', ocenka_4)
