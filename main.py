import random
import time
import os

board = list('''
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║   Visiting   ║     Pall     ║   Electric   ║              ║  Northumlr'd ║  Marylebone  ║     Bow      ║   Community  ║  Marlborough ║     Vine     ║     Free     ║
║     Jail     ║     Mall     ║   Company    ║   Whitehall  ║    Avenue    ║    Station   ║    Street    ║     Chest    ║    Street    ║    Street    ║    Parking   ║
║      👮      ║   🟣 $140    ║   💡 $150    ║    🟣 $140   ║    🟣 $160   ║    🚂 $200   ║   🟠 $180    ║      🗝️      ║   🟠 $180    ║   🟠 $200    ║      🚗      ║
║              ║              ║              ║              ║              ║              ║              ║              ║              ║              ║              ║
║══════════════║══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║══════════════║
║  Pentonville ║                                                                                                                                      ║              ║
║     Road     ║                                                                                                                                      ║    Strand    ║
║   🟤 $100    ║                                                                                                                                      ║   🔴 $220    ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║    Euston    ║                                                                                                                                      ║              ║
║     Road     ║                                                                                                                                      ║    Chance    ║
║   🟤 $100    ║                                                                                                                                      ║      ❓      ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║              ║                                                                                                                                      ║    Fleet     ║
║    Chance    ║                                                                                                                                      ║    Street    ║
║      ❓      ║                                                                                                                                      ║   🔴 $220    ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║   The Angel  ║                                                                                                                                      ║   Trafalgar  ║
║   Islington  ║                                                                                                                                      ║     Square   ║
║    🟤 $100   ║                                                                                                                                      ║    🔴 $240   ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║  Kings Cross ║                                                                                                                                      ║ Fenchurch St.║
║    Station   ║                                                                                                                                      ║    Station   ║
║    🚂 $200   ║                                                                                                                                      ║    🚂 $200   ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║    Income    ║                                                                                                                                      ║   Leicester  ║
║     Tax      ║                                                                                                                                      ║    Square    ║
║   💰 $200    ║                                                                                                                                      ║   🟡 $260M   ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║  Whitechapel ║                                                                                                                                      ║   Coventry   ║
║     Road     ║                                                                                                                                      ║    Street    ║
║    ⚪ $60    ║                                                                                                                                      ║   🟡 $260M   ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║   Community  ║                                                                                                                                      ║     Water    ║
║     Chest    ║                                                                                                                                      ║     Works    ║
║      🗝️      ║                                                                                                                                      ║    🚰 $150   ║
║              ║                                                                                                                                      ║              ║
║══════════════║                                                                                                                                      ║══════════════║
║   Old Kent   ║                                                                                                                                      ║              ║
║     Road     ║                                                                                                                                      ║  Piccadilly  ║
║    ⚪ $60    ║                                                                                                                                      ║    🟡 $280M  ║
║              ║                                                                                                                                      ║              ║
║══════════════║══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║══════════════║
║      GO      ║              ║    Super     ║     Park     ║              ║ Liverpool St.║     Bond     ║   Community  ║    Oxford    ║    Regent    ║    Go To     ║
║ Collect $200 ║    Mayfair   ║     Tax      ║     Lane     ║    Chance    ║    Station   ║    Street    ║     Chest    ║    Street    ║    Street    ║     Jail     ║
║              ║    🔵 $400   ║   💰 $100    ║    🔵 $350   ║      ❓      ║    🚂 $200   ║   🟢 $320    ║      🗝️      ║   🟢 $300    ║   🟢 $300    ║     👮       ║
║              ║              ║              ║              ║              ║              ║              ║              ║              ║              ║              ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
''')
for i in range(len(board)):
    if ''.join(board[i: i + 16]) == '║              ║':
        board[i: i + 16] = ['║', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '║']

