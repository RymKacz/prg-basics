def f(firstname,lastname,age):
    if age < 18:
        return f"{firstname[0].lower()}{lastname[0].lower()}{age}"
    else:
        return f"{firstname[0].upper()}{lastname[0].upper()}{age}"
print(f("John","May",18))
print(f("Anna","Brown",17))