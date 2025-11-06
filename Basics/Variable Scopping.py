def myf():
    a=20
    def youf():
        a=10
        print("Inner Function.")
        print(a)
    youf()   
    print("Outer Function")
    print(a)
myf()     