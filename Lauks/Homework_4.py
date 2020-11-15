# Task 1
lst = [9, 7, 6, 8, 4, 6, 5, 0]
ind = 1
while ind <= len(lst) - 1:
    if lst[ind - 1] > lst[ind]:
        lst[ind], lst[ind - 1] = lst[ind - 1], lst[ind]
        ind = 1
        continue
    else:
        ind += 1
print(lst)


# Task 2
cnt = 0
print('Please enter your favourite number')
while True:
    fav_num = input()
    cnt += 1
    if fav_num.isdigit() is False:
        if cnt <= 3:
            print ('Please be more attentive, enter a "number"!')
            continue
        elif 3 < cnt <= 5:
            print('Enter a NUMBER!!!')
            continue
        elif cnt == 6:
            print('It is your last chance!!!')
            continue
        else:
            print('You are stupid mother fucker!!!')
            break
    else:
        print('Great, thank you!')
        break