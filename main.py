"""
format for players
    nick 1 (defender)
        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

    nick 2 (defender)
        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]


"""

# create list of players who send S.O.S
# txt to csv (delete BB-code, defenders, wall, pop-lvl)
# make data form csv (list of attacks)
# how many attacks from village - list of dict [{xxx|xxx: X},{xxx|xxx: X}]
# calculate distance
# calculate travel time
# seconds to datetime
# calculate when sent
# sort by sent datetime
# list of villages with attacks
# todo


from txt_to_csv import txt_to_csv
import data_connection
import change_data_form
import logic

TYP_ATTACK = 0
ATTACKER_VILLAGE_CORDS = 1
DATE_AND_TIME = 2
ATTACKER_NICK = 3
DEFENDER_VILLAGE_CORDS = 4
DEFENDER_NICK = 5
WHEN_SENT = 6
DISTANCE = 7
HOW_MANY_ATTACKS = 8


def main():
    """

    """
    players_list = logic.get_players_list("data/txt/")
    txt_to_csv(players_list)
    data = data_connection.read_file(players_list)
    list_of_attacks = change_data_form.change_format_to_list_of_list(data)
    dict_attacks_from_village = logic.get_how_many_attacks_from_attacker_village(list_of_attacks)

    sorted_list_of_attacks = logic.add_sent_time_and_sort_by_this(dict_attacks_from_village, list_of_attacks)
    list_of_attack_sorted_by_sent_time = logic.add_information_send_no(sorted_list_of_attacks)
    list_of_attack_sorted_by_end_time = logic.sort_by_date(list_of_attack_sorted_by_sent_time, DATE_AND_TIME)
    sos_format = logic.get_sorted_attacks_by_nickname_and_villages_and_sent_time(list_of_attack_sorted_by_end_time)
    data_connection.write_attacks_by_sent_time(list_of_attack_sorted_by_sent_time)
    data_connection.write_in_sos_format(list_of_attack_sorted_by_end_time, players_list, sos_format)


if __name__ == '__main__':
    main()
