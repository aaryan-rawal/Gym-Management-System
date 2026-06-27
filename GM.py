import random
import mysql.connector as sqlc

print('''
--------------------------------------------------------------------------------
                                 GYM MANAGEMENT                                  
--------------------------------------------------------------------------------
''')

msp=input("Enter your mysql password:")
if msp=="":
    mydb=sqlc.connect(host="localhost",user="root",password="")
else:
    mydb=sqlc.connect(host="localhost",user="root",password=msp)

mycursor=mydb.cursor()

def database():
    
#CREATEING DATABASE    
    
    mycursor.execute("create database if not exists gym")

#CREATING TABLES

    mycursor.execute("use gym")

    mycursor.execute("create table \
        if not exists \
        yearlyfees(silver int,gold int,\
        platinum int,diamond int)")

    mycursor.execute("create table \
        if not exists \
        login(username varchar(25),\
        password varchar(25) not null)")

    mycursor.execute("create table \
        if not exists \
        member(id int,\
        name varchar(25),\
        gender char(1),\
        category varchar(25),\
        amount int,\
        timeslot varchar(30))")

    mycursor.execute("create table \
        if not exists \
        sno(id int,\
        did int)")

    mycursor.execute("create table \
        if not exists \
        trainer(id int(11),\
        name varchar(25),\
        age int(2) check(age<=35),\
        gender char(1),\
        salary int(11) check(salary<=30000),\
        shift varchar(30))")

    mydb.commit()

#INSERTING IMPORTANT DATA

#INSERTING DATA INTO FEES TABLE

    mycursor.execute("select*from yearlyfees")

    flag=0

    for i in mycursor:

        flag=1

    if flag==0:

        mycursor.execute("insert into yearlyfees \
        values(20000,25000,35000,50000)")

        mydb.commit()

#INSERTING DATA INTO LOGIN TABLE

    mycursor.execute("select*from login")

    flag=0

    for i in mycursor:

        flag=1

    if flag==0:

        mycursor.execute("insert into login \
        values('admin','admin@123')")

        mydb.commit()

#INSERTING DATA INTO SNO TABLE

    mycursor.execute("select*from sno")

    flag=0

    for i in mycursor:

        flag=1

    if flag==0:

        mycursor.execute("insert into sno values(0,0)")

        mydb.commit()

#MAIN SECTION

database()

task=int(input("If you want to perform any \
changes in the database then press 1 else 0:"))

print("Please login first")

password=input("Enter your password:")

mycursor.execute("select*from login")

for i in mycursor:

    t_user,t_pass=i    

while task==1:

    if t_pass==password:

        print('''
1. Add Trainer
2. Add Member
3. Remove Trainer
4. Remove Member
5. Modify
6. Change Password
7. Forgot Password
8. Display Trainer
9. Display Member
10. Exit
''')

        ch1=int(input("Enter Your Choice:"))

#ADDING TRAINER

        if ch1==1:

            name=input("Enter Name:")

            age=input("Enter Age:")

            gender=input("Enter Gender(M/F):")

            salary=int(input("Enter Salary:"))

            mycursor.execute("select*from sno")

            shiftlst=["10am to 2pm","2pm to 6pm","6pm to 10pm","10pm to 2am","2am to 6am","6am to 10am"]

            shift=random.choice(shiftlst)
            
            for i in mycursor:

                t_id,t_did=i

            t_id=t_id+1

            mycursor.execute("insert into \
            trainer values('"+str(t_id)+"','"+name+"',\
            '"+age+"','"+gender+"',\
            '"+str(salary)+"','"+shift+"')")

            mycursor.execute("update sno set id='"+str(t_id)+"'")

            mydb.commit()

            print(f"Trainer added with unique id{t_id}")

#ADDING MEMBER

        elif ch1==2:

            name=input("Enter Name:")

            gender=input("Enter Gender(M/F):")

            print('''
Choose a yearly plan
1. Silver----->amount-->20000  [YEARLY]
2. Gold----->amount-->25000  [YEARLY]
3. Platinum----->amount-->35000  [YEARLY]
4. Diamond----->amount-->50000  [YEARLY]
''')
            ch2=int(input("Enter Your Choice:"))

            mycursor.execute("select*from yearlyfees")

            for i in mycursor:

                t_silver,t_gold,t_platinum,t_diamond=i

            if ch2==1:

                category="silver"

                amount=t_silver

            elif ch2==2:

                category="gold"

                amount=t_gold

            elif ch2==3:

                category="platinum"

                amount=t_platinum

            else:

                category="diamond"

                amount=t_diamond

            print('''
Choose your preferred time slot
1. 10am to 2pm
2. 2pm to 6pm
3. 6pm to 10pm
4. 10pm to 2am
5. 2am to 6am
6. 6am to 10am
''')

            ch9=int(input("Enter your choice:"))

            if ch9==1:
                
                timeslot="10am to 2pm"

            elif ch9==2:

                timeslot="2pm to 6pm"

            elif ch9==3:

                timeslot="6pm to 10pm"
                
            elif ch9==4:

                timeslot="10pm to 2am"

            elif ch9==5:

                timeslot="2am to 6am"

            else:

                timeslot="6am to 10am"
                
            mycursor.execute("select*from sno")

            for i in mycursor:

                t_id,t_did=i

            t_did=t_did+1

            mycursor.execute("insert into member \
            values('"+str(t_did)+"','"+name+"',\
            '"+gender+"','"+category+"',\
            '"+str(amount)+"','"+timeslot+"')")

            mycursor.execute("update sno set did='"+str(t_did)+"'")

            mydb.commit()

            print(f"Member added successfully with unique id{t_did}")

