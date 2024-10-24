#!/usr/bin/python3
if __name__ == "__main__":
    import sys
   def adding_argument():
       sum = ""
       for i in sys.argv[1:]:
           sum += int(i)
           print(sum)
adding_argument()
