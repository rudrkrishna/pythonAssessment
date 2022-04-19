import csv

movies = []
def writeData(moviedata):
    movies.append(moviedata)
    with open('booking_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range (0, len(movies)) :
            employee_writer.writerow(movies[i])

        print("Movies added succesfully")


def readData():
    with open('booking_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

            line_count += 1

readData()