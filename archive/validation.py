"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
    if type(value) != str:
        return False, "Invalid ID"
    if value[0, 2] != "MS" or type(value[2, 5]) != int:
        return False, "Invalid ID"
    else:
        return True, "Valid ID"
    raise NotImplementedError("validate_id")


def validate_title(value):
    if type(value) != str:
        return False
    x = value.strip()
    for i in range(0, len(x)):
        if type(value[i]) != str:
            if value[i] != " " or value[i] != "-":
                return False
    raise NotImplementedError("validate_title")

def validate_city(value):
    if type(value) != str:
        return False, "Invalid City"
    if value not in KNOWN_CITIES:
        return False, "Invalid City"
    else:
        return True, "Valid"
    raise NotImplementedError("validate_city")


def validate_year(value):
    if type(value) != int:
        return False, "Invalid Year"
    if value not in range(MIN_YEAR, MAX_YEAR + 1):
        return False, "Invalid Year"
    else:
        return True, "Valid Year"
    raise NotImplementedError("validate_year")


def validate_condition(value):
    if type(value) != str:
        return False, "Invalid Condition"
    if value == "fragile" ^ value == "fair" ^ value == "good":
        return True, "Valid"
    else:
        return False, "Invalid Condition"
    raise NotImplementedError("validate_condition")


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    raise NotImplementedError("validate_record")
