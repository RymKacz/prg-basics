# The file books.csv contains a list of books. Write a program that copies the book data from a given genre to its corresponding file. Use functions to divide the program into logical parts.

#Genre --> Filename
#Fantasy --> books_fantasy.txt
#Historical --> books_historical.txt
#Romance --> books_romance.txt
#Classic --> books_classic.txt  

import csv

with open('books.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    genre_files = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    for row in reader:
        if row[2] == 'Fantasy':
            with open(genre_files['Fantasy'], mode='a') as fantasy_file:
                fantasy_file.write(','.join(row) + '\n')
        elif row[2] == 'Historical':
            with open(genre_files['Historical'], mode='a') as historical_file:
                historical_file.write(','.join(row) + '\n')
        elif row[2] == 'Romance':
            with open(genre_files['Romance'], mode='a') as romance_file:
                romance_file.write(','.join(row) + '\n')
        elif row[2] == 'Classic':
            with open(genre_files['Classic'], mode='a') as classic_file:
                classic_file.write(','.join(row) + '\n')