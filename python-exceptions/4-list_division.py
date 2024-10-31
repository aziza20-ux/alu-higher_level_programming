#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:

        for i in range(list_length):
            if (i >= len(my_list_1) or i >= len(my_list_2)):
                print("out of range")
                new_list.append(0)
                continue
            if not (isinstance(my_list_1(i), (integer,float)) and (isinstance(my_list_2(i),(integer,float)):
                print("wrong type")
                new_list.append(0)
                continue
        mun1 = my_list_1[i]
            mun2 = my_list_2[i]
        if num2 == 0:
            print("division by zero")
            new_list.append(0)
            continue
        new_list.append(mun1/num2)
    except exception as e:
        new_list.append(0)
      return new_list