player_count = int(input('Enter number of players (2-6)'))
player_data = [{'name': 'player1', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''},
               {'name': 'player2', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''},
               {'name': 'player3', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''},
               {'name': 'player4', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''},
               {'name': 'player5', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''},
               {'name': 'player6', 'credit': 1500, 'pos': -1, 'railways': 0, 'utilities': 0, 'sprite': ''}][:player_count]
property_data = [{'name': 'Old Kent Road', 'type': 'property', 'cost': 60, 'rent': 10, 'index': 7933, 'owner': ''},
                 {'name': 'Community Chest', 'type': 'community chest', 'cost': 0, 'rent': 0, 'index': 7121,
                  'owner': ''},
                 {'name': 'Whitechapel Road', 'type': 'property', 'cost': 60, 'rent': 20, 'index': 6301, 'owner': ''},
                 {'name': 'Income Tax', 'type': 'tax', 'cost': 200, 'rent': 0, 'index': 5482, 'owner': ''},
                 {'name': 'Kings Cross Station', 'type': 'station', 'cost': 200, 'rent': 25, 'index': 4663,
                  'owner': ''},
                 {'name': 'The Angel Islington', 'type': 'property', 'cost': 100, 'rent': 30, 'index': 3844,
                  'owner': ''},
                 {'name': 'Chance', 'type': 'chance', 'cost': 0, 'rent': 0, 'index': 3025, 'owner': ''},
                 {'name': 'Euston Road', 'type': 'property', 'cost': 100, 'rent': 30, 'index': 2213, 'owner': ''},
                 {'name': 'Pentoville Road', 'type': 'property', 'cost': 100, 'rent': 40, 'index': 1401, 'owner': ''},
                 {'name': 'Visting Jail', 'type': 'Just visiting jail', 'cost': 0, 'rent': 0, 'index': 652, 'owner': ''},
                 {'name': 'Pall Mall', 'type': 'property', 'cost': 140, 'rent': 50, 'index': 660, 'owner': ''},
                 {'name': 'Electric Company', 'type': 'utility', 'cost': 150, 'rent': 4, 'index': 668, 'owner': ''},
                 {'name': 'Whitehall', 'type': 'property', 'cost': 140, 'rent': 50, 'index': 676, 'owner': ''},
                 {'name': 'Northumberland  Avenue', 'type': 'property', 'cost': 160, 'rent': 60, 'index': 684,
                  'owner': ''},
                 {'name': 'Marylebone Station', 'type': 'station', 'cost': 200, 'rent': 25, 'index': 692, 'owner': ''},
                 {'name': 'Bow Street', 'type': 'property', 'cost': 180, 'rent': 70, 'index': 700, 'owner': ''},
                 {'name': 'Community Chest', 'type': 'community chest', 'cost': 0, 'rent': 0, 'index': 708,
                  'owner': ''},
                 {'name': 'Marlborough Street', 'type': 'property', 'cost': 180, 'rent': 70, 'index': 716,
                  'owner': ''},
                 {'name': 'Vine Street', 'type': 'property', 'cost': 200, 'rent': 80, 'index': 724, 'owner': ''},
                 {'name': 'Free parking', 'type': 'Free parking', 'cost': 0, 'rent': 0, 'index': 732, 'owner': ''},
                 {'name': 'Strand', 'type': 'property', 'cost': 220, 'rent': 90, 'index': 1544, 'owner': ''},
                 {'name': 'Chance', 'type': 'chance', 'cost': 0, 'rent': 0, 'index': 2356, 'owner': ''},
                 {'name': 'Fleet Street', 'type': 'property', 'cost': 220, 'rent': 90, 'index': 3168, 'owner': ''},
                 {'name': 'Trafalgar Square', 'type': 'property', 'cost': 240, 'rent': 100, 'index': 3987,
                  'owner': ''},
                 {'name': 'Fenchurch St. Station', 'type': 'station', 'cost': 200, 'rent': 0, 'index': 4806,
                  'owner': ''},
                 {'name': 'Leicester Square', 'type': 'property', 'cost': 260, 'rent': 110, 'index': 5625,
                  'owner': ''},
                 {'name': 'Coventry Street', 'type': 'property', 'cost': 260, 'rent': 110, 'index': 6444,
                  'owner': ''},
                 {'name': 'Water Works', 'type': 'utility', 'cost': 150, 'rent': 4, 'index': 7264, 'owner': ''},
                 {'name': 'Piccadilly', 'type': 'property', 'cost': 280, 'rent': 120, 'index': 8076, 'owner': ''},
                 {'name': 'Go to Jail', 'type': 'jail', 'cost': 0, 'rent': 0, 'index': 8804, 'owner': ''},
                 {'name': 'Regent Street', 'type': 'property', 'cost': 300, 'rent': 130, 'index': 8796, 'owner': ''},
                 {'name': 'Oxford Street', 'type': 'property', 'cost': 300, 'rent': 130, 'index': 8788, 'owner': ''},
                 {'name': 'Community Chest', 'type': 'community chest', 'cost': 0, 'rent': 0, 'index': 8780,
                  'owner': ''},
                 {'name': 'Bond Street', 'type': 'property', 'cost': 320, 'rent': 150, 'index': 8772, 'owner': ''},
                 {'name': 'Liverpool St. Station', 'type': 'station', 'cost': 200, 'rent': 25, 'index': 8764,
                  'owner': ''},
                 {'name': 'Chance', 'type': 'chance', 'cost': 0, 'rent': 0, 'index': 8756, 'owner': ''},
                 {'name': 'Park Lane', 'type': 'property', 'cost': 350, 'rent': 175, 'index': 8748, 'owner': ''},
                 {'name': 'Super Tax', 'type': 'tax', 'cost': 100, 'rent': 0, 'index': 8740, 'owner': ''},
                 {'name': 'Mayfair', 'type': '', 'cost': 400, 'rent': 200, 'index': 8732, 'owner': ''},
                 {'name': 'GO Collect', 'type': 'go', 'cost': 200, 'rent': 0, 'index': 8724, 'owner': ''}]

