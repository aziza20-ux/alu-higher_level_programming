#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    total_sum = 0
    i = 1
    if length == 0:
        print("{}".format(total_sum))
    else:
        while i <= length:
            total_sum += int(argv[i])
            i += 1
        print(total_sum)
