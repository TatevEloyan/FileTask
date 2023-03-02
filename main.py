from file_reader import read_file_info_list, read_file_into_dictionary
from helper import replace_values_and_return_list, count_changes_and_print_sorted_list

if __name__ == '__main__':
    list = read_file_info_list('files/text')
    list1 = read_file_info_list('files/text')
    dic = read_file_into_dictionary('files/config')
    list2 = replace_values_and_return_list(list1, dic)
    count_changes_and_print_sorted_list(list, list2)
