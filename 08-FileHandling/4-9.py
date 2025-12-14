### Convenient processing of CSV documents is possible using the CSV module. Find on the Internet how to use this module. Then write a program that, based on the it_company.csv file, prints the first name, last name and email (in the given order, without Job Title) of people employed in the position of 'Graphic Designer'.
import csv
with open('it_company.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        if row[2] == 'Graphic Designer':  
            first_name = row[1]  
            last_name = row[0]  
            email = row[3]      
            print(f"{first_name} {last_name} {email}")
        