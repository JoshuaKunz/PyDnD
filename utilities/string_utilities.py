# Ternary line assigns a value in a single line with an if else statement
def write_positive(num):
    output = write_positive(num) if num >=0 else str(num)
    return output

def write_percent(num):
    output = str(num) + "%"
    return output