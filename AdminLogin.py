import csvReaderCode
class AdminLogin:

    def adminLogin(self):
        print("******Welcome Admin*******")
        print("1. Add New Movie Info")
        print("2. Edit Movie Info")
        print("3. Delete Movies")
        print("4. Logout")
        inputOption = int(input("Enter Option: "))

        match inputOption:
            case 1:
                self.addNewMovie()
            case 2:
                self.editMovieInfo()
            case 3:
                self.deleteMovies()
            case 4:
                print()


    def addNewMovie(self):
        print("Add new Movie: ")
        print("----------------------------------------------------")
        movietitle = input("Title: ")
        genre = input("Genre: ")
        length = input("Length: ")
        cast = input("Cast: ")
        director = input("Director: ")
        adminrating = input("Admin Rating: ")
        language = input("Language: ")
        print("Timings:")
        print("----------------------------------------------------")
        shows = int(input("Number of Shows in a day: "))
        firstshow = input("First Show: ")
        intervaltime = input("Interval Time: ")
        gap = input("Gap Between Shows: ")
        capacity = int(input("Capacity: "))

        moviedata =[movietitle, genre, length, cast, director, adminrating,
                    language, shows, firstshow, intervaltime, gap, capacity]

        csvReaderCode.writeData(moviedata)
        self.adminLogin()





    def editMovieInfo(self):
        print("Edit Movie: ")
        print("----------------------------------------------------")
        moviename = input("Select movie which you want to edit: ")




    def deleteMovies(self):
        print("Delete Movie: ")
        print("----------------------------------------------------")
        deltitle = input("Title of the movie to be deleted: ")


