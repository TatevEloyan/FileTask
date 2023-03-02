def read_file_info_list(file_name):
    with open(file_name) as file:
        data = file.read()

    data_list = data.replace('\n', ' ').split(" ")
    return data_list


def read_file_into_dictionary(file_name):
    dic = {}
    with open(file_name) as file:
        for line in file:
            (key, val) = line.split()
            dic[(key)] = val
    return dic
