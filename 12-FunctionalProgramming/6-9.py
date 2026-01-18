arr = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
pos = list(filter(lambda x: x[1]>0,arr.items()))
print("Cities with positive temperatures: ",", ".join(map(lambda x: x[0],pos)))
