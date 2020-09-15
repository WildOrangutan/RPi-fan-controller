def range(valueName, value, min=None, max=None):
    if min!=None and max!=None and min > max:
        raise ValueError("Min value is bigger than max value")
    if min!=None and value<min:
        raise ValueError(f"{valueName} should be smaller than {min}")
    if max!=None and value>max:
        raise ValueError(f"{valueName} should be bigger than {max}")
