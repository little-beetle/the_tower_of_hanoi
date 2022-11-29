"""THE TOWER OF HANOI
Moving disk puzzle"""

import copy
import sys

TOTAL_DISKS = 5  # the more discs, the harder the game

# first all disks are on the rod A:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    """Start game"""
    print("""
        THE TOWER OF HANOI.
        
        Move the tower of disks, one disk at a time, to another tower. Larger
        disks cannot rest on top of a smaller disk.
        """
          )
    """List towers contains keys 'A', 'B' and 'C', and value --- lists, which are a column of disks.
     The list contains integers number, which are disks of different sizes, and beginning of the tower is
     the bottom of the tower. For the game with 5 elements are list [5, 4, 3, 2, 1] which are full tower. 
     An empty list [] is an empty tower with no elements. In the list [1, 3] larger disk located on smaller disk.
     It is error! List [3, 1] is correct."""
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}
    NUMBER_OF_MOVES = 0
    while True:  # one move to iterate the loop
        # Showing the tower

        print(f"---------------- number of moves {NUMBER_OF_MOVES} ----------------")
        display_towers(towers)
        NUMBER_OF_MOVES += 1
        # ask the user to move
        from_tower, to_tower = get_player_move(towers)

        # moving top disk with from_tower to to_tower
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # performance check
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)  # show the towers one last time
            print("You have solved the puzzle! Well done!")
            sys.exit()


def get_player_move(towers):
    """
    ask the user to move

    :param towers:
    :return: from_tower, to_tower
    """

    while True:  # while user will not input correct course
        print("Enter the letters of 'from' and 'to' towers, or QUIT.")
        print("(e.g., AB to moves a disk from tower A to tower B.)\n")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # correct input
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA, or CB")
            continue  # ask the move again

        # more meaningful variable names
        from_towers, to_towers = response[0], response[1]

        if len(towers[from_towers]) == 0:
            # tower from_towers will not empty
            print("YOu selected a tower with no disks.")
            continue
        elif len(towers[to_towers]) == 0:
            # any disk can be moved to an empty tower
            return from_towers, to_towers
        elif towers[to_towers][-1] < towers[from_towers][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue  # ask the move again
        else:
            # the right move, return selected towers
            return from_towers, to_towers


def display_towers(towers):
    """Output three towers with disks"""

    # Output three towers
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # output empty tower
            else:
                display_disk(tower[level])  # output disk
        print()

    empty_space = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))

def display_disk(width):
    """
    Width 0 means no disks
    :param width:
    :return: disk of the required width
    """
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # output rod segment without disc
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # output disk
        disk = "@" * width
        num_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


if __name__ == "__main__":
    main()

