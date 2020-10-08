import sys
import time
import string
import os


board1_shadow = []
board2_shadow = []


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=800, cols=800))


def intro():
    print("Loading:")

    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


def animated_logo_print():
    filenames = ["logo.txt", "logo2.txt"]
    frames = []

    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for _ in range(6):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.3)
            os.system('cls' if os.name == 'nt' else 'clear')


def check_quit(input):
    if input == 'QUIT':
        sys.exit(0)
    else:
        return


def get_coord_input(ship_size):
    if ship_size == 1:
        size_one_ship_coord = list(input("Please select a starting coordinate for your small(1) ship (for example A1): \n").upper())
        check_quit(''.join(size_one_ship_coord))
        return size_one_ship_coord
    if ship_size == 2:
        size_two_ship_coord = list(input("Please select a starting coordinate for your medium(2) ship (for example A1): \n").upper())
        check_quit(''.join(size_two_ship_coord))
        return size_two_ship_coord


def get_shoot_coord_input():
    shoot_enemy_coord = list(input("Please select a coordinate to shoot your enemy(for example A1): \n").upper())
    print()
    check_quit(''.join(shoot_enemy_coord))
    return shoot_enemy_coord


def ship_input(ship_size, game_phase):
    input_checker = False
    good_cords_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    good_cords_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    good_cords_number_string = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    while input_checker is False:
        try:
            if game_phase == 1:
                full_input = get_coord_input(ship_size)
                row, col = valid_input_checker(full_input, good_cords_letter, good_cords_number_string, good_cords_number)
                return row, col
            elif game_phase == 2:
                full_input = get_shoot_coord_input()
                row, col = valid_input_checker(full_input, good_cords_letter, good_cords_number_string, good_cords_number)
                return row, col
        except ZeroDivisionError:
            print("Wrong coordinates!")
            input_checker = False


def valid_input_checker(full_input, good_cords_letter, good_cords_number_string, good_cords_number):
    check_quit(''.join(full_input))
    if len(full_input) == 3:
        full_input.remove(full_input[1])
    if len(full_input) == 2:
        if full_input[0] in good_cords_letter.keys():
            if full_input[1] in good_cords_number_string:
                row = full_input[0]
                col = int(full_input[1]) - 1
                col = 9 if col == -1 else col
                if row in good_cords_letter.keys() and col in good_cords_number:
                    for r, v in good_cords_letter.items():
                        if row == r:
                            row = v
                            return row, col
                else:
                    raise ZeroDivisionError
            else:
                raise ZeroDivisionError
        else:
            raise ZeroDivisionError
    else:
        raise ZeroDivisionError


def valid_board_size_input():
    input_is_valid = True
    while input_is_valid:
        valid_input_numbers = list(range(5, 11))
        board_size = input("What board size do you want? ")
        check_quit(board_size)
        if board_size.isdigit():
            board_size = int(board_size)
            if board_size in valid_input_numbers:
                return board_size
            else:
                print("Not a valid input! Please input a number from 5 to 10 ")
                input_is_valid = True
        else:
            print("Not a valid input! Please input a number from 5 to 10 ")
            input_is_valid = True


def size_two_ship_orient(ship_coordinates, board_size):
    good_coords_and_orientation = False
    while good_coords_and_orientation is False:
        ship_orientation = input("Please input the orientation of the ship: ((N)orth/(W)est/(S)outh/(E)ast ").upper()
        check_quit(ship_orientation)
        if ship_orientation.isalpha():
            if len(ship_orientation) == 1:
                ship_orientation_var_y = -1 if ship_orientation == "W" else 1 if ship_orientation == "E" else 0
                ship_orientation_var_x = -1 if ship_orientation == "N" else 1 if ship_orientation == "S" else 0
                if (ship_orientation_var_x + ship_coordinates[0]) < 0 or (ship_orientation_var_y + ship_coordinates[1]) < 0 or (ship_orientation_var_x + ship_coordinates[0]) > board_size - 1 or (ship_orientation_var_y + ship_coordinates[1]) > board_size - 1:
                    good_coords_and_orientation = False
                    print("You can't place the ship here!")
                else:
                    orient = ship_coordinates, ((ship_coordinates[0]) + ship_orientation_var_x, ship_coordinates[1] + ship_orientation_var_y)
                    return orient
            else:
                good_coords_and_orientation = False
                print("Not a valid input!")
        else:
            good_coords_and_orientation = False
            print("Not a valid input!")


