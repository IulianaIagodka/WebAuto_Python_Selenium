def increment_string(strng):
    one = 1
    end = strng[-1]
    if end.isnumeric():
        end += 1
        strng[-1] = str(end)
    else:
        strng = strng + str(one)

    return strng
