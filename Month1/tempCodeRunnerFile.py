def check_file():
    count =0
    with open("Todo.txt", "r") as f:
        for line in f:
            num = line.strip().split(",")
            num = [int(x) for x in num ]
            print(num)
            for y in num:
                if y%2==0:
                    print(y)
                    count+=1
            print("Total is ",count)       
        

check_file()
