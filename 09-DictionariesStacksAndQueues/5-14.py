queue = {}
input_customer = input("Podaj nazwę klienta do dodania do kolejki: ")
add_customer = queue.update({input_customer: queue.__len__()})
print("Aktualna kolejka klientów:", queue)