from model.transaction_model import transaction_model
from db.connection import connection
class transaction_service:
    def __init__(self):
        self.con=connection()
    
    def transaction(self):
        if not self.con:
            return
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
            to_account_id=int(input("enter to account id "))
            amount=int(input("enter amount "))
            type=input("enter transaction type deposit/withdraw ")
            data=transaction_model(acc_id,to_account_id,amount,type,"2025-12-12")
            sql="insert into transaction(from_account_id,to_account_id,amount,type,created_at,status,remarks) values(%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sql,data.to_tuple())
            print("updating the account balance")
            if type=="deposit":
                cursor.execute("update account set balance=balance+%s where account_id=%s",(amount,to_account_id))
                cursor.execute("update account set balance=balance-%s where account_id=%s",(amount,acc_id))
            self.con.commit()
            print("transaction done")
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                self.con.close()
            except:
                pass    
        