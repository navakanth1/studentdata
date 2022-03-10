import sqlite3 as sql
from prettytable import PrettyTable
connection=sql.connect("records.db")

listOfStudTable=connection.execute("select name from sqlite_master where type='table' AND name='student'").fetchall()

if listOfStudTable!=[]:
    print("table is created successfully")
else:
    connection.execute('''create table records(
                                  ID integer primary key autoincrement,
                                  recordName text,
                                  record_rollNo integer,
                                  exam_record text,
                                  total_records integer
);   ''')
    print("Table Created Successfully.")

while True:

    print("1. Add record name :")
    print("2. record_roll  no :")
    print("3. Search record using Partial name :")
    print("4. Search record using  Roll number :")
    print("5. Update record with Roll no Number :")
    print("6. Delete using roll number:")
    print("7. Total records :")
    print("8. exit")

    choice=int(input("Enter choice :"))

    if choice==1:
        getName=input("Enter name :")
        getRollNum=input("Enter the Roll Number :")
        getexam=input("Enter the exxam :")
        gettotal=input("Enter the total records :")
        connection.execute("insert into records(recordname,record_rollno,exam_record,total_records)\
                                  values('" + getName + "'," + getRollNum + ",'" + getexam + "'," + gettotal + ")")
        connection.commit()
        print("records Data Added Successfully.")

    elif choice == 2:
        result = connection.execute("select * from records")
        table = PrettyTable(
            ["ID", "NAME", "ROLL NO", "exam", "total"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(table)

    elif choice == 3:
        getName = input("Search the Partial Name Which you want:")

        result=connection.execute("select * from records where Name like '"+getName+"%'")
        table=PrettyTable(["ID","NAME", "ROLL NO", "exam", "total"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(table)
    elif choice==4:
        getRollNum = input("Enter the records to Search ")


        result=connection.execute("select * from records where RollNo="+getrollnum+" or AdmnNo="+gettotal+"")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "exam", "total"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(table)

    elif choice==5:
        getrollnum = input("Enter the roll number to get Update :")
        getName = input("Enter name :")
        getRollNum = input("Enter the Roll Number :")
        getexam = input("Enter the exxam :")
        gettotal = input("Enter the total records :")



        connection.execute("update student set Name='"+getName+"',RollNo="+getRollNum+",ExamName='"+getexam+"',total_records="+gettotal+"")
        connection.commit()
        print("Updated Successfully.")


    elif choice == 6:
        getrollnum = input("Enter the Roll_number to get Delete :")
        connection.execute("delete from records where record_rollNo=" + getrollnum + "")
        connection.commit()
        print("Data Deleted Successfully.")


    elif choice == 7:
        result = connection.execute("select count(*) from records")
        for i in result:
            print("Total records Count :", i[0])

    elif choice == 8:
        break

    else:
        print("invalid option")

