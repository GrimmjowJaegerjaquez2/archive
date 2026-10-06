"""Questions we ask the Archive.

YOU IMPLEMENT THIS FILE.

Every function here takes `records` — a list of record dicts as produced by
load_archive — and answers one question about the collection. None of them
touch a file. None of them print anything. They return values.

Keep in mind from Week 2: the structure you are given decides which of these
is cheap and which is expensive. All of these are linear scans over a list.
Note in your README which one would be instant with a dictionary instead.
"""


def count_before(records, year):
    """How many manuscripts were written strictly BEFORE `year`?

    `year` is an int. Record years may be strings from the file — convert.

    Returns int.
    """



def find_by_city(records, city):
    input(city)
    if city not in KNOWN_CITIES:
        return False
    
    raise NotImplementedError("find_by_city")


def oldest(records):
    """The record with the smallest year.

    An empty list returns None — not an error, not a crash. Deciding what
    "the oldest of nothing" means is your job, and the answer is None.

    If two records tie on year, return the one that appears FIRST.

    Returns dict or None.
    """
 


def cities_summary(records):
    """How many manuscripts come from each city?

    Returns a dict mapping city name to count. A city with zero manuscripts
    does not appear as a key at all — do not pre-fill from KNOWN_CITIES.

    Use the city spelling exactly as it appears in the records.

    Returns dict.
    """
    city_counts = int([count1, count2, count3, count4, count5,])
    
    for record in records:
        if record["city"] in KNOWN_CITIES:
            for i in range(0, 6):
                if record["city"] == KNOWN_CITIES[i]:
                    city_counts[i] += 1

                for city in KNOWN_CITIES:
                    City_Summary = {}
                    City_Summary[f"{city}"] = city_counts[i]



        
    
