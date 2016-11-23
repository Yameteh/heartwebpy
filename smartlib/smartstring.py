

def equals(s,d):
    return s == d

def equals_ingorecase(s,d):
    try:
        return s.upper() == d.upper()
    except AttributeError:
        return s == d