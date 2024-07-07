class Customer:
    cid=0
    name=""
    balance=0.0
    def __init__(self,cid,name,balance):#to initialize values for object
        self.cid=cid
        self.name=name
        self.balance=balance
    def __str__(self):#to return a string
        return "({0},{1})".format(self.name,self.balance)
    def withdrawAmount(cid,amount):#to withdraw amount from a account
        for i in b.cdobj:
            if i==cid:#checks if customer exists or not
                if b.cdobj.get(i).balance<amount:#checks if balance is sufficient or not
                    print("Balance is not sufficient")
                    cid=str(cid)
                    s="Customer of id "+cid+" tried to withdraw funds but they were insufficient"
                    filec.write(s)
                    filec.write("\n")
                else:
                    b.cdobj.get(i).balance-=amount
                    cid=str(cid)
                    amount=str(amount)
                    print("Amount withdrawn succesfully")
                    s="Customer of id "+cid+" successfully withdrew funds of "+amount+" Rs"
                    filec.write(s)
                    filec.write("\n")
                break
        else:
            print("Customer doesn't exist")
            s="Unknown user with no id tried to withdraw amounts"
            filec.write(s)
            filec.write("\n")
    def depositAmount(cid,amount):#to deposit amount in an account
        for i in b.cdobj:
            if i==cid:#checks if customer exists or not
                b.cdobj.get(i).balance+=amount
                print("Amount deposited successfully")
                cid=str(cid)
                amount=str(amount)
                s="Customer of id "+cid+" successfully deposited funds of "+amount+" Rs"
                filec.write(s)
                filec.write("\n")
                break
        else:
            print("Customer doesn't exist")
            s="Unknown user with no id tried to deposit amounts"
            filec.write(s)
            filec.write("\n")
    def viewBalance(cid):#to view a balance
        for i in b.cdobj:
            if i==cid:#checks if customer exists or not
                print("Balance is ",b.cdobj.get(i).balance)
                cid=str(cid)
                s="Customer of id "+cid+" viewed their balance"
                filec.write(s)
                filec.write("\n")
                break
        else:
            print("Customer doesn't exist")
            s="Unknown user with no id tried to view balance"
            filec.write(s)
            filec.write("\n")
        
class Bank:
    cdstr={}#main dictionary for customer details
    cdobj={}
    total=0#variable to store total amount in bank
    balance=0.0
    def addCustomer(self,cid,name,balance):#to add a Customer
        self.balance=balance
        self.total+=balance
        co=Customer(cid,name,balance)
        a=co.__str__()
        c1={cid:a}#temporary dictionary
        c2={cid:co}
        self.cdstr.update(c1)#adds customer id and object in dictionary
        self.cdobj.update(c2)
        cid=str(cid)
        balance=str(balance)
        s="Banker added a customer of with customer id "+cid+" with name "+name+" and opening balance of "+balance
        fileb.write(s)
        fileb.write("\n")
    def viewAllCustomer(self):#to view all Customers
        print(self.cdstr)
        s="Banker viewed All Customers"
        fileb.write(s)
        fileb.write("\n")
    def searchCustomer(self,cid):#to search for a Customer
        for i in self.cdstr:
            if i==cid:
                print("Customer found")
                print(self.cdstr.get(cid))
                cid=str(cid)
                s="Banker sucessfully searched for a customer of id "+cid
                fileb.write(s)
                fileb.write("\n")
                break
        else:
            print("Customer not found")
            s="Banker tried to search for a customer but couldn't find it"
            fileb.write(s)
            fileb.write("\n")
    def totalAmount(self):#to view total amount in bank
        print("Total amount in bank is ")
        print(self.total)
        s="Banker viewed the total amount in the bank"
        fileb.write(s)
        fileb.write("\n")
    def viewCustomer(self,id):#to view a customer
        for i in self.cd:
            if i==cid:
                print("Customer found")
                print(self.cdstr.get(cid))
                cid=str(cid)
                s="Banker sucessfully searched for a customer of id "+cid
                fileb.write(s)
                fileb.write("\n")
                break
        else:
            print("Customer not found")
            s="Banker tried to search for a customer but couldn't find it"
            fileb.write(s)
            fileb.write("\n")

