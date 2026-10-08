import MAX_YEAR
import KNOWN_CITIES


def count_before(records, year):
    count = 0
    for record in records:
        if records["year"] < year:
            count += 1
    
    return count

def find_by_city(records, city):
    input(city)
    if city not in KNOWN_CITIES:
        return False
    

def oldest(records):
    for records in records:
        if record["year"] =< MAX_YEAR:
            MAX_YEAR == record.year

    return MAX_YEAR


def cities_summary(records):

    city_counts = int([count1, count2, count3, count4, count5,])
    
    for record in records:
        if record["city"] in KNOWN_CITIES:
            for i in range(0, 6):
                if record["city"] == KNOWN_CITIES[i]:
                    city_counts[i] += 1

                for city in KNOWN_CITIES:
                    City_Summary = {}
                    City_Summary[f"{city}"] = city_counts[i]



        
    
