import csvReaderCode


class UserLogin:
    def userLogin(self, user):

        print("----------------------------------------------------")
        print("******Welcome "+ user +"*******")
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
        print("User Rating: "+li[12])
        print("1.  Book Tickets ")
        print("2.  Cancel Tickets ")
        print("3.  Give User Rating ")
        option = int(input("Enter option: "))

        match option:
            case 1:
                self.bookticket()
            case 2:
                self.cancelticket()
            case 3:
                self.giveuserrating()



    def mintohrs(self, hrs, mins):
        if isinstance(int(hrs.split()[2]), int):
            mins = mins+int(hrs.split()[2])

        hr = int(int(hrs.split()[0]) + mins//60)
        if hr>12:
            hr=hr%12
        mins = mins%60

        return ""+str(hr)+" : "+str(mins)

    def bookticket(self):



    def cancelticket(self):


    def giveuserrating(self):
