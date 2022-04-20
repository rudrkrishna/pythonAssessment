import csvReaderCode

class AdminLogin():

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
                self.logout()
                return



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
        userrating="0/10"

        moviedata =[movietitle, genre, length, cast, director, adminrating,
                    language, shows, firstshow, intervaltime, gap, capacity, userrating]

        csvReaderCode.writeData(moviedata)
        self.adminLogin()





    def editMovieInfo(self):
        csvReaderCode.displaymovies()
        print("Edit Movie: ")
        print("----------------------------------------------------")
        moviename = input("Select movie which you want to edit: ")
        li=csvReaderCode.readData(moviename)
        if li == 0:
            self.editMovieInfo()

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

        moviedata = [movietitle, genre, length, cast, director, adminrating,
                     language, shows, firstshow, intervaltime, gap, capacity]

        csvReaderCode.updatecsv(moviedata, csvReaderCode.readmovieindex(moviename))



    def deleteMovies(self):

        print("Delete Movie: ")
        print("----------------------------------------------------")
        deltitle = input("Title of the movie to be deleted: ")
        csvReaderCode.deletemovie(deltitle)

    def logout(self):
        print("Logged out successfully")
        return




