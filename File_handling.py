import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)

#########################################################################

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

######################################################################################

f = open('fileName.txt', 'r')
f.read()

f1 = open('fileName1.txt', 'w')
f1.write('something')
for data in f: # writes all data from f into f1
    f1.write(data)


f = open('fileName1.txt', 'a')
f.write('something more')

# modes of operation, r, w, a, rb, wb. rb and wb is to read and write binary.//
