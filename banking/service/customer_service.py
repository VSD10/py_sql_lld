from model.customer_model import customer_model 
from db.connection import connection

class customer_service:
    def __init__(self):
        self.con=connection()

    def create_acc(self):
        if not self.con:
            print("db not cnnected")
        try:
            name=input("enter your name")
            email=input("enter your email ")
            phone=input("enter your phone ")
            sql='insert into customer(name,email,phone) values(%s,%s,%s)'
            data=customer_model(name,email,phone)
            cursor=self.con.cursor()
            cursor.execute(sql,data.to_tuple())
            self.con.commit()
            print("account created")
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                self.con.close()
            except:
                pass

    def get_customer(self):
        if not self.con:
            print("db not cnnected")
        try:
            email=input("enter your email ")
            cursor=self.con.cursor()
            cursor.execute("select * from customer where email=%s",(email,))
            r=cursor.fetchone()
            print(r)
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                self.con.close()
            except:
                pass



