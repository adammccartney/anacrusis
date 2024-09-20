#!/usr/bin/python3

__doc__ = """Generate a file containing a lookup table. Each line contains an
item which is a single number corresponding to a value that can be used by the 
pure data patch `lp_noise~` or similar. The values are intended to be used to
lookup the value needed as input to dbtorms object in order that the patch
generates a constant RMS output irrespective of which midi value is requested
for the cutoff of the filter."""


def lookup_dbtorms(mn: int) -> int:
    """Works as a sort of lookup table"""
    if mn >= 0 and mn < 13:
        return 116
    elif mn >= 13 and mn < 25:
        return 112
    elif mn >= 25 and mn < 37:
        return 110
    elif mn >= 37 and mn < 49:
        return 106
    elif mn >= 49 and mn < 61:
        return 104
    elif mn >= 61 and mn < 73:
        return 100
    elif mn >= 73 and mn < 85:
        return 96
    elif mn >= 85 and mn < 97:
        return 94
    elif mn >= 97 and mn < 109:
        return 90
    elif mn >= 109 and mn < 121:
        return 86
    elif mn >= 121:
        return 86
    else:  # I really shouldn't be here!
        return -1


def main():
    vals = [lookup_dbtorms(i) for i in range(0, 132)]
    with open("dbtorms-lookup.txt", "w", encoding="utf-8") as f:
        line = ""
        for v in vals:
            line = line + str(v) + " "
        line = line + ";"
        f.write(line)


if __name__ == '__main__':
    main()
