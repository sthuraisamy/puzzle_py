import copy

# get puzzle parameters
number_of_doors = int(input('How many doors are there? '))
door_initial_state = int(
    input('What is the initial state of the doors (open=0 or close=1)? '))


def get_initial_doors(number_of_doors, door_initial_state):
    # create initial door numbers and the states
    doors = {}
    for i in range(1, number_of_doors+1):
        doors[i] = door_initial_state

    return doors


def print_doors(doors):
    # print door number and state  
    for key in doors:
        print(f'{key} is {doors[key]}')


def find_door_changes(doors_changing):
    # identiy the doors that change state
    for key in doors_changing:
        next_door_number = key
        while next_door_number <= number_of_doors:
            if doors_changing[next_door_number] == 0:
                doors_changing[next_door_number] = 1
            else:
                doors_changing[next_door_number] = 0
            next_door_number += key

    return doors_changing


def print_door_changes(changed_doors):
    # print door number and state
    doors_open = 0
    doors_closed = 0
    for key in changed_doors:
        if changed_doors[key] == 1:
            doors_closed += 1
        else:
            doors_open += 1

    print(f'There are {doors_open} doors open and {doors_closed} doors closed')


def solve_puzzle(number_of_doors, door_initial_state):
    # run the puzzle solver
    print(
        f'solve puzzel for number of doors {number_of_doors} and initial door state (open=0 or close=1) {door_initial_state}')

    initial_doors = get_initial_doors(number_of_doors, door_initial_state)
    print_doors(initial_doors)

    doors_changing = copy.deepcopy(initial_doors)

    doors_changing = find_door_changes(doors_changing)

    print_doors(doors_changing)

    print_door_changes(doors_changing)


def main():
    """
    Main function.
    """
    print('running puzzle...')
    solve_puzzle(number_of_doors, door_initial_state)


if __name__ == '__main__':
    main()
