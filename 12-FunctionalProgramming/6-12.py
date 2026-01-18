arr = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]
morethan10 = list(filter(lambda x: x["gold"] + x["silver"] + x["bronze"] > 10, arr))
print("Countries with more than 10 medals: ",", ".join(map(lambda x: x["country"], morethan10)),": " , "".join(list(map(lambda x: str(x["gold"]) + ", " + str(x["silver"]) + ", " + str(x["bronze"]), morethan10))))