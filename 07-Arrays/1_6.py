###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= n <= 7:
        return weekdays[n - 1]
    else:
        return "Invalid day number"
x=int(input("Enter day number (1-7): "))
print(weekday(x))