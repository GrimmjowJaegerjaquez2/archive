value = input ("Enter your ID: ")
def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str).
    """
    if type(value) != str :
        return False, "ID must be a string."
    x = value.strip()
    if len(value) != 5:
        return False, "Id must be 5 characters long."
    if value[0] != "M" or value[1] != "S":
        return False, "ID must start with 'MS'."
    for i in range (2,5):
        if value[i].isdigit == False:
            return False, "ID must end with three digits."
        else:
            return True, "Valid"

    raise NotImplementedError("validate_id")

print(validate_id(value))