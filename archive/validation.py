from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
    if type(value) != str:
        return False
    if value[0,2] != "MS" or type(value[2, 5]) != int:
        return False
    else:
        return True
    raise NotImplementedError("validate_id")


def validate_title(value):
    stripped_value = strip(value)
    if type(stripped_value) != str:
        return False
    if len(stripped_value) < 3:
        return False
    else:
        return True
    raise NotImplementedError("validate_title")


def validate_city(value):
    if type(value) != str:
        return False
    if value not in KNOWN_CITIES:
        return False
    else:
        return True
    raise NotImplementedError("validate_city")


def validate_year(value):
    if type(value) != int:
        return False
    if value not in range(MIN_YEAR, MAX_YEAR + 1):
        return False
    else:
        return True
    raise NotImplementedError("validate_year")


def validate_condition(value):
    if type(value) != str:
        return False
    if value not in VALID_CONDITIONS:
        return False
    else:
        return True
    raise NotImplementedError("validate_condition")


def validate_record(record):

    raise NotImplementedError("validate_record")
