def get_input_for_day(day: int, delim=None) -> list[str]:
    f = open("input/day" + str(day) + ".txt")
    if delim is None:
        return [line.strip() for line in f.readlines()]
    else:
        return f.read().split(delim)

def get_int_input_for_day(day: int) -> list[int]:
    f = open("input/day" + str(day) + ".txt")
    return [int(line.strip()) for line in f.readlines()]


def get_input_for_file(file: str, delim=None) -> list[str]:
    f = open("input/" + file + ".txt")
    if delim is None:
        return [line.strip() for line in f.readlines()]
    else:
        return f.read().split(delim)


def get_int_input_for_file(file: str) -> list[int]:
    f = open("input/" + file + ".txt")
    return [int(line.strip()) for line in f.readlines()]


def get_raw_input_for_day(day: int) -> list[str]:
    f = open("input/day" + str(day) + ".txt")
    return [line.strip("\n") for line in f.readlines()]

def get_raw_input_for_file(file: str) -> list[str]:
    f = open("input/" + file + ".txt")
    return [line.strip("\n") for line in f.readlines()]
