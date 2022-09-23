from random import choice


def main():
    board = []
    magic_square_conversion_directory = {0:1,1:6,2:5,3:8,4:4,5:0,6:3,7:2,8:7}
    for i in range(9):
        board.append((magic_square_conversion_directory[i], " "))
    game_over = False
    turn = choice(["x","o"])
    turns_taken = 0
    while not game_over:
        print(f"{turn} to play")
        print_board(board)
        try:
            spot = int(input())-1
        except ValueError:
            continue
        if board[spot][1] != " ":
            continue
        board[spot] = (board[spot][0],turn)
        turns_taken += 1
        if turns_taken == 9:
            game_over = True
        sets = find_subsets_of_three(unpack_board_list(board)[turn])
        sets_no_duplicates = []
        for i in sets:
            if not i in sets_no_duplicates:
                sets_no_duplicates.append(i)
        for i in sets_no_duplicates:
            if sum(i) == 12:
                game_over = True
                print(f"{turn} wins!".upper())
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    print_board(board)
        
def print_board(board):
    b = []
    for _, item in board:
        b.append(item)
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}\n")

def unpack_board_list(board):
    board_list = {}
    for item in board:
        amount, player = item
        if not player in board_list:
            board_list[player] = [amount]
        else:
            board_list[player].append(amount)
    return board_list

def find_subsets_of_three(l):
    if len(l) < 3:
        return []
    elif len(l) == 3:
        return [l]
    ret = []
    for i in range(len(l)):
        g = l[0:i]+l[i+1:len(l)]
        ret += find_subsets_of_three(g)
    return ret
    
if __name__ == "__main__":
    main()