def f(fnc,res):
   filtering =  list(filter(fnc,res))
   return max(filtering) - min(filtering)
res = [95,90,20,50,70]
fnc1 = lambda x: x > 50
print(f(fnc1,res))
fnc2 = lambda x: x>30 and x < 90
print(f(fnc2,res))