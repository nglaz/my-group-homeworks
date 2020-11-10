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
print(sample_dict["class_a"]["student"]["name"])
print(sample_dict["class_a"]["student"]["marks"]["history"])
sample_dict["class_a"]["student2"]= {"name":"Alex",
         "marks":{
            "math":95,
            "history":80
         }
      }
print(sample_dict)
sample_dict2 = {'class_b': {'student': {'name': 'Grisha', 'marks':
    {'math': 35, 'history': 56}}, 'student2':
    {'name': 'FAlex', 'marks': {'math': 99, 'history': 98}}}}
sample_dictt = sample_dict.copy()
sample_dictt.update(sample_dict2)
print(sample_dictt)
sample_dicttt = dict(list(sample_dict.items()) + list(sample_dict2.items()))
print(sample_dicttt)
sample_dicttt["class_a"]["student"]["marks"]= {"physics": 78,'math': 90, 'history': 85}
sample_dicttt["class_a"]["student2"]["marks"]= {"physics": 55,'math': 95, 'history': 80}
sample_dicttt["class_b"]["student"]["marks"]= {"physics": 94,'math': 35, 'history': 56}
sample_dicttt["class_b"]["student2"]["marks"]= {"physics": 99,'math': 99, 'history': 98}
misha = round(sum(sample_dicttt["class_a"]["student"]["marks"]
      .values()) / len(sample_dicttt["class_a"]["student"]["marks"]
      .values()), 2)
Alex = round(sum(sample_dicttt["class_a"]["student2"]["marks"]
      .values()) / len(sample_dicttt["class_a"]["student2"]["marks"]
      .values()), 2)
Grisha = round(sum(sample_dicttt["class_b"]["student"]["marks"]
      .values()) / len(sample_dicttt["class_b"]["student"]["marks"]
      .values()), 2)
Falex = round(sum(sample_dicttt["class_b"]["student2"]["marks"]
      .values()) / len(sample_dicttt["class_b"]["student2"]["marks"]
      .values()), 2)
marks = {"mishaavg": misha,"grishaavg": Grisha,"alexavg": Alex, "falexavg": Falex}
print(marks)
print(max(marks, key=marks.get))
classa = round(misha / 2 + Alex / 2, 2)
classb = round(Grisha / 2 + Falex / 2, 2)
marksclass = {"classaavg":classa, "classbavg": classb}
print(marksclass)
print(max(marksclass, key=marksclass.get))