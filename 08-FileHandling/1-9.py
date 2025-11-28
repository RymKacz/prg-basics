###
# Prints employees employed in a specified position.
#

# Employee List


# Position
job_title = 'Software Engineer'
i =1 
with open("it_company.csv") as file:
    debile= file.read()
    linesfiles = debile.splitlines()
    for line in linesfiles:
      if job_title in line:
         print (f"{i}. {line}")
         i+=1