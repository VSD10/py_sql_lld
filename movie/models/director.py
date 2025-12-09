class director:
    def __init__(self,name,email,experience,status):
        self.name=name
        self.email=email
        self.experience=experience
        self.status=status
    
    def to_tuple(self):
        return (self.name,self.email,self.experience,self.status)