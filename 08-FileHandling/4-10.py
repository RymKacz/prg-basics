import csv
with open('clothing.csv', mode ='r', newline='')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)

  # displaying the contents of the CSV file
  for lines in csvFile:
        if lines[5] < '60' and lines[6] < '40':
            print(lines)