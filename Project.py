import mysql.connector 
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Root123",
database="MANAGER")
mycursor = mydb.cursor()
def add():
    x=input("Enter your Name: ")
    y=input("Enter the Website Name: ")
    z=input("Enter the Password: ")
    sql = "INSERT INTO LOGIN (Name_of_the_User, Website_Name,Password) VALUES (%s, %s, %s)"
    val = (x, y, z)
    mycursor.execute(sql, val)
    print("\nValues added: \n\n Name of the User:",x,"\n WebsiteName:",y,"\n Password:",z)
    mydb.commit()
def update():
    x=input("Enter your Name: ")
    y=input("Enter your Website Name: ")
    z=input("Enter your Old Password: ")
    new=input("Enter your New Password: ")
    d=(new,x,y,z)
    sql = "UPDATE LOGIN SET Password = %s WHERE Name_of_the_User=%s and Website_Name=%s and Password=%s"
    mycursor.execute(sql,d)
    print("\nValues Updated: \n\n Name of the User:",x,"\nWebsite Name:",y,"\n Old Password:",z,"\n NewPassword:",new)
    mydb.commit()
def remove():
    a=input("Enter your Name: ")
    b=input("Enter your Website Name: ")
    c=input("Enter the Password to Remove: ")
    d=(a,b,c)
    mycursor = mydb.cursor()
    sql = "DELETE FROM LOGIN WHERE Name_of_the_User=%s and Website_Name=%s and Password = %s"
    mycursor.execute(sql,d)
    mydb.commit()
    print("\n",mycursor.rowcount, "Record Deleted")
def execute():
    from tabulate import tabulate 
    n=input("Enter your Name: ")
    d=(n,)
    sql = "SELECT * FROM LOGIN WHERE Name_of_the_User= %s"
    mycursor.execute(sql,d)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Name_of_the_User','Website_Name',"Password","Date_and_Time"],
    tablefmt='psql'))
def randompass():
    import random
    a="1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"
    b="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    c="A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    d="!","@","#","$","%","^","*","&","(",")","_","-","+","=","{","[","]","}","|",",","<",">","/",".","~","`"
    g="A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    f="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    h="1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"
    e="!","@","#","$","%","^","*","&","(",")","_","-","+","=","{","[","]","}","|",",","<",">","/",".","~","`"
    i=random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(g)+random.choice(f)+random.choice(h)+random.choice(e)
    print("The required password is :",i)
    g=input("Do you want to SAVE this Password!(y/n): ")
    if g.lower()=="yes" or g.lower()=="y":
        x=input("Enter your Name: ")
        y=input("Enter the Website Name: ")
        z=i
        sql = "INSERT INTO LOGIN (Name_of_the_User,Website_Name, Password) VALUES (%s, %s, %s)"
        val = (x, y, z)
        mycursor.execute(sql, val)
        print("Values added: \n\n Name of the User: ",x,"\n Website Name: ",y,"\n Password: ",z )
    mydb.commit()

def run():
    print("\n Welcome to Password_Manager!")
    password=input("\nEnter the Master Password: ")
    if password.lower()=="thisisthemasterpassword":
        print("\n\n1) To ADD your Password intoPassword_Manager \n2) To UPDATE your Password in this Password_Manager \n3) To REMOVE your Password fromPassword_Manager \n4) To EXECUTE your required Password from Password_Manager \n5) To CREATE randompassword")
        user_input=input("\nEnter your Choice: ")
        if user_input=="1":
            add()
        elif user_input=="2":
            update()
        elif user_input=="3":
            remove()
        elif user_input=="4":
            execute()
        elif user_input=="5":
            randompass()
        else:
            print("Sorry unable to Access: ")
    else:
        print("Your Master Password is INCORRECT!!!")
run()
stop = False
def rerun():
    global stop
choice=input("\nDo you want to Run Again!(y/n): ")
if choice.lower()=="y" or choice.lower=="yes":
    run()
elif choice.lower()=="n" or choice.lower()=="no":
    print("Bye!!!")
stop = True

while True:
    if stop == True:
        break
    rerun()
