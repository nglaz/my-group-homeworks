v = 0
while True :
    words = input(" Введите своё любимое число ")
    v += 1
    if  words.isdigit() == True:
        print(" Спасибо ")
        break
    elif words.isdigit() == False:
        if v<=3 :
             print("Ошибка, попробуйте ещё раз")
        if 3<v<5 :
             print("Нужно быть внимательнее")
        if 4<v<6 :
            print("Нужно быть внимательнее")
            print("Остался последний шанс")
        if 5<v<=6:
             print("Не возвращайтесь сюда никогда")
             break
