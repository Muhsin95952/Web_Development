def table(x):
    print("Table of ", x, "is given below...")
    for i in range(11):
        print(i, "x", x, "=", i*int(x))


table(input("Enter a number: "))
      