i = 0
while True:
    n = input("your favorite number")
    i = i + 1
    if n.isdigit() is True:
        print("good boy")
        break
    if n.isdigit() is False:
        if i == 1:
            print("no problem, this time try number")
        if i == 2:
            print("come on i told you to print number")
        if i == 3:
            print("are you kidding me!!!!! look above it is"
                        "NOT NUMBER!!! print pls number")
        if i == 4:
            print("OMG!!!!print number or i will find you ip")
        if i == 5:
            print("OMGOMG!!! you are not very clever, i know you ip"
                        " already!!! its your last CHANCE! print number!!!!")
        if i == 6:
            print("okay MTFCR, i am coming for you!! RUNNNNNNN!!!!! ")
            break
        continue