def init_board(board_size):
    return [['0' for _ in range(board_size)] for _ in range(board_size)]


def print_board(board, board_size):
    print_var = ''
    header = ' '
    for index in range(board_size):
        header += f' {index+1}'
    print_var += header + "\n"
    for row_index, row in enumerate(board):
        line = f"{list(string.ascii_uppercase)[row_index]} "
        for element in row:
            line += element + ' '
        line = line[0:-1]
        print_var += line + "\n"
    return print_var


def mark_ship_1(board, board_size, size_one_ship_coordinates):
    row = size_one_ship_coordinates[0]
    col = size_one_ship_coordinates[1]
    if board[row][col] == '0':
        board[row][col] = 'X'


def mark_ship_2(board, board_size, size_two_ship_full_coordinates):
    row_start = size_two_ship_full_coordinates[0][0]
    row_end = size_two_ship_full_coordinates[1][0]
    col_start = size_two_ship_full_coordinates[0][1]
    col_end = size_two_ship_full_coordinates[1][1]
    if board[row_start][col_start] == '0':
        board[row_start][col_start] = 'X'
    if board[row_end][col_end] == '0':
        board[row_end][col_end] = 'X'


def ship_placement(board, board_size):
    player_ship_list = []
    ship_size = 1
    game_phase = 1
    size_one_ship_coordinates = ship_input(ship_size, game_phase)
    player_ship_list.append(size_one_ship_coordinates)
    mark_ship_1(board, board_size, size_one_ship_coordinates)
    placement_board_p_1 = print_board(board, board_size)
    print()
    print(placement_board_p_1)
    ship_size += 1
    size_two_ship_start_coordinates = ship_input(ship_size, game_phase)
    size_two_ship_full_coordinates = size_two_ship_orient(size_two_ship_start_coordinates, board_size)
    player_ship_list.append(size_two_ship_full_coordinates)
    mark_ship_2(board, board_size, size_two_ship_full_coordinates)
    placement_board_p_1 = print_board(board, board_size)
    print()
    print(placement_board_p_1)
    return player_ship_list


def battleship_game_player_rotation(board1, board2, board_size, player_1_ship_list, player_2_ship_list, game_phase, ship_size):
    player = '1'
    player_1_miss = []
    player_2_miss = []
    player_1_ship_list_copy = []
    player_2_ship_list_copy = []
    win_checker = True
    player_1_ship_1, player_1_ship_2, player_2_ship_1, player_2_ship_2 = all_ship_coordiane_lists(player_1_ship_list, player_2_ship_list)
    while win_checker is True:
        reset = hit_checker(game_phase, ship_size, player, player_1_miss, player_2_miss, player_1_ship_1, player_1_ship_2, player_2_ship_1, player_2_ship_2, player_1_ship_list_copy, player_2_ship_list_copy)
        if reset != 'skip':
            os.system('cls' if os.name == 'nt' else 'clear')
        double_board_print_logic(board1, board2, board_size)
        if reset == True:
            win_checker = False
        elif reset == 'skip':
            win_checker = True
        else:
            player = '1' if player == '2' else '2'


def new_game():
    while True:
        new_game = input("Do you want to play Battleship again?(Y/N)").upper()
        if new_game == 'Y':
            return True
        elif new_game == 'N':
            return False
    

def all_ship_coordiane_lists(player_1_ship_list, player_2_ship_list):
    player_2_ship_2 = []
    player_2_ship_1 = [item for i, item in enumerate(player_2_ship_list) if i == 0]
    for item in player_2_ship_list[1]:
        player_2_ship_2.append(item)
    player_1_ship_2 = []
    player_1_ship_1 = [item for i, item in enumerate(player_1_ship_list) if i == 0]
    for item in player_1_ship_list[1]:
        player_1_ship_2.append(item)
    return player_1_ship_1, player_1_ship_2, player_2_ship_1, player_2_ship_2


