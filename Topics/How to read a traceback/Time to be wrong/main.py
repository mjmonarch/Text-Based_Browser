def print_list(some_list):
    for i in range(len(some_list)):
        if int(some_list[i]) % 2 == 0:
            print(some_list[i])
        if int(some_list[i]) % 3 == 0:
            print(int(some_list[i]) % 3)
        i += 1
