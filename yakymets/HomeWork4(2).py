v = 0
while True :
    words = input(" Введите своё любимое число ")
    v += 1
    if v <= 3:
        if words.isdigit() == True:
            print(" Спасибо ")
            break
        if words.isdigit() == False:
            print("Неверно, попробуйте ещё раз.")
    elif 3 < v <= 5:
        if words.isdigit() == True:
            print(" Спасибо ")
            break
        if words.isdigit() == False:
            print(" Внимательней ! Нужно ввести именно число ! ")
    elif 5 < v <= 6:
         input(" Если не сейчас , то никогда . Введите число !")
         if words.isdigit() == True:
            print(" Ура ! Хорошего Вам дня.")
            break
         if words.isdigit() == False:
            print(" Никогда сюда не возвращайтесь! ")
            break