class castings:
    def __init__(self,movie_id,actor_name,role_name,salary,status):
        self.movie_id=movie_id
        self.actor_name=actor_name
        self.role_name=role_name
        self.salary=salary
        self.status=status
    
    def to_tuple(self):
        return (self.movie_id,self.actor_name,self.role_name,self.salary,self.status)
