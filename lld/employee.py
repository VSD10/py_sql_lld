import mysql.connector
from tabulate import tabulate
def getcon():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="payroll_db"
    )
    if con:
        return con
    else:
        print("not connected")
        return
def main():
    while True:
        val='''
1.add department
2.add employee
3. process monthly salary
4.mark salary as paid
5.view salary record (join)
6.view pending systems
7.exit'''
        print(val)
        choice=int(input("Enter choice : "))
        if choice ==1:
            adddept()
        elif choice==2:
            addemp()
        elif choice==3:
            pms()
        elif choice ==4:
            msap()
        elif choice==5:
            vsp()
        elif choice==6:
            vps()
        elif choice==7:
            return
def adddept():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        name=input("enter a depart name : ")
        desc=input("enter a description :")
        val=(name,desc)
        sql=("insert into departments(dept_name,description) values(%s,%s)")
        cursor.execute(sql,val)
        con.commit()
        print("data inserted ")
    except:
        print("not inserted")
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def addemp():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        name=input("enter  name : ")
        role=input("enter a role :")
        dept_id=int(input("enter a depart id : "))
        phone=input("enter a phone:")
        email=input("enter a email : ")
        val=(name,role,dept_id,phone,email)
        sql=("insert into employees(name,role,dept_id,phone,email) values(%s,%s,%s,%s,%s)")
        cursor.execute(sql,val)
        con.commit()
        print("data inserted ")
    except:
        print("not inserted")
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def pms():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        emp_id=int(input("enter  emp_id : "))
        month=input("enter a month :")
        basic_salary=int(input("enter a basic salary : "))
        bonus=int(input("enter a bonus:"))
        deductions=int(input("enter a deductions : "))
        net=basic_salary+bonus-deductions
        val=(emp_id,month,basic_salary,bonus,deductions,net,"pending")
        sql=("insert into salary_records(emp_id,month,basic_salary,bonus,deductions,net_salary,status) values(%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(sql,val)
        con.commit()
        print("data inserted ")
    except:
        print("not inserted")
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def vsp():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        val='''
        select distinct    
         s.salary_id,
         e.name,
         d.dept_name,
         s.month,
         s.basic_salary,
         s.bonus,
         s.deductions,
         s.net_salary,
         s.status 
        from departments d 
        join employees e on d.dept_id=e.dept_id
        join salary_records s on e.emp_id=s.emp_id

'''
        sql=(val)
        cursor.execute(sql)
        r=cursor.fetchall()
        print(tabulate(r,tablefmt="rounded_outline"))
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def vps():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        val="SELECT * FROM salary_records WHERE status='Pending';"
        sql=(val)
        cursor.execute(sql)
        r=cursor.fetchall()
        print(tabulate(r))
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def msap():
    con=getcon()
    if not con:
        return
    try:
        cursor=con.cursor()
        id=int(input("enter a salary id :"))
        print("checking the id ")
        cursor.execute("select salary_id,status from salary_records where salary_id=%s or status=%s",(id,"Pending"))
        r=cursor.fetchone()
        print(r)
        if r:
            print("id present")
        else:
            print("id not present")
            return
        if r[1]=="Pending":
            print("salary is processing........")
        else:
            print("salary already processed")
            return
        cursor.execute("update salary_records set status=%s where salary_id=%s",("Processed",id))
        print("processed")
        con.commit()
    except Exception as e:
        print("error found",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
if __name__=="__main__":
    main()




























# def createdb():
#     con=mysql.connector.connect(
#         host='localhost',
#         user="root",
#         password="#Harinisri2012"
#     )
#     cursor=con.cursor()
#     cursor.execute("create database if not exists payroll_db ")
#     print("database created")

# def createtable():
#     con=mysql.connector.connect(
#         host="localhost",
#         user='root',
#         password="#Harinisri2012",
#         database="payroll_db"
#     )
#     cursor=con.cursor()
#     cursor.execute("create table if not exists departments( dept_id int primary key auto_increment, dept_name varchar(50),description varchar(50))")
#     cursor.execute("create table if not exists employees(emp_id int primary key auto_increment , name varchar(50), role varchar(50), dept_id int ,phone varchar(20),email varchar(50))")
#     cursor.execute("create table if not exists salary_records(salary_id int primary key auto_increment ,emp_id int, month varchar(50), basic_salary int, bonus int,deductions int,net_salary int, status varchar(50))")
#     print("tables are created")



# createdb()
# createtable()