from db.connection import connection
from service.account_service import account_service
from service.transaction_service import transaction_service
from service.customer_service import customer_service
class main:
    def __init__(self):
        self.cs=customer_service()
        self.acc=account_service()
        self.tr=transaction_service()
    def st(self):
        while True:
            d='''
    1.create acc
    2.open acc
    3.deposit
    4.get customer by email
    5.get acc balance
    6.withdraw'''
            print(d)
            c=int(input("choice : "))
            if c==1:
                self.cs.create_acc()
            elif c==2:
                self.acc.open_acc()
            elif c==3:
                self.tr.transaction()
            elif c==4:
                self.cs.get_customer()
            elif c==5:
                self.acc.balance()
            elif c==6:
                self.tr.withdraw()
            

            else:
                return
            


if __name__=="__main__":
    new=main()
    new.st()