import sys
import time
import string
import os


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=800, cols=800))


def intro():
    print("Loading:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

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

    for _ in range(10):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.4)
            os.system('cls' if os.name == 'nt' else 'clear')


def check_quit(input):
    if input == 'QUIT':
        sys.exit(0)
    else:
        return


def get_coord_input(ship_size):
    if ship_size == 1:
        size_one_ship_coord = list(input("Please select a starting coordinate for your small(1) ship (for example A1): ").upper())
        check_quit(''.join(size_one_ship_coord))
        return size_one_ship_coord
    if ship_size == 2:
        size_two_ship_coord = list(input("Please select a starting coordinate for your medium(2) ship (for example A1): ").upper())
        check_quit(''.join(size_two_ship_coord))
        return size_two_ship_coord


def ship_input(ship_size):
    input_checker = False
    good_cords_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    good_cords_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    good_cords_number_string = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    while input_checker is False:
        full_input = get_coord_input(ship_size)
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
                        print("Wrong coordinates!")
                        input_checker = False
                else:
                    print("Wrong coordinates!")
                    input_checker = False
            else:
                print("Wrong coordinates!")
                input_checker = False
        else:
            print("Wrong coordinates!")
            input_checker = False


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
                ship_orientation_var_x = -1 if ship_orientation == "N" else 1 if ship_orientation == "S" else 0
                ship_orientation_var_y = -1 if ship_orientation == "E" else 1 if ship_orientation == "W" else 0
                if ship_coordinates[0] == 0 and ship_orientation_var_x != 0 or ship_coordinates[1] == board_size - 1 and ship_orientation_var_y != 0:
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
    return [['O' for _ in range(board_size)] for _ in range(board_size)]


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


def ship_placement(board, board_size):
    ship_size = 1
    size_one_ship_coordinates = ship_input(ship_size)
    print(size_one_ship_coordinates)
    ship_size += 1
    size_two_ship_start_coordinates = ship_input(ship_size)
    print(size_two_ship_start_coordinates)
    size_two_ship_full_coordinates = size_two_ship_orient(size_two_ship_start_coordinates, board_size)
    battleship_game(board, board_size, size_one_ship_coordinates, size_two_ship_full_coordinates)


def mark_ship(size_one_ship_coordinates, size_two_ship_full_coordinates, board_size):
    row = size_one_ship_coordinates[0]
    col = size_one_ship_coordinates[1]


def battleship_game(board, board_size, size_one_ship_coordinates, size_two_ship_full_coordinates):
    print("akurvanyad")


def get_player_boards(player, board, board_size):
    print_var = ''
    if player == "1":
        print_var = print_board(board, board_size)
    if player == "2":
        print_var = print_board(board, board_size) 
    return print_var


def main():
    # intro()
    # animated_logo_print()
    board_size = valid_board_size_input()
    board1 = init_board(board_size)
    board2 = init_board(board_size)
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
    ship_placement(board1, board_size)


if __name__ == "__main__":
    main()
