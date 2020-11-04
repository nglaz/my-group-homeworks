sample_dict = {"class_a": {} ,"student": {} ,  "name":"Misha", "marks":{} ,  "math":90 , "history":85}
print(sample_dict)
print(sample_dict["name"])
print(sample_dict["history"])
sample_dict["class_a"]= "Slipenko"
sample_dict["name"] = "Daryna"
sample_dict["marks"]= "11 , 7 , 10"
print(sample_dict)
sample_dict["class_b"] = "Akunin , Tolstoy , Pushkin"
sample_dict["marks"] = "11 , 7 , 10 , Physics = 10 , Physics = 8 , Physics =12  "
print(sample_dict)
Akunin = 10 , 90 , 85
Tolstoy = 8 , 90 , 85
Pushkin = 12 , 90 , 85
g = (round(sum(Akunin)/len(Akunin),2))
c = (round(sum(Tolstoy)/len(Tolstoy),2))
p = (round(sum(Pushkin)/len(Pushkin),2))
print(g)
print(c)
print(p)
Vyr_dict = {"Akunin" : g , " Tolstoy ": c, "Pushkin": p}
print(Vyr_dict)
best_s = max(dict(Vyr_dict))
print(best_s)
class_a = 11 , 7 , 10 , 90 , 85
class_b = 10 , 8 , 12 , 90 , 85
a = (round(sum(class_a)/len(class_a) , 2))
b = (round(sum(class_b)/len(class_b),2))
print(a)
print(b)
wer_dict = {"class_a": a,"class_b": b}
print(wer_dict)
best_c = max(dict(wer_dict))
print(best_c)
