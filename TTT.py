SIZE = 3
board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]  # 게임 보드
moves = []  # 플레이어가 둔 위치를 저장하는 리스트

def initialize_board():
    # 보드를 빈 칸으로 초기화
    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = ' '  # 빈 칸으로 초기화

def print_board():
    # 현재 보드 상태 출력
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end='')
            if j < SIZE - 1:
                print(" | ", end='')
        print()
        if i < SIZE - 1:
            print("--+---+--")

def check_win(player):
    # 가로, 세로, 대각선에서 승리 여부 확인
    for i in range(SIZE):
        # 가로 체크
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # 세로 체크
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # 대각선 체크
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_board_full():
    # 보드가 꽉 찼는지 확인
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == ' ':
                return False
    return True

def remove_first_move():
    if moves:
        first_move = moves.pop(0)  # 가장 처음 선택한 위치
        row, col = first_move
        board[row][col] = ' '  # 그 위치 비우기

def main():
    player = 'X'  # 첫 번째 플레이어는 'X'
    game_won = False

    initialize_board()

    while not game_won and not is_board_full():
        print_board()
        move = int(input(f"Player {player}, enter your move (1-9): "))

        if 1 <= move <= 9:
            row = (move - 1) // SIZE
            col = (move - 1) % SIZE

            if board[row][col] == ' ':  # 빈 칸에만 놓을 수 있음
                board[row][col] = player  # 현재 플레이어의 마크 넣기
                moves.append((row, col))  # 현재 플레이어의 움직임 저장

                # 6번째 움직임부터는 가장 먼저 둔 자리를 비움
                if len(moves) > 6:
                    remove_first_move()  # 6번째 움직임 이후 가장 먼저 선택한 자리 지우기

                # 승리 여부 확인
                if check_win(player):
                    game_won = True
                    print_board()
                    print(f"Player {player} wins!")
                else:
                    # 다음 플레이어로 전환
                    player = 'O' if player == 'X' else 'X'
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid move. Try again.")

    if not game_won and is_board_full():
        print_board()
        print("It's a draw!")

if __name__ == "__main__":
    main()