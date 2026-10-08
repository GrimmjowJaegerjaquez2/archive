from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
    if type(value) != str:
        return False, "Invalid ID"
    if value[0: 2] != "MS" or not value[2: 5].isdigit():
        return False, "Invalid ID"
    else:
        return True, "Valid ID"




def validate_title(value):
    if type(value) != str:
        return False
    x = value.strip()
    for i in range(0, len(x)):
        if (not value[i].isalpha()) or value[i] != " " or value[i] != "-":
            return False
    

def validate_city(value):
    if type(value) != str:
        return False, "Invalid City"
    if value not in KNOWN_CITIES:
        return False, "Invalid City"
    else:
        return True, "Valid"
    


def validate_year(value):
    if  not value.isdigit():
        return False, "Invalid Year"
    if int(value) not in range(MIN_YEAR, MAX_YEAR + 1):
        return False, "Invalid Year"
    else:
        return True, "Valid Year"
    


def validate_condition(value):
    if type(value) != str:
        return False, "Invalid Condition"
    if value not in VALID_CONDITIONS
        return True, "Valid"
    else:
        return False, "Invalid Condition"


def validate_record(record):
    errors = []
    validators [
        validate_
    ]