name = input("Please enter your name ")
age = input("Please enter your age ")
gender = input("Specify your gender ")


string1 = " Hallo! My name is " + name + ". I'm "\
          + age + " years old " + " and I'm  a " + gender
string2 = " Hallo! My name is %s. I'm %s years old and I'm a %s " % (
    name,
    age,
    gender
)
string3 = " Hallo! My name is {}. I'm {} years old and I'm a {}".format(
    name,
    age,
    gender
)
about_me_string = f"Hallo! My name is {name}. " \
                  f"I'm {age} years old and I'm a {gender}"
sentance = about_me_string.split('.')
sentance1 = sentance[0]
sentance2 = sentance[1]
print(sentance1)
print(sentance2)


about_my_friend_string = about_me_string.replace("Bogdan", "Margarita")\
    .replace("28", "29").replace("male", "female")
print(about_my_friend_string)
list_from_str = about_me_string.split()
print(type(list_from_str))
string_from_list = ' '.join(list_from_str)
print(string_from_list)


string_from_about_me_string = about_me_string.swapcase()
print(string_from_about_me_string)