flag1=True#it checks if outer loop should keep running .
b=Bank()#object of class Bank
fileb=open("BankerLogs.txt","w")#file of Banker
filec=open("CustomerLogs.txt","w")#file of Customer
while flag1:
    print("Welcome to PYTHON Bank Management System")
    print()
    print("Select your role")
    print()
    print("    1.Banker")
    print("    2.Customer")
    print("    3.Exit")
    while True:
        try:
            choice=int(input("Choose your role "))
            break
        except Exception as e:
            print("Enter proper value")
    if choice==1:#if user selects one
        flag1=True
        continueOps="y"
        while flag1 and continueOps=="y":
            print("Welcome to Banker's App")
            print("   Operation's Menu")
            print("      1.Add Customer")
            print("      2.View Customer")
            print("      3.Search Customer")
            print("      4.View all Customer")
            print("      5.Total Amount in Bank")
            while True:
                try:
                    choice2=int(input("Enter choice   :-  "))
                    break
                except Exception as e:
                    print("Enter proper value")
            print("--------------------------------------")
            if choice2==1:#if chosen 1 in Bankers App 
                while True:
                    try:
                        cid=int(input("Enter customer id "))
                        balance=float(input("Enter opening balance "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                name=input("Enter customer name ")
                b.addCustomer(cid,name,balance)
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                print("--------------------------------------")
            elif choice2==2:#if chosen 2 in Bankers App
                while True:
                    try:
                        cid=int(input("Enter Customer id you want to view "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                b.viewCustomer(cid)
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                print("--------------------------------------")
            elif choice2==3:#if chosen 3 in Bankers App
                while True:
                    try:
                        cid=int(input("Enter Customer id you want to view "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                b.searchCustomer(cid)
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                print("--------------------------------------")
            elif choice2==4:#if chosen 4 in Bankers App
                b.viewAllCustomer()
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                print("--------------------------------------")
            elif choice2==5:#if chosen 5 in Bankers App
                b.totalAmount()
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                print("--------------------------------------")
            else:#if user inputs a wrong value
                print("Choose between 1 and 5")
                continueOps=input("Do you want to perform further operations . Type 'y' for yes or 'n' for No :- ")
                while continueOps!="y" and continueOps!="n":
                    continueOps=input("Enter either 'y' or 'n' ,Input now ")
                if continueOps=="n":
                    break
                print("--------------------------------------")
    elif choice==2:#if user selects 2
        continueOrNot="y"
        while continueOrNot=="y":
            print("Operations Menu")
            print("    1.Withdraw Amount")
            print("    2.Deposit Amount")
            print("    3.View Balance")
            while True:
                try:
                    choice3=int(input("Enter your choice "))
                    break
                except Exception as e:
                    print("Enter proper value")
                    print("--------------------------------------")
            if choice3==1:#if choosen to withdraw amount
                while True:
                    try:
                        cid=int(input("Enter customr id "))
                        balance=float(input("Enter balance "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                        print("--------------------------------------")
                Customer.withdrawAmount(cid,balance)
                print("--------------------------------------")
                while True:
                    try:         
                        continueOrNot=input("Do you want to continue in Customer Menu . Type 'y' for yes and 'n' for no ")
                        print("--------------------------------------")
                        break
                    except Exception as e:
                        print("Enter 'y' or 'n'")
                        print("--------------------------------------")
            elif choice3==2:#if choosen to deposit amount
                while True:
                    try:
                        cid=int(input("Enter customr id "))
                        balance=float(input("Enter balance "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                        print("--------------------------------------")
                Customer.depositAmount(cid,balance)
                print("--------------------------------------")
                while True:
                    try:         
                        continueOrNot=input("Do you want to continue in Customer Menu . Type 'y' for yes and 'n' for no ")
                        print("--------------------------------------")
                        break
                    except Exception as e:
                        print("Enter 'y' or 'n'")
                        print("--------------------------------------")
            elif choice3==3:#if choosen to view balance
                while True:
                    try:
                        cid=int(input("Enter customr id "))
                        break
                    except Exception as e:
                        print("Enter proper value")
                        print("--------------------------------------")
                Customer.viewBalance(cid)
                print("--------------------------------------")
                while True:
                    try:         
                        continueOrNot=input("Do you want to continue in Customer Menu . Type 'y' for yes and 'n' for no ")
                        print("--------------------------------------")
                        break
                    except Exception as e:
                        print("Enter 'y' or 'n'")
                        print("--------------------------------------")
            else:#if a wrong input is given
                print("Enter between 1 and 3")
                print("--------------------------------------")
                
    elif choice==3:#if user chooses to exit
        print("You have chosen to exit our System")
        fileb.close()
        filec.close()
        flag1=False
    else:#if user selects something else
        print("Select from 1,2 or 3")
        print("--------------------------------------")
