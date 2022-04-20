import csv
from jproperties import Properties

movies = []
users =[]
bookings=[]
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

        configs = Properties()
        #with open('credentials.properties', 'rb') as write_prop:




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









