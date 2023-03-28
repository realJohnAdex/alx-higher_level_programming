#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    value = 0
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except IndexError:
            value = 0
            print("out of range")
            continue
        except ZeroDivisionError as err:
            value = 0
            print("division by 0")
            continue
        except (TypeError, ValueError):
            value = 0
            print("wrong type")
            continue
        finally:
            new_list.append(value)
    return (new_list)
