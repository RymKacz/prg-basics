def hotel_list(hotels):
    hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
    ]

    hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
    ]
    if hotels == "hotels_in_Krakow":
        return hotels_in_Krakow
    elif hotels == "hotels_in_Sopot":
        return hotels_in_Sopot
def avg_price(city):
    total_price = 0
    for hotel in hotel_list(city):
        total_price += hotel["price"]
    average = total_price / len(hotel_list(city))
    return average
    if hotels == "hotels_in_Krakow":
        return avg_price(hotels_in_Krakow)
    elif hotels == "hotels_in_Sopot":
        return avg_price(hotels_in_Sopot)
    else:
        return "City not found"
if __name__ == "__main__":
    print(f"Hotels in Krakow: {hotel_list('hotels_in_Krakow')}\n Average price in Krakow: {avg_price('hotels_in_Krakow')}")
    print(f"Hotels in Sopot: {hotel_list('hotels_in_Sopot')}\n Average price in Sopot: {avg_price('hotels_in_Sopot')}")
    print(f"Cheaper hotels in: {'Krakow' if avg_price('hotels_in_Krakow') < avg_price('hotels_in_Sopot') else 'Sopot'}")
