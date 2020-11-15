# Task 1
lst = [9, 7, 6, 8, 4, 6, 5, 0]
ind = 1
while ind < len(lst) - 1:
    if lst[ind - 1] > lst[ind]:
        lst[ind], lst[ind - 1] = lst[ind - 1], lst[ind]
        ind = 1
        continue
    else:
        ind += 1
print(lst)

# Task 2
fav_num = input('Please enter your favourite number')
cnt = 1
while fav_num.isdigit() is False:
    cnt += 1
    if cnt <= 3:
        av_num = input('Please be more attentive, enter a "number"!')
        continue
    elif 3 < cnt <= 5:
        fav_num = input('Enter NUMBER!!!')
        continue
    elif cnt == 6:
        fav_num = input('It is your last chance!!!')
        continue
    else:
        print('You are stupid mother fucker!!!')
        break
else:
    print('Great, thank you!')