###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as employees:
    employee_lines = employees.read().splitlines()
    with open(position_file, 'w') as position:
      for line in employee_lines:
         if job_title in line:
            position.write(line + '\n')