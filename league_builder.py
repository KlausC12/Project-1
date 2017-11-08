import random
import csv


def exp_sorter(players):    # sorts players into two lists - experience vs no experience
    for row in players:
        if row['Soccer Experience'] == 'YES':
            has_exp.append(row)
        else:
            no_exp.append(row)


def team_builder(players1, players2):    # appends equal number players from exp/no exp to team list
    team = random.sample(has_exp, 3) + random.sample(no_exp, 3)    # chooses players randomly
    for player in team:
        if player in players1:    # removes randomly chosen players from player lists
            players1.remove(player)
        elif player in players2:
            players2.remove(player)
    return team


def team_list(*teams):    # accepts final team lists and writes them to txt file
    with open('teams.txt', 'w') as file:
        count = 0
        for team in teams:
            file.write(team_names[count] + '\n')
            file.write('----------' + '\n')
            for player in team:
                file.write('{Name}, {Soccer Experience}, {Guardian Name(s)}\n'.format(**player))
            file.write('\n\n')
            count += 1


def letter_info(*teams):     # include team name, deal with name append issue
    name_list = []
    for team in teams:
        for player in team:
            name_list.append([player['Name'].lower(), player])
    for player in name_list:
        player[0] = player[0].split()
        player[0] = '_'.join(player[0]) + '.txt'
        letter_list.append(player)


def intro_letter(names):
    for player in names:
        with open(player[0], 'w') as file:
            file.write('Dear Mr. and/or Mrs. ' + player[1]['Guardian Name(s)'] + ',\n\n')
            file.write('Your child, ' + player[1]['Name'] + ' has been placed on the '


                       )


if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvfile:    # opens and obtains csvfile data for each player
        filereader = csv.DictReader(csvfile)

        player_list = list(filereader)

    team_names = ['Dragons', 'Raptors', 'Sharks']

    has_exp = []
    no_exp = []

    exp_sorter(player_list)

    dragons = team_builder(has_exp, no_exp)
    raptors = team_builder(has_exp, no_exp)
    sharks = team_builder(has_exp, no_exp)

    team_list(dragons, raptors, sharks)

    letter_list = []
    letter_info(dragons, raptors, sharks)

    intro_letter(letter_list)





