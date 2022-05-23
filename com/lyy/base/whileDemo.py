# while语法
count = 0
while count < 10:
    count += 1
    print("loop", count)

# while实现猜年龄
count = 0
age = 25
while count < 3:
    inputAge = input("Input age:")
    if inputAge.isdigit():
        inputAge = int(inputAge)
    else:
        print("error:Please input int.")
        continue
    if inputAge > age:
        print("Bigger")
    elif inputAge < age:
        print("Smaller")
    else:
        print("Correct, congratulation!")
        break
    count += 1
    if count == 3:
        inputMsg = input("Whether or not to continue?(y/n)")
        if inputMsg in ['y', 'Y', "YES", "yes", "Yes"]:
            count = 0
        elif inputMsg in ['n', 'N', "NO", "no", "No"]:
            print("Bye~")
            break
        else:
            print("error:Please input 'y' or 'n'.")