# ============================================================
# KAREL'S JOURNEY HOME
# A simple terminal puzzle game. Karel starts at the top-left
# of a 10x10 grid and must reach the goal at the bottom-right
# while managing a limited bag of beepers and a limited number
# of steps.
# ============================================================


# Returns three lists that describe every beeper on the grid.
# beeper at (cols[i], rows[i]) has counts[i] beepers on it.
# All values are hardcoded to match the game's fixed map.
def setup_beepers():
    cols = [3, 5, 8, 2, 6, 10, 1, 4, 7, 3, 6, 8, 2, 5, 9, 4, 7, 9, 10, 1, 3, 6, 10, 5, 7, 9, 2, 4, 8, 10, 3, 6, 9]
    rows = [10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]
    counts = [2, 3, 1, 1, 2, 2, 3, 2, 1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2]
    return cols, rows, counts


# Looks through the lists for (col, row) and returns how many
# beepers are there. Returns 0 if that square has no beepers.
def get_beeper_count(cols, rows, counts, col, row):
    i = 0 # start at the first entry in the lists
    while i < len(cols): # check the entry one by one until we reach the end
        if cols[i] == col and rows[i] == row:
            return counts[i]
        i = i + 1 # otherwise move on to the next entry
    return 0


# Changes the beeper count at (col, row) to new_count.
# If that square has no entry yet, a new one is added.
def update_beeper_count(cols, rows, counts, col, row, new_count):
    i = 0
    found = False # Assume the square isn't in the lists yet (flag to update only, or add new)
    while i < len(cols):
        if cols[i] == col and rows[i] == row:
            counts[i] = new_count # overwrite its count with the new value (=1)
            found = True # Remember that we found and updated it
        i = i + 1
    if not found: # add new entry to all three lists
        cols.append(col)
        rows.append(row)
        counts.append(new_count)


# Applies the beeper rule for the square Karel just stepped onto:
# pick up every beeper there, then put exactly 1 beeper back down.
# Returns the new bag total.
def apply_beeper_rule(cols, rows, counts, col, row, bag):
    found = get_beeper_count(cols, rows, counts, col, row)
    new_bag = bag + found - 1
    update_beeper_count(cols, rows, counts, col, row, 1)
    return new_bag


# Prints the 10x10 grid: row 10 at the top, row 1 at the bottom,
# columns 1 to 10 left to right. Each cell sits inside a box border.
def show_grid(karel_col, karel_row, cols, rows, counts):
    border = "+" + "-----+" * 10  # Build the horizontal border line once and reuse it
    row = 10 # Start at row 10 (top of the grid) and work down to row 1
    while row >= 1:
        print(border)
        # Start building the row's content
        line = "|" # opening wall on the left
        # Go through each column left to right
        col = 1
        while col <= 10:
            # Karel's current position - show K
            if karel_col == col and karel_row == row:
                cell = "  K  "
            # Bottom-right corner is the goal - show G
            elif col == 10 and row == 1:
                cell = "  G  "
            else:
                # Look up how many beepers are on this square
                count = get_beeper_count(cols, rows, counts, col, row)
                if count > 0:
                    # Show the beeper count centered in the cell
                    cell = "  " + str(count) + "  "
                else:
                    # Empty square - just blank space
                    cell = "     "
            line = line + cell + "|" # Add this cell and a closing wall to the row
            col = col + 1 # left to right
        print(line) # Print the completed row
        row = row - 1 # down to row 1
    print(border) # Print the bottom border after the last row


# Prints how many beepers are in the bag and how many steps are left.
def show_status(bag, steps_left):
    print("Bag total     : " + str(bag) + " beepers")
    print("Steps left    : " + str(steps_left))


# True if (col, row) is a real square on the 10x10 grid.
def is_valid_position(col, row):
    if col >= 1 and col <= 10 and row >= 1 and row <= 10:
        return True
    return False


# Prints the welcome message shown once when the game starts.
def show_welcome_message(bag, step_limit):
    print("--------------------------------------------------")
    print("         KAREL'S JOURNEY HOME")
    print("--------------------------------------------------")
    print("Help Karel reach home at the bottom-right corner!")
    print("")
    print("HOW IT WORKS:")
    print("  Every step Karel takes:")
    print("  - Empty square  : bag loses 1 beeper")
    print("  - 1 beeper      : bag stays the same")
    print("  - 2 beepers     : bag gains 1 beeper")
    print("  - 3 beepers     : bag gains 2 beepers")
    print("")
    print("  Run out of beepers = GAME OVER")
    print("  Run out of steps   = GAME OVER")
    print("  Reach G            = YOU WIN")
    print("")
    print("COMMANDS:")
    print("  w = up    s = down")
    print("  a = left  d = right")
    print("")
    print("Starting bag : " + str(bag) + " beepers")
    print("Step limit   : " + str(step_limit) + " steps")
    print("--------------------------------------------------")


def main():
    beeper_cols, beeper_rows, beeper_counts = setup_beepers()

    karel_col = 1
    karel_row = 10
    bag = 4
    step_limit = 20
    steps_left = 20

    show_welcome_message(bag, step_limit)
    print("")
    show_grid(karel_col, karel_row, beeper_cols, beeper_rows, beeper_counts)
    show_status(bag, steps_left)
    print("")

    game_over = False

    while not game_over:
        move = input("Your move (w=up, s=down, a=left, d=right): ")

        if move != "w" and move != "s" and move != "a" and move != "d":
            print("Please enter w, a, s or d.")
        else:
            new_col = karel_col
            new_row = karel_row
            if move == "w":
                new_row = karel_row + 1
            elif move == "s":
                new_row = karel_row - 1
            elif move == "a":
                new_col = karel_col - 1
            elif move == "d":
                new_col = karel_col + 1

            if not is_valid_position(new_col, new_row):
                print("Karel cannot go that way!")
            else:
                karel_col = new_col
                karel_row = new_row
                steps_left = steps_left - 1

                if karel_col == 10 and karel_row == 1:
                    print("")
                    show_grid(karel_col, karel_row, beeper_cols, beeper_rows, beeper_counts)
                    steps_used = step_limit - steps_left
                    print("")
                    print("YOU WIN! Karel made it home!")
                    print("Steps used : " + str(steps_used))
                    print("Bag total  : " + str(bag) + " beepers")
                    game_over = True
                else:
                    bag = apply_beeper_rule(beeper_cols, beeper_rows, beeper_counts, karel_col, karel_row, bag)

                    print("")
                    show_grid(karel_col, karel_row, beeper_cols, beeper_rows, beeper_counts)
                    show_status(bag, steps_left)
                    print("")

                    if bag < 0:
                        print("GAME OVER - Karel ran out of beepers!")
                        print("Tip: look for squares with 2 or 3 beepers on your route.")
                        game_over = True
                    elif steps_left == 0:
                        print("GAME OVER - Karel ran out of steps!")
                        print("Tip: try a more direct route to the goal.")
                        game_over = True


main()

if __name__ == "__main__":
    main()