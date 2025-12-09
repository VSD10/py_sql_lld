import mysql.connector
from tabulate import tabulate
def get_connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="service_center_db"
    )
    if con:
        print("connected")
        return con
    else:
        return 
def addcus():
    pass
def addveh():
    pass
def regser():
    pass
def updser():
    pass
def view():
    con = get_connection()   # or get_connection(), but be consistent
    if not con:
        return
    cursor = None
    try:
        cursor = con.cursor()
        sql = """
        SELECT 
            c.customer_id,
            c.name,
            c.phone,
            v.vehicle_id,
            v.model,
            v.number_plate,
            v.vehicle_type,
            s.service_type,
            s.service_date,
            s.delivery_date,
            s.status
        FROM customers c
        JOIN vehicles v ON c.customer_id = v.customer_id
        JOIN service_records s ON v.vehicle_id = s.vehicle_id
        """
        cursor.execute(sql)

        row = cursor.fetchall()

        if not row:
            print("No service records found.")
        else:
            print(tabulate(
                row,
                headers=[
                    "Customer ID","Name","Phone",
                    "Vehicle ID","Model","Number plate","Vehicle Type",
                    "Service Type","Service Date","Delivery Date","Status"
                ],
                tablefmt="grid"
            ))
    except Exception as e:
        print("error", e)
    finally:
        try:
            if cursor:
                cursor.close()
            con.close()
        except:
            pass


def viewpen():
    con = get_connection()   # or get_connection(), but be consistent
    if not con:
        return
    cursor = None
    try:
        cursor = con.cursor()
        sql = """
        SELECT * from customers
        """
        cursor.execute(sql)
        row = cursor.fetchall()

        if not row:
            print("No service records found.")
        else:
            print(tabulate(row))
    except Exception as e:
        print("error", e)
    finally:
        try:
            if cursor:
                cursor.close()
            con.close()
        except:
            pass





def main():
    while True:
        print("\n\n\t\tService Center Management System\n")
        val='''
1. Add Customer
2. Add Vehicle
3. Register Service Request
4. Update Service Status (Delivery)
5. View All Service Records (JOIN)
6. View Pending Services (status = In-Service)
7. Exit
                '''
        print(val)

        try:
            choice = int(input("Your option: "))
        except ValueError:
            print("❌ Please enter a valid number (1-5).")
            continue

        if choice == 1:
            addcus()
        elif choice == 2:
            addveh()
        elif choice == 3:
            regser()
        elif choice == 4:
            updser()
        elif choice == 5:
            view()
        elif choice==6:
            viewpen()
        elif choice==7:
            print("byee")
            return
        else:
            print("❌ Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