def hit_checker(game_phase, ship_size, player, player_1_miss, player_2_miss, player_1_ship_1, player_1_ship_2, player_2_ship_1, player_2_ship_2, player_1_ship_list_copy, player_2_ship_list_copy):
    game_phase = 2
    player_shoot = ship_input(ship_size, game_phase)
    hit_var = ''
    if player == '1':
        if player_shoot in player_1_miss:
            print("You've already shot here Colonel! Don't waste ammo!")
            return 'skip'
        elif player_shoot in player_2_ship_1:
            player_1_miss.append(player_shoot)
            print('Precise Hit! You sunk the enemy ship! Ay Ay Colonel!')
            hit_var = 'S'
        elif player_shoot in player_2_ship_2:
            player_1_miss.append(player_shoot)
            if len(player_2_ship_2) != 0:
                player_2_ship_2.remove(player_shoot)
                player_2_ship_list_copy.append(player_shoot)
                print('Precise Hit! Ay Ay Colonel!\n')
                hit_var = 'H'
                if len(player_2_ship_2) == 0:    
                    print('Precise Hit! You sunk the enemy ship! Ay Ay Colonel!')
                    hit_var = 'S'
                    for i in player_2_ship_list_copy:
                        board1_shadow[i[0]][i[1]] = hit_var
                    return True
        else:
            player_1_miss.append(player_shoot)
            print("You've missed it Colonel!")
            hit_var = 'M'
        board2_shadow[player_shoot[0]][player_shoot[1]] = hit_var
    elif player == '2':
        if player_shoot in player_2_miss:
            print("You've already shot here Colonel! Don't waste ammo!")
            return 'skip'
        elif player_shoot in player_1_ship_1:
            player_2_miss.append(player_shoot)
            print('Precise Hit! You sunk the enemy ship! Ay Ay Colonel!')
            hit_var = 'S'
        elif player_shoot in player_1_ship_2:
            player_2_miss.append(player_shoot)
            if len(player_1_ship_2) != 0:
                player_1_ship_2.remove(player_shoot)
                player_1_ship_list_copy.append(player_shoot)
                print('Precise Hit! Ay Ay Colonel!\n')
                hit_var = 'H'
                if len(player_1_ship_2) == 0:    
                    print('Precise Hit! You sunk the enemy ship! Ay Ay Colonel!')
                    hit_var = 'S'
                    for i in player_1_ship_list_copy:
                        board1_shadow[i[0]][i[1]] = hit_var
                    return True
        else:
            player_2_miss.append(player_shoot)
            print("You've missed it Colonel!")
            hit_var = 'M'
        board1_shadow[player_shoot[0]][player_shoot[1]] = hit_var


def get_player_boards(player, board, board_size):
    print_var = ''
    if player == "1":
        print_var = print_board(board, board_size)
    if player == "2":
        print_var = print_board(board, board_size)
    return print_var


def double_board_print_logic(board1, board2, board_size):
    get_player_1_list = get_player_boards('1', board1, board_size).splitlines()
    get_player_2_list = get_player_boards('2', board2, board_size).splitlines()
    board_size_spaces = ((board_size * 2) - 14)
    board_size_spaces = 1 if board_size_spaces <= 0 else board_size_spaces
    print('\n{2:{3}}{0:30}{1}\n'.format("Player1 board:", "Player2 board:", ' ', board_size_spaces))
    board_size_meter = (14 - ((board_size * 2) + 1)) / 2
    board_size_meter = 1 if board_size_meter <= 0 else board_size_meter
    for i in range(len(get_player_1_list)):
        print('{2:{3}}{0:30}{1}'.format(get_player_1_list[i], get_player_2_list[i], ' ', board_size_meter))
    print()


def main():
    intro()
    animated_logo_print()
    new_game_check = True
    while new_game_check:
        os.system('cls' if os.name == 'nt' else 'clear')
        board_size = valid_board_size_input()
        board1 = init_board(board_size)
        board2 = init_board(board_size)
        double_board_print_logic(board1, board2, board_size)
        print("Player 1 Board: \n")
        player_1_ship_list = ship_placement(board1, board_size)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Player 2 Board: \n")
        player_2_ship_list = ship_placement(board2, board_size)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{'':>13}Let the game begin!\n")
        global board1_shadow
        board1_shadow = init_board(board_size)
        global board2_shadow
        board2_shadow = init_board(board_size)
        battleship_game_player_rotation(board1_shadow, board2_shadow, board_size, player_1_ship_list, player_2_ship_list, game_phase=1, ship_size=1)
        new_game_check = new_game()


if __name__ == "__main__":
    main()
