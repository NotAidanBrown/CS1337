import csv

test_list = []

with open('test.csv', newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        test_list.append(row)

with open ('test.csv', newline="") as file:
    writer = csv.write(file)
    writer.writerows(test_list[row])