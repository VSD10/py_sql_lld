

class movie:
    def __init__(self,movie_id,title,genre,release_year,budget,director_id):    
        self.movie_id=movie_id
        self.title=title
        self.genre=genre
        self.release_year=release_year
        self.budget=budget
        self.director_id=director_id
    
    def to_tuple(self):
        return (self.title,self.genre,self.release_year,self.budget,self.director_id)