def find_common_participants(group1, group2, separator=","):
    list_group1 = group1.split(separator)
    list_group2 = group2.split(separator)

    common_participants = []
    for participant in list_group1:
        if participant in list_group2 and participant not in common_participants:
            common_participants.append(participant)

    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common_participants)