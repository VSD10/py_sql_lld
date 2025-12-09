class account_model():
    def __init__(self,ci,at,b,s,ca):
        self.customer_id=ci
        self.account_type=at
        self.balance=b
        self.status=s
        self.created_at=ca

    def to_tuple(self):
        return (self.customer_id,self.account_type,self.balance,self.status,self.created_at)