import csvReaderCode

class UserLogin:

    def userLogin(self, user):

        print("----------------------------------------------------")
        print("******Welcome "+ user +" *******")
        csvReaderCode.displaymoviesbyindex()
        i = int(input("Enter Movie: "))
        li = csvReaderCode.readMovieData(i)

        print("Title: "+li[0])
        print("Genre: "+li[1])
        print("Length: "+li[2])
        print("Cast: "+li[3])
        print("Director: "+li[4])
        print("Admin Rating: "+li[5])
        print("Timings: ")
        start = li[8]
        duration = int(li[9].split()[0])  + int(li[2].split()[0])
        hrs=""
        if isinstance(start.split()[2], int):
            hrs = start.split()[0]+" : "+start.split()[2]
        else:
            hrs=start.split()[0]+" : "+"00"


        for i in range(0, int(li[7])):
            time = self.mintohrs(hrs, duration)
            print(i+1, end=". ")
            print(hrs, end=" - ")
            print(time)
            csvReaderCode.bookingsUpdate([li[0], hrs+" - "+time , int(li[11])])
            hrs=self.mintohrs(time, int(li[10].split()[0]))
        print("User Rating: " + li[12])
        self.useractions()


    def useractions(self):

        print("1.  Book Tickets ")
        print("2.  Cancel Tickets ")
        print("3.  Give User Rating ")
        print("4. Logout")
        option = int(input("Enter option: "))

        match option:
            case 1:
                self.bookticket()
            case 2:
                self.cancelticket()
            case 3:
                self.giveuserrating()
            case 4:
                return



    def mintohrs(self, hrs, mins):

        if isinstance(int(hrs.split()[2]), int):
            mins = mins+int(hrs.split()[2])

        hr = int(int(hrs.split()[0]) + mins//60)
        if hr>12:
            hr=hr%12
        mins = mins%60

        return ""+str(hr)+" : "+str(mins)

    def bookticket(self):

        csvReaderCode.movietimings()
        selecttime = int(input("Select Timing: "))
        csvReaderCode.fetchSeats(selecttime)
        count=int(input("Enter Number of Seats: "))

        if csvReaderCode.bookseats(count, selecttime):
            self.bookticket()
        else:
            print("Thanks for booking. ")
            self.useractions()






    def cancelticket(self):
        csvReaderCode.showbookings()
        selectmovie = int(input("Select movie you want to cancel tickets: "))
        cancel = int(input("Number of seats you want to cancel: "))
        if csvReaderCode.updatecanceltickets(selectmovie, cancel):
            self.cancelticket()
        else:
            print("Tickets cancelled Successfully")
        self.useractions()


    def giveuserrating(self):

        csvReaderCode.displaymoviesbyindex()
        i = int(input("Enter Movie: "))
        rating = input("Enter User Rating")
        csvReaderCode.userratingupdate(i, rating)
        print("User rating updated successfully")
        self.useractions()
