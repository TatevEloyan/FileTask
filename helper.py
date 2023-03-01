def replace_values_and_return_list(list, dic):
    for k in dic.keys():
        for i in range(len(list)):
            s = list[i].replace(k, dic.get(k))
            list[i] = s
    return list


def count_changes_and_print_sorted_list(list1, list2):
    dic = {}
    for k in range(len(list1)):
        change_count = 0
        s = zip(list1[k], list2[k])
        for i, j in s:
            if i != j:
                change_count += 1
        dic[list2[k]] = change_count
    sorted_dic = sorted(dic, key=dic.get, reverse=True)
    print(sorted_dic)