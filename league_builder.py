import random
import csv
from datetime import date, timedelta


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


def letter_info(*teams):    # gathers player data, team name, creates txt file for use in intro letter
    name_list = []
    for team in teams:
        for player in team:    # updates team names to player data
            if player in dragons:
                player.update({'Team': 'Dragons'})
            elif player in raptors:
                player.update({'Team': 'Raptors'})
            elif player in sharks:
                player.update({'Team': 'Sharks'})

        for player in team:
            for item in player.items():    # includes name for txt file and player data
                if item[0] == 'Name':
                    name_list.append([item[1].lower(), player])

    for player in name_list:    # creates txt file based on player name
        player[0] = player[0].split()
        player[0] = '_'.join(player[0]) + '.txt'
        letter_list.append(player)


def letter_writer(names):   # creates a new txt file for each player on the roster
    for player in names:
        with open(player[0], 'w') as file:
            file.write('Dear Mr. and/or Mrs. ' + player[1]['Guardian Name(s)'] + ',\n\n')
            file.write('Your child, ' + player[1]['Name'] + ', will be playing for the ' + player[1]['Team']
                       + ' soccer team in the upcoming season.\n')
            file.write('The first team practice will be one week from now on '
                       + (current_date + week).strftime("%A %d, %B %Y") + ' at 4:00 pm.\n')

            first_name = player[1]['Name'].split()
            first_name = first_name[0]

            file.write('Good luck to ' + first_name + ' this year!\n\n--Youth Soccer League--')


if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvfile:    # opens and obtains csvfile data for each player
        filereader = csv.DictReader(csvfile)

        player_list = list(filereader)

    team_names = ['Dragons', 'Raptors', 'Sharks']
    has_exp = []
    no_exp = []

    exp_sorter(player_list)    # sort players

    dragons = team_builder(has_exp, no_exp)    # build teams
    raptors = team_builder(has_exp, no_exp)
    sharks = team_builder(has_exp, no_exp)

    team_list(dragons, raptors, sharks)    # create team file

    letter_list = []
    current_date = date.today()
    week = timedelta(days=7)

    letter_info(dragons, raptors, sharks)    # gather info
    letter_writer(letter_list)    # write letters
