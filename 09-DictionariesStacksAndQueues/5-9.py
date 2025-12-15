import csv
license_plates = {}
with open('vehicle.txt', 'r') as file:
    text = file.read()
    lines = text.splitlines()
    with open('province.csv','r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header
        
        for row in reader:
            for line in lines:
                if line[:1]  == row[0]:
                    license_plates.update({row[1]: line})



print(license_plates)