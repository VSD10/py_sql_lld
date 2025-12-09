from model.account_model import account_model
from db.connection import connection
class account_service():
    def __init__(self):
        self.con=connection()

    def open_acc(self):
        if not self.con:
            print("db not connected")
        try:
            cursor=self.con.cursor()
            customer_id=int(input("enter your customer id "))
            print("checking customer id")
            cursor.execute("select * from customer where customer_id=%s",(customer_id,))
            r=cursor.fetchone()
            if not r:
                print("customer id not exists")
                return
            else:
                print("customer id exists")
            acc_type=input("enter account type saving/current ")
            balance=int(input("enter initial balance "))
            sql='insert into accounts(custome_id,account_type,balance,status,Created_date) values(%s,%s ,%s,%s,%s)'
            data=account_model(customer_id,acc_type,balance,"Active","2025-12-12")
            cursor.execute(sql,data.to_tuple())
            self.con.commit()
            print("account opened successfully")
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                self.con.close()
            except:
                pass
    def balance(self):
        if not self.con:
            print("db not connected")
        try:
            cursor=self.con.cursor()
            acc_id=int(input("enter your account id "))
            print("checking account id")
            cursor.execute("select * from account where acc_id=%s",(acc_id,))
            r=cursor.fetchone()
            if not r:
                print("account id not exists")
                return
            else:
                print("account id exists")
                print(f"your account balance is {r[3]}")
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                self.con.close()
            except:
                pass

