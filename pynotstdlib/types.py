def _test_type(ty, val):
    try:
        ty(val)
        return True
    except TypeError:
        return False


def is_float(num, strict = True):
    return is_float_strict(num) if strict else _test_type(float, num)


def is_int(num, strict = True):
    return is_int_strict(num) if strict else _test_type(int, num)


def is_bool(num, strict = True):
    return is_bool_strict(num) if strict else num in [True, False] or is_int(num) and num in [0, 1]


def is_float_strict(num):
    return _test_type(float, num) and is_int(num) and str(int(num)) == str(float(num))


def is_int_strict(num):
    return _test_type(int, num) and str(num) == str(int(num))


def is_bool_strict(num):
    return num in [True, False]


def safe_convert(val, to: type):
    def convert_type(type1: str, type2: str):
        if type2 is None or type2 == "":
            # If the column type has not been set yet, always valid!
            return True
        if type1 == type2:
            # If the two types match, great!
            return True
        elif type1 == "int" and type2 == "float":
            # Able to cast an int to a float
            return True
        elif type1 == "int" and type2 == "date":
            # Able to cast an int to a date (conditionally)
            return True
        elif is_bool(val, strict = False) and type2 == "bool":
            return True
        else:
            # Should be able to cast anything to string.
            return type2 == "str"

    dest_type = type(val).__name__
    target_type = to.__name__
    can_convert = convert_type(type1 = dest_type,
                               type2 = target_type)
    if not can_convert:
        raise TypeError("Incompatible types: {0} -> {1}".format(dest_type, target_type))
    else:
        return to(val)