sprites = ['👽', '🤖', '🤡', '🥸', '👻', '🎃']
for i in range(len(player_data)):
    print(f'Player {i + 1}\nChoose your sprite!\n', end='')
    for j in range(len(sprites)):
        print(f'{j + 1}.{sprites[j]}')
    player_data[i]['sprite'] = sprites[(int(input()) - 1)]
    sprites.remove(player_data[i]['sprite'])
    board[8725 + i] = player_data[i]["sprite"]

print(''.join(board))


def transaction(pay=tuple(), receiver=-1, go=-1):
    if go > -1:
        player_data[go]['credit'] += 200
        print('You passed go!\nYou have been credited $200.')
    elif receiver == -1:
        player_data[pay[0]]['credit'] -= pay[1]
        print(f'${pay[1]} has been deducted from {player_data[pay[0]]["sprite"]}.\nRemaining Balance:\n{player_data[pay[0]]["sprite"]} - ${player_data[pay[0]]["credit"]}')
    elif receiver > -1:
        player_data[pay[0]]['credit'] -= pay[1]
        player_data[receiver]['credit'] += pay[1]
        print(f'${pay[1]} has been transferred from {player_data[pay[0]]["sprite"]} to {player_data[receiver]["sprite"]}.\nRemaining Balance:\n{player_data[pay[0]]["sprite"]} - ${player_data[pay[0]]["credit"]}\n{player_data[receiver]["sprite"]} - ${player_data[receiver]["credit"]}')


