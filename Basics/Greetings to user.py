user=['Sohel','Rana','Mehera','Meher','Admin']
#user=[]
if user:
    for name in user:
        if name.lower()=='admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello",name.title(),"thank you for logging again")
else:
    print("We need to find some users!")