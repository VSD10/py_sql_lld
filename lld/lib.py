import mysql.connector 
from tabulate import tabulate
def create_db():
    try:
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Harinisri2012"
        )
        cursor=con.cursor()
        cursor.execute("create database if not exists librarydb")
        print("The library Database created")
    except Exception as e:
        print("Error found ",e)

def create_table():
    try:
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Harinisri2012",
            database="librarydb"
        )
        cursor=con.cursor()
        sql='''
        CREATE TABLE IF NOT EXISTS members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(20),
    status VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author VARCHAR(50),
    genre VARCHAR(50),
    stock INT
);
CREATE TABLE IF NOT EXISTS borrowings (
    borrow_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(20)
);

'''
        cursor.execute(sql)
        print("table create successfully")
    except Exception as e:
        print("found error", e)

def safeinput(p,c):
    while True:
        try:
            val=c(input(p))
            return val
        except:
            print("Enter a valid type",c)

def get_connections():
    try:
        con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="#Harinisri2012",
                database="librarydb"
        )
        return con
    except:
        print("database not connected")

def add_member():
    con=get_connections()
    if not con:
        return
    try:
        name=safeinput("Name : ",str)
        email=safeinput("Email : ",str)
        phone=safeinput("Phone : ",str)
        status=safeinput("Status : ",str)
        data=(name,email,phone,status)
        sql="insert into members(name,email,phone,status) values(%s,%s,%s,%s)"
        cursor=con.cursor()
        cursor.execute(sql,data)
        con.commit()
        print("Member added success")
    except:
        print("Member not added!!!!!!!!")
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def add_book():
    con=get_connections()
    if not con:
        return
    try:
        title=safeinput("Book Tittle : ",str)
        author=safeinput("book Author : ",str)
        genre=safeinput("Book genre : ",str)
        stock=safeinput("Stock : ",int)
        data=(title,author,genre,stock)
        sql="insert into books(title,author,genre,stock) values(%s,%s,%s,%s)"
        cursor=con.cursor()
        cursor.execute(sql,data)
        con.commit()
        print("books added success")
    except:
        print("books not added!!!!!!!!")
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def view():
    con=get_connections()
    if not con:
        return
    try:
        sql="select * from books"
        cursor=con.cursor()
        cursor.execute(sql)
        row=cursor.fetchall()
        print(tabulate(row,headers=["Book_id","tittle","author","genre","stock"],tablefmt="grid"))
    except  Exception as e:
        print("failed to  view!!!!!!!!",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


def availablebooks():
    con=get_connections()
    if not con:
        return
    try:
        sql="select * from books where stock>0"
        cursor=con.cursor()
        cursor.execute(sql)
        row=cursor.fetchall()
        print(tabulate(row,headers=["Book_id","tittle","author","genre","stock"],tablefmt="grid"))
    except  Exception as e:
        print("failed to  view!!!!!!!!",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def borrow():
    con=get_connections()
    if not con:
        return
    try:
        member=safeinput("Member Id : ",int)
        cursor=con.cursor()
        print("Checking the member status")
        cursor.execute("select status from members where member_id=%s and status=%s",(member,"Active"))
        mem=cursor.fetchone()
        if not mem:
            print("Member Not found ")
            return
        else:
            print("member found")
        
        if mem[0]=="Active":
            print("Membership is Active")
        else:
            print("Member is Expired")
            return
        book_id=safeinput("Book Id : ",int)
        print("checking the book availability and stocks!")
        cursor.execute("Select stock from books where stock>0 and book_id=%s",(book_id,))
        stock=cursor.fetchone()
        if not stock:
            print("Book not found")
        else:
            print("Book found")
        if stock[0]!=0:
            print("book is available")
        else:
            print("book not available")
            return
        borrow_date=safeinput("Borrowed Date : ",str)
        data=(member,book_id,borrow_date,None,"Borrowed")
        sql="insert into borrowings(member_id,book_id,borrow_date,return_date,status) values(%s,%s,%s,%s,%s)"

        cursor.execute(sql,data)
        print("Recorded Book borrowed")

        cursor.execute("update books set stock=stock-1 where book_id=%s",(book_id,))
        print("Updated book stocks")
        con.commit()
    except:
        print("books not borrowed!!!!!!!!")
    finally:
        try:
            cursor.close()
            con.close()
        except: 
            pass  
def returnbook():
    con=get_connections()
    if not con:
        return
    try:
        b_id=safeinput("Enter id : ",int)
        print("Checking the id about the books Details")
        cursor=con.cursor()
        cursor.execute(
    "SELECT * FROM borrowings WHERE borrow_id = %s AND status = %s",
    (b_id, "Borrowed")
)
        r=cursor.fetchone()
        if not r:
            print("No id found from the borrow id")
        else:
            print("book record found")
            print(r)
        book_id=r[2]
        r_date=safeinput("Enter return date ; ",str)
        cursor.execute("update borrowings set return_date=%s,status=%s where book_id=%s",(r_date,"returned",book_id))
        print("book return updted")
        cursor.execute("update books set stock=stock+1 where book_id=%s",(book_id,))
        print("book stock updated")
        con.commit()
    except Exception as  e:
        print("booked not returned!!",e)
def borrowedbooks():
    con=get_connections()
    if not con:
        return
    try:
        sql='''select 
                b.borrow_id,
                m.name as Member_name,
                bo.title as Book_title ,
                b.borrow_date,
                b.return_date,
                b.status
                from borrowings b
                join members m on b.member_id=m.member_id
                join books bo on b.book_id=bo.book_id'''
        cursor=con.cursor()
        cursor.execute(sql)
        row=cursor.fetchall()
        print(tabulate(row,headers=["Book_id","Name","tittle","date","return","status"],tablefmt="grid"))
    except  Exception as e:
        print("failed to  view borrowed books!!!!!!!!",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def main():
    while True:
        print("""
1. Add Member
2. Add Book
3. View All Books
4. Borrow a Book
5. Return a Book
6. View Borrowed Books (JOIN)
7. View Available Books Only
8. Exit

""")
        try:
            choice=safeinput("enter a choice ",int)
        except ValueError:
            print("dude enter from 1 t0 8")
        if choice == 1:
            add_member()
        elif choice == 2:
            add_book()
        elif choice == 3:
            view()
        elif choice == 4:
            borrow()
        elif choice == 5:
            returnbook()

        elif choice == 6:
            borrowedbooks()
        elif choice == 7:
            availablebooks()
        elif choice == 8:
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")

            


if __name__=="__main__":
    create_db()
    create_table()
    main()
