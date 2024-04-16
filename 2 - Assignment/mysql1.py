import mysql.connector

con = mysql.connector.connect(host="localhost", username="root", password="chandrakiran30@", database="demo")

#con=mysql.connector.connect(host="localhost",user="root",password="rajagr98@",database="python_db")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users (name,age,city) values (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data ingested sucessfully")
def update(id,name,age,city):
    res = con.cursor()
    sql="update users set name=%s, age=%s, city=%s where id=%s;"
    user=(name, age, city, id)
    res.execute(sql, user)
    con.commit()
    print("Data updated sucessfully")
def select():
    res=con.cursor()
    sql="select ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result=res.fetchall()
    print(result)
    #print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))


def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s;"
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print("User deleted sucessfully")

while True:
    print("1.Insert Data")
    print("2.update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    
    choice = int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter Name : ")
        age=int(input("Enter your Age : "))
        city=input("Enter city : ")
        insert(name,age,city)

    elif choice == 2:
        id=int(input("Enter the ID : "))
        name = input("Enter Name : ")
        age = int(input("Enter your Age : "))
        city = input("Enter city : ")
        update(id,name, age, city)

    elif choice == 3:
        select()

    elif choice == 4:
        id = int(input("Enter the ID : "))
        delete(id)

    elif choice == 5:
        quit()
    else:
        print("Invalid selection. Please try Again")

