test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]
passed = list(filter(lambda r: r["result"]>=50, test_results))
print("Students who passed the test: ",", ".join(map(lambda r: r["name"], passed)))