with open('it_company.csv', 'r') as file:
    count = 0
    for line in file:
        print(line.strip().split(','))
        if count % 5 == 0:
            input("Press Enter to continue...")
        count += 1
