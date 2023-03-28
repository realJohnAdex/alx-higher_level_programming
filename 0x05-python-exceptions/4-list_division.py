#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    value = 0
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
            new_list.append(value)
        except IndexError:
            new_list.append(0)
            print("out of range")
            continue
        except ZeroDivisionError as err:
            new_list.append(0)
            print("division by 0")
            continue
        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")
            continue
    return (new_list)
