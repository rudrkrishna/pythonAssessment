import csv
from jproperties import Properties

movies = []
users =[]
bookings=[]
booked=[]

def writeData(moviedata):
    movies.append(moviedata)
    with open('booking_file.csv', mode='w') as data_file:
        booking_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range (0, len(movies)) :
            booking_writer.writerow(movies[i])

        print("Movies added succesfully")


def readData(moviename):
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row
            l=l+1
        if l==len(list(csv_reader)):
            print("Movie does not exist")
            return 0

def displaymovies():
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print("Title: "+row[0])

def displaymoviesbyindex():
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i=1
        for row in csv_reader:
            print(str(i)+" "+row[0])
            i=i+1


def readalldata():
    li = []
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            li.append(row)

    return li

def readmovieindex(moviename):
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return l
            else:
                l=l+1



def updatecsv(moviedata, index):

    li = readalldata()
    li[index] = moviedata
    with open('booking_file.csv', mode='w') as booking_file:
        booking_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        booking_writer.writerows(li)

def deletemovie(moviename):
    li = readalldata()
    with open('booking_file.csv', mode='w') as booking_file:
        booking_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0,len(li)):
            if li[i][0]!= moviename:
                booking_writer.writerow(li[i])

        print("Movie deleted Successfully")


def addUsers(userdetails):
    users.append(userdetails)
    with open('userdetails.csv', mode='w') as user_file:
        user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range (0, len(users)) :
            user_writer.writerow(users[i])






    print("Users added successfully")

def readMovieData(index):
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l=0
        index= index-1
        for row in csv_reader:
           if l== index:
               return row
           else:
               l=l+1


def bookingsUpdate(li):

    bookings.append(li)
    with open('bookingdata_file.csv', mode='w') as ticket_file:
        ticket_writer = csv.writer(ticket_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range (0, len(bookings)) :
            ticket_writer.writerow(bookings[i])


def movietimings():
    i=0
    print("Timings: ")
    with open('bookingdata_file.csv') as csv_file:
        ticket_reader = csv.reader(csv_file, delimiter=',')
        for row in ticket_reader:
            print(str(i+1)+". " +row[1])
            i=i+1

def fetchSeats(index):
    with open('bookingdata_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l=0
        index = index-1
        for row in csv_reader:
           if l == index:
               print("Remaining Seats: "+row[2])
               l=l+1
           else:
               l=l+1

def readticketsdata():
    li=[]
    with open('bookingdata_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            li.append(row)
    return li

def bookinghistory(li):
    booked.append(li)
    with open('bookinghistory_file.csv', mode='w') as booking_file:
        booking_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        booking_writer.writerows(booked)

def bookseats(count, index):
    li=readticketsdata()
    if int(li[index-1][2])-count<0:
        print(str(count)+" Number of Tickets Not Available")
        return True
    else:
        booked=[li[index-1][0], li[index-1][1], count]
        bookinghistory(booked)
        li[index-1] = [li[index-1][0], li[index-1][1], int(li[index-1][2])-count]
        with open('bookingdata_file.csv', mode='w') as booking_file:
            booking_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(0, len(li)):
                booking_writer.writerow(li[i])
        return False

def showbookings():
    l=0
    with open('bookinghistory_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(str(l+1)+". Movie Name: "+row[0], end=" - ")
            print("Show Time: "+row[1])
            l=l+1

def updatecanceltickets(index, count):

    time = ""
    li = readticketsdata()
    bookedcount=0
    with open('bookingdata_file.csv') as ticket_file:
        ticket_reader = csv.reader(ticket_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        with open('bookinghistory_file.csv') as booking_file:
            booking_reader = csv.reader(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            l = 0
            for row in booking_reader:
                if l == index-1:
                    time=row[1]
                    bookedcount = int(row[2])
                    l=l+1
                else:
                    l=l+1
        rowindex=0
        for row in ticket_reader:
            if row[1] == time:
                if count > bookedcount:
                    print("You are trying cancel the tickets more than you have booked")
                    print()
                    print()
                    return True
                else:
                    li[rowindex] = [row[0], row[1], int(row[2]) + count]
                    rowindex = rowindex + 1
            else:
                rowindex=rowindex+1

    with open('bookingdata_file.csv', mode='w') as booking_file:
        ticket_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ticket_writer.writerows(li)


def userratingupdate(index, userrating):
    li = readalldata()

    li[index-1][12] = str(userrating)
    with open('booking_file.csv', mode='w') as booking_file:
        booking_writer = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        booking_writer.writerows(li)