#REMOVING TRAINER

        elif ch1==3:

            idd=int(input("Enter Trainer ID to remove:"))

            mycursor.execute("select*from trainer")

            flag=0

            for i in mycursor:

                t_id=i[0]

                if t_id==idd:

                    flag=1

            if flag==1:

                mycursor.execute("delete from trainer where id='"+str(idd)+"'")

                mydb.commit()

                print("Removed Successfully")

            else:

                print("Trainer ID not found")

#REMOVING MEMBER

        elif ch1==4:

            idd=int(input("Enter Member ID to remove:"))

            mycursor.execute("select*from member")

            flag=0

            for i in mycursor:

                t_id=i[0]

                if t_id==idd:

                    flag=1

            if flag==1:

                mycursor.execute("delete from member where id='"+str(idd)+"'")

                mydb.commit()

                print("Removed Successfully")

            else:

                print("Member ID not found")

#MODIFYING THE DATA

        elif ch1==5:

            loop1="y"

            while loop1=="y":

                print('''
1. Plans
2. Trainer Info
3. Member Info
4. Go Back
''')

                ch3=int(input("Enter your choice:"))

#MODIFYING PLANS

                if ch3==1:

                    print('''
1. Silver
2. Gold
3. Platinum
4. Diamond
''')

                    ch4=int(input("Enter your choice:"))

                    amt=int(input("Enter yearly amount to update:"))

                    if ch4==1:

                        mycursor.execute("update yearlyfees set silver='"+str(amt)+"'")

                        mydb.commit()

                    elif ch4==2:

                        mycursor.execute("update yearlyfees set gold='"+str(amt)+"'")

                        mydb.commit()

                    elif ch4==3:

                        mycursor.execute("update yearlyfees set platinum='"+str(amt)+"'")

                        mydb.commit()

                    else:

                        mycursor.execute("update yearlyfees set diamond='"+str(amt)+"'")

                        mydb.commit()

#MODIFYING TRAINER INFO

                elif ch3==2:

                    idd=int(input("Enter Trainer ID to be modified:"))

                    mycursor.execute("select*from trainer")

                    flag=0

                    for i in mycursor:

                        if t_id==idd:

                            flag=1

                    if flag==1:

                        print('''
1. Name
2. Age
3. Gender
4. Salary
''')

                        ch5=int(input("Enter your choice:"))

                        if ch5==1:

                            name=input("Enter updated name:")

                            mycursor.execute("update trainer set name='"+name+"' \
                            where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                        elif ch5==2:

                            age=input("Enter updated age:")

                            mycursor.execute("update trainer set \
                            age='"+age+"' where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                        elif ch5==3:

                            gender=input("Enter updated gender(M/F):")

                            mycursor.execute("update trainer set \
                            gender='"+gender+"' where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                        else:

                            name=int(input("Enter updated salary:"))

                            mycursor.execute("update trainer set \
                            salary='"+str(salary)+"' where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

#MODIFYING MEMBER INFO    

                elif ch3==3:

                    idd=int(input("Enter Member ID to modify:"))

                    mycursor.execute("select*from member")

                    flag=0

                    for i in mycursor:

                        t_id=i[0]

                        if t_id==idd:

                            flag=1

                    if flag==1:

                        print('''
1. Name
2. Gender
3. Category
''')

                        ch6=int(input("Enter your choice:"))

                        if ch6==1:

                            name=input("Enter updated name:")

                            mycursor.execute("update member set name='"+name+"' \
                            where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                        elif ch6==2:

                            gender=input("Enter updated gender(M/F):")

                            mycursor.execute("update member set gender='"+gender+"' \
                            where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                        else:

                            print('''
1. Silver
2. Gold
3. Platinum
4. Diamond
''')

                            mycursor.execute("select*from yearlyfees")

                            for i in mycursor:

                                t_silver,t_gold,t_platinum,t_diamond=i

                            ch7=int(input("Enter your choice:"))

                            if ch7==1:

                                category="silver"

                                amt=t_silver

                            elif ch7==2:

                                category="gold"

                                amt=t_gold

                            elif ch7==3:

                                category="platinum"

                                amt=t_platinum

                            else:

                                category="diamond"

                                amt=t_diamond

                            mycursor.execute("update member set \
                            category='"+category+"',amount='"+str(amt)+"' \
                            where id='"+str(idd)+"'")

                            mydb.commit()

                            print("Successfully Updated")

                    else:

                        print("ID not found")

                else:

                    break

#CHANGE PASSWORD

        elif ch1==6:

            passs=input("Enter old password:")

            mycursor.execute("select*from login")

            for i in mycursor:

                t_user,t_pas=i

            if t_pas==passs:

                new_pas=input("Enter new password:")

                mycursor.execute("update login set password='"+new_pas+"'")

                mydb.commit()

            else:

                print("Wrong password")
                
#FORGOT PASSWORD                
                
        elif ch1==7:
            
            print('''WARNING:
                  You have to reset the Database''')
            
            ch8=input("Enter y if you want to reset the database else enter n:")
            
            if ch8=="y":
                
                mycursor.execute("drop database gym")
                
                database()
                
                print("Database has been reset successfully")
                
                break
            else:
                
                print("Could not reset the database")
                
#DISPLAY TRAINER                
                
        elif ch1==8:
            
            mycursor.execute("select*from trainer")
            
            print("Displayed in the order",("id","name","age","gender","salary","shift"),sep=" --> ")
            
            for i in mycursor:
                
                print(i)
                
#DISPLAY MEMBER
        
        elif ch1==9:
            
            mycursor.execute("select*from member")
            
            print("Displayed in the order",("id","name","gender","category","amount","timeslot"),sep=" --> ")
            
            for i in mycursor:
                
                print(i)

#EXIT

        else:

            break
        
#PASSWORD IS WRONG

    else:

        print("Wrong password")

        break
