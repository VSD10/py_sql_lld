class transaction_model():
    def __init__(self,f,t,a,ty,c,s,r):
        self.from_acc=f
        self.to_acc=t
        self.amount=a
        self.type=ty
        self.created_at=c
        self.status=s
        self.remarks=r

    def to_tuple(self):
        return ( self.from_acc,self.to_acc,self.amount,self.type,self.created_at,self.status,self.remarks,)