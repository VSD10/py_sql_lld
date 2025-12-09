import mysql.connector
from tabulate import tabulate
# ---------- DB CONNECTION ----------

def get_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Harinisri2012",   # ← change this
            database="db"                    # ← change if needed
        )
        if con.is_connected():
            # print("Connected")  # optional
            return con
        else:
            print("❌ Could not connect to database.")
            return None
    except mysql.connector.Error as e:
        print("❌ Error while connecting to MySQL:", e)
        return None


# ---------- INSERT ----------

def insert():
    con = get_connection()
    if con is None:
        return

    try:
        cursor = con.cursor()

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        city = input("Enter City: ")
        phone = input("Enter Phone: ")   # keep as string (VARCHAR)

        sql = "INSERT INTO users (name, age, city, phone) VALUES (%s, %s, %s, %s)"
        vals = (name, age, city, phone)

        cursor.execute(sql, vals)
        con.commit()

        print("✔ New student inserted successfully!")

    except ValueError:
        print("❌ Invalid input type. Age must be a number.")
    except mysql.connector.Error as e:
        print("❌ Database error during INSERT:", e)
        con.rollback()
    except Exception as e:
        print("❌ Unexpected error during INSERT:", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


# ---------- UPDATE ----------

def update():
    con = get_connection()
    if con is None:
        return

    try:
        cursor = con.cursor()

        id_val = int(input("Enter ID to update: "))
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        city = input("Enter New City: ")
        phone = input("Enter New Phone: ")

        sql = "UPDATE users SET name=%s, age=%s, city=%s, phone=%s WHERE id=%s"
        vals = (name, age, city, phone, id_val)

        cursor.execute(sql, vals)
        con.commit()

        if cursor.rowcount == 0:
            print("❌ No student found with that ID. Nothing updated.")
        else:
            print("✔ Student updated successfully!")

    except ValueError:
        print("❌ Invalid input type. ID and Age must be numbers.")
    except mysql.connector.Error as e:
        print("❌ Database error during UPDATE:", e)
        con.rollback()
    except Exception as e:
        print("❌ Unexpected error during UPDATE:", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


# ---------- DELETE ----------

def delete():
    con = get_connection()
    if con is None:
        return

    try:
        cursor = con.cursor()

        id_val = int(input("Enter ID to delete: "))

        sql = "DELETE FROM users WHERE id=%s"
        vals = (id_val,)

        cursor.execute(sql, vals)
        con.commit()

        if cursor.rowcount == 0:
            print("❌ No student found with that ID. Nothing deleted.")
        else:
            print("✔ Student deleted successfully!")

    except ValueError:
        print("❌ Invalid input type. ID must be a number.")
    except mysql.connector.Error as e:
        print("❌ Database error during DELETE:", e)
        con.rollback()
    except Exception as e:
        print("❌ Unexpected error during DELETE:", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


# ---------- SEARCH (VIEW ALL) ----------

def search():
    con = get_connection()
    if con is None:
        return

    try:
        cursor = con.cursor()

        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("ℹ No students found.")
        else:
            print("\nID | NAME       | AGE | CITY       | PHONE")
            print("-------------------------------------------")
            for row in rows:
                # row = (id, name, age, city, phone)
                print(f"{row[0]}  | {row[1]}  | {row[2]}  | {row[3]}  | {row[4]}")

    except mysql.connector.Error as e:
        print("❌ Database error during SEARCH:", e)
    except Exception as e:
        print("❌ Unexpected error during SEARCH:", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def searchbycity():
    con = get_connection()
    if con is None :
        return
    try:
        cursor=con.cursor()
        city=input("enter a city name:: ")
        sql="select * from users where city=%s"
        cursor.execute(sql,(city,))
        row=cursor.fetchall()
        print(tabulate(row,headers=["id","name","age","city","phone"],tablefmt="grid"))
    except mysql.connector.Error as e:
        print("the database as some errors",e)
    except Exception as e:
        print("it has some error",e)
    finally:
        try :
            cursor.close()
            con.close()
        except:
            pass
def prints(row):
    print(tabulate(row,headers=["id","name","age","city","phone"],tablefmt="grid"))


def searchbyid():
    con=get_connection()
    if con is None :
        return
    cursor=con.cursor()
    try:
        id=int(input("enter a id:"))
        sql="select * from users where id=%s"
        cursor.execute(sql,(id,))
        row=cursor.fetchall()
        prints(row)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


    



# ---------- MAIN MENU ----------

def main():
    while True:
        print("\n\n\t\tStudent Management System\n")
        print("1. New Student (INSERT)")
        print("2. Update Student")
        print("3. Search Students")
        print("4. Delete Student")
        print("5. Exit")
        print("6. Search student by city")
        print("7. Search student by id")

        try:
            choice = int(input("Your option: "))
        except ValueError:
            print("❌ Please enter a valid number (1-5).")
            continue

        if choice == 1:
            insert()
        elif choice == 2:
            update()
        elif choice == 3:
            search()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Exiting... Bye!")
            break
        elif choice==6:
            searchbycity()
        elif choice==7:
            searchbyid()
        else:
            print("❌ Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
