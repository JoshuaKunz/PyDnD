# Ternary line assigns a value in a single line with an if else statement
def write_positive(num):
    output = num if num <=0 else "+" + str(num)
    return output

def write_percent(num):
    output = str(num) + "%"
    return output

def write_pounds(num):
    output = str(num) + '#'
    return output

def nth(num):
    if num == 0:
        return str(num)
    elif num == 1:
        return str(num) + 'st'
    elif num == 2:
        return str(num) + 'nd'
    elif num == 3:
        return str(num) + 'rd'
    else:
        return str(num) + 'th'
    