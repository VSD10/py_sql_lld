from service.casting_service import casting_service
from service.director_service import director_service
from service.movie_service import movie_service

class main:
    def st():
        ds = director_service()
        ms = movie_service()
        cs = casting_service()

        while True:
            v='''
1. Add Director
2. Add Movie
3. Add Casting (Actor → Movie)
4. Update Movie Director
5. View All Movies (JOIN)
6. View Cast of a Movie (JOIN)
7. Complete Casting
8. Exit'''
            print(v)
            choice=int(input("Enter your choice: "))
            if choice==1:
                ds.add_director()
            elif choice==2:
                ms.add_movie()
            elif choice==3:
                cs.add_cast()
            elif choice==4:
                ms.update_movie_director()
            elif choice==5:
                ms.view_movies()
            elif choice==6:
                cs.view_cast()
                
            elif choice==7:
                cs.update_cast()
            elif choice==8:
                return
            else:
                print("enter a valid choice 1-8")

main.st()