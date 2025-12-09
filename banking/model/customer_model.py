class customer_model():
    def __init__(self,n,e,p):
        self.name=n
        self.email=e
        self.phone=p
    
    def to_tuple(self):
        return (self.name,self.email,self.phone)
