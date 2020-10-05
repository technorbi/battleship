import sys
import string

from numpy.core.numeric import full


def check_quit(input):
    if input == 'QUIT':
        sys.exit(0)
    else:
        return


def ship_input():
    input_checker = False
    good_cords_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    good_cords_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while input_checker is False:
        full_input = list(input("Please select a row and a column (for example A1): ").upper())
        check_quit(''.join(full_input))
        if len(full_input) == 2:
            for key, value in good_cords_letter.items():
                if full_input[0] == key:
                    if int(full_input[1]) in good_cords_number:
                        row = full_input[0]
                        col = int(full_input[1])-1
                        if row in good_cords_letter.keys() and col in good_cords_number:
                            for r, v in good_cords_letter.items():
                                if row == r:
                                    row = v
                                    return row, col
                                # else:
                                #     print("anyád3")
                                #     print("Coordinates is used! Choose another coordinate!")
                                #     input_checker = False
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
        board_size = int(input("What size you want for the board? "))
        if board_size in valid_input_numbers:
            return board_size
        else:
            print("Not a valid input! Please input a number from 5 to 10 ") 
            input_is_valid = True


def size_two_ship_orient(ship_coordinates):
    good_coords_and_orientation = False
    while good_coords_and_orientation is False:
        ship_orientation = input("Please input the orientation of the ship: ((N)orth/(W)est/(S)outh/(E)ast ").lower()
        if ship_orientation == "n":
            if ship_coordinates[0] == 0:
                good_coords_and_orientation = False
                print("You can't place the ship here!")
            else:
                orient = ship_coordinates, ((ship_coordinates[0]) - 1 , ship_coordinates[1])
                return orient
        if ship_orientation == "w":
            pass
        if ship_orientation == "s":
            pass
        if ship_orientation == "e":
            pass

    # return starting coordinates, and orientation
    pass


def ship_place(ship_orient):
    little_ship = []
    medium_ship = []
    pass
 

def init_board(board_size):
    return [['O' for _ in range(board_size)] for _ in range(board_size)]


def print_board(board, board_size):
    header = ' '
    for index in range(board_size):
        header += f' {index+1}'
    print(header)
    for row_index, row in enumerate(board):
        line = f"{list(string.ascii_uppercase)[row_index]} "
        for element in row:
            line += element + ' '
        line = line[0:-1]
        print(line)


def hit_checker():
    pass


def main():
    board_size = valid_board_size_input()
    board = init_board(board_size)
    print_board(board, board_size)
    ship_coordinates = ship_input()
    ship_orientation = size_two_ship_orient(ship_coordinates)
    ship_placement = ship_place(ship_orientation)
    hit_checker(ship_placement)


if __name__ == "__main__":
    main()