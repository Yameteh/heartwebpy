

def equals(s,d):
    return s == d

def equals_ingorecase(s,d):
    try:
        return s.upper() == d.upper()
    except AttributeError:
        return s == d


def unicode2str(u_str):
    return u_str.encode('unicode-escape').decode('string_escape')
