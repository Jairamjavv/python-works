def zero(f1=0):
    if f1:
        return eval(f"0{f1}")
    else:
        return "0"


def one(f1=0):
    if f1:
        return eval(f"1{f1}")
    else:
        return "1"


def two(f1=0):
    if f1:
        return eval(f"2{f1}")
    else:
        return "2"


def three(f1=0):
    if f1:
        return eval(f"3{f1}")
    else:
        return "3"


def four(f1=0):
    if f1:
        return eval(f"4{f1}")
    else:
        return "4"


def five(f1=0):
    if f1:
        return eval(f"5{f1}")
    else:
        return "5"


def six(f1=0):
    if f1:
        return eval(f"6{f1}")
    else:
        return "6"


def seven(f1=0):
    if f1:
        return eval(f"7{f1}")
    else:
        return "7"


def eight(f1=0):
    if f1:
        return eval(f"8{f1}")
    else:
        return "8"


def nine(f1=0):
    if f1:
        return eval(f"9{f1}")
    else:
        return "9"


def plus(num=0):
    return f"+{num}"


def minus(num=0):
    return f"-{num}"


def times(num=0):
    return f"*{num}"


def divided_by(num=0):
    return f"//{num}"


print(nine(divided_by(three())))
