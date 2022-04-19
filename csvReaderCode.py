import csv

movies = []
def writeData(moviedata):
    movies.append(moviedata)
    with open('booking_file.csv', mode='w') as employee_file:
        booking_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

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
    with open('booking_file.csv', mode='w') as employee_file:
        booking_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        booking_writer.writerows(li)