i, rent = 0, 0
while True:
    input(f'Player {player_data[i]["sprite"]}\'s turn!\nPress enter to roll the dice.')
    dice = random.randint(2, 12)
    print(f'Player {player_data[i]["sprite"]} rolled {dice}.')
    board[property_data[player_data[i]['pos']]["index"] + 1 + i] = '  '
    if player_data[i]['pos'] + dice < 40:
        player_data[i]['pos'] = player_data[i]['pos'] + dice
    else:
        player_data[i]['pos'] = dice - (40 - player_data[i]['pos'])
        transaction(go=i)
    time.sleep(2)
    board[property_data[player_data[i]['pos']]["index"] + 1 + i] = player_data[i]["sprite"]
    os.system('cls')
    print(''.join(board))

    if property_data[player_data[i]['pos']]['type'] == 'community chest':
        print("We do the comm chest stuff in a bit")

    elif property_data[player_data[i]['pos']]['type'] == 'chance':  # scenes
        print("Chances to mess up ezly")
        ch = random.randint(0, 1)
        if ch == 0:  # good or bad luck on this
            pass
        else:
            pass

    elif property_data[player_data[i]['pos']]['type'] == 'jail':  # Either pay 100 and continue on bail or skip a turn?
        board[property_data[player_data[i]['pos']]["index"] + 1 + i] = '  '
        player_data[i]['pos'] = 9
        board[property_data[player_data[i]['pos']]["index"] + 1 + i] = player_data[i]["sprite"]
        print("Criminal! You need to pay a bail of $100.")
        transaction(pay=(i, 100))

    elif property_data[player_data[i]['pos']]['type'] == 'tax':
        print("Pay your taxes!")  # Straight up deduct the amount
        transaction(pay=(i, property_data[player_data[i]['pos']]['cost']))

    elif property_data[player_data[i]['pos']]['type'] in ['Just visiting jail', 'Free parking']:
        print(f"{property_data[player_data[i]['pos']]['type']}!")

    elif property_data[player_data[i]['pos']]['type'] == 'go':
        pass

    elif property_data[player_data[i]['pos']]['owner'] == '':
        while True:
            if property_data[player_data[i]['pos']]['cost'] > player_data[i]['credit']:
                print('Insufficient credits, you can\'t buy this property!')
                break
            resp = input(f"Do you want to purchase {property_data[player_data[i]['pos']]['name']}? (y/n)")
            if resp == 'y':
                transaction(pay=(i, property_data[player_data[i]['pos']]['cost']))
                property_data[player_data[i]['pos']]['owner'] = i
                if property_data[player_data[i]['pos']]['type'] == 'station':
                    player_data[i]['railways'] += 1
                elif property_data[player_data[i]['pos']]['type'] == 'utility':
                    player_data[i]['utilities'] += 1
                break
            elif resp == 'n':
                break
    elif property_data[player_data[i]['pos']]['owner'] != i:
        if property_data[player_data[i]['pos']]['type'] == 'property':
            rent = property_data[player_data[i]['pos']]['rent']

        elif property_data[player_data[i]['pos']]['type'] == 'station':
            rent = 25 * player_data[property_data[player_data[i]['pos']]['owner']]['railways']

        elif property_data[player_data[i]['pos']]['type'] == 'utility':
            rent = dice * 4 if player_data[property_data[player_data[i]['pos']]['owner']]['utilities'] == 1 else dice * 10
        print(f"You landed on {player_data[property_data[player_data[i]['pos']]['owner']]['sprite']}'s property. You have to pay a rent of ${rent}!")
        transaction(pay=(i, rent), receiver=property_data[player_data[i]['pos']]['owner'])
    time.sleep(2)
    if player_data[i]['credit'] < 0:
        print(f'Player {player_data[i]["sprite"]} is bankrupt!\nAll their properties are going to be transferred to the bank.')
        player_data[i]['name'] = 'bank'
    if [x['name'] != 'bank' for x in player_data].count(True) == 1:
        print(f"Player {player_data[[x['name'] != 'bank' for x in player_data].index(True)]['sprite']} wins!!")
        break
    i = i + 1 if i < (len(player_data) - 1) else 0
    if player_data[i]['name'] == 'bank':
        i = i + 1 if i < (len(player_data) - 1) else 0

input()
