def find_common_participants(group1, group2, sep=','):
    list1 = group1.split(sep)
    list2 = group2.split(sep)

    result = []

    for person in list1:
        if person in list2:
            if person not in result:
                result.append(person)

    result.sort()
    return result
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, sep='|')
print(result)