arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
print(list(map(lambda x: x[0].upper()+", "+x[1], arr)))
