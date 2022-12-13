# Write your code here
import random
import collections
def create_set():
    all_pairs = []
    for i in range(7):
        for j in range(i,7):
            all_pairs.append([i,j])
    shuffled = shuffle(all_pairs)
    computer_set, player_set, stock_set = shuffled[0], shuffled[1], shuffled[2]
    return computer_set, player_set, stock_set

def shuffle(domino_set):
    random.shuffle(domino_set)
    return domino_set[0:7], domino_set[7:14], domino_set[14:]

def starting_piece(computer, player):
    for double in (6, -1, -1):
        if [double, double] in computer or [double, double] in player:
            return[double, double]
    return -1

def check_status(doubles, computer, player):
    status = ""
    if doubles in computer:
        computer.remove(doubles)
        status += str0
    elif doubles in player:
        player.remove(doubles)
        status += str1
    return status, computer, player

def show_player_pcs():
    print("Your pieces:")
    for i in range(len(player)):
        print(f"{i + 1}:{player[i]}")
    print("")

def show_domino_snake():
    print("")

    if len(snake) > 6:
        for i in range(0,3):
            print(snake[i], end = '')
        print("...", end = '')
        for i in range(-3, 0):
            print(snake[i], end = '')
    else:
        for i in snake:
            print(i, end='')

    print("\n")

def show_set_sizes():
    print("Stock size: ", len(stock))
    print("Computer pieces: ", len(computer))

def interface():
    print("=" * 70)
    show_set_sizes()
    show_domino_snake()
    show_player_pcs()

def validateMove(cmd, type):
    if type == 'p':
        if 0 > cmd >= -len(player):
            domino = player[-(cmd+1)]
            if snake[0][0] == domino[0] or snake[0][0] == domino[1]:
                return True
        elif 0 < cmd <= len(player):
            domino = player[cmd - 1]
            if snake[-1][-1] == domino[0] or snake[-1][-1] == domino[1]:
                return True

    if type == 'c':
        if 0 > cmd >= -len(computer):
            domino = computer[-(cmd+1)]
            if snake[0][0] == domino[0] or snake[0][0] == domino[1]:
                return True
        elif 0 < cmd <= len(computer):
            domino = computer[cmd - 1]
            if snake[-1][-1] == domino[0] or snake[-1][-1] == domino[1]:
                    return True
    return False

def l_domino_reverse(snake_piece, domino):
    if snake_piece[0] == domino[-1] :
        return domino
    else:
        return domino[::-1]

def r_domino_reverse(snake_piece, domino):
    if snake_piece[-1] == domino[0]:
        return domino
    else:
        return domino[::-1]

def player_turn():
    while True:
        try:
            cmd = int(input())
            if cmd == 0 == len(stock):
                return 0
        except Exception:
            print("Invalid input. Please try again.")
            continue

        if cmd > len(player) or cmd < -len(player):
            print("Invalid input. Please try again.")
            continue

        if validateMove(cmd, 'p') == False and cmd != 0:
            print("Illegal move. Please Try again.")
            continue

        if 0 > cmd > -(len(player) + 1):
            cmd = abs(cmd)
            domino = player.pop(cmd - 1)
            domino = l_domino_reverse(snake[0], domino)
            snake.insert(0, domino)
            break
        elif cmd == 0 and len(stock) != 0:
            domino = stock.pop()
            player.append(domino)
            break

        elif 0 < cmd < (len(player) + 1):
            domino = player.pop(cmd - 1)
            domino = r_domino_reverse(snake[-1], domino)
            snake.append(domino)
            break
        else:
            print("Invalid input. Please try again.")

def computer_turn():
    length = len(computer)
    cmd = 0
    for i in ai():
        if validateMove(i, 'c') == True:
            cmd = i
        elif validateMove(-i, 'c') == True:
            cmd = -i

    if cmd == 0 and len(stock) != 0:
        domino = stock.pop()
        computer.append(domino)
    elif cmd == 0 == len(stock):
        return 0
    elif cmd < 0:
        cmd += 1
        domino = computer.pop(abs(cmd))
        domino = l_domino_reverse(snake[0], domino)
        snake.insert(0, domino)
    elif cmd > 0:
        cmd -= 1
        domino = computer.pop(cmd)
        domino = r_domino_reverse(snake[-1], domino)
        snake.append(domino)

def counts():
    # scores of each number
    count = {}
    for indexes in range(0,7):
        c = 0
        for i in computer:
            for j in i:
                if indexes == j:
                    c += 1
        for i in snake:
            for j in i:
                if indexes == j:
                    c += 1
        count[indexes] = c
    return count

def scores():
    c = counts()
    l = len(computer)
    score = []
    for i in range(l):
        sum = 0
        # print(computer[i])
        for j in computer[i]:
            sum += c[j]
        score.append([i,sum])
    return score

def ai():
    score =  counts()
    x = scores()
    selectionSort(x)
    return [x[0] for x in selectionSort(x)]

def selectionSort(array):
    size =  len(array)
    for ind in range(size):
        max_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j][1] > array[max_index][1]:
                max_index = j
    # swapping the elements to sort the array
        (array[ind], array[max_index]) = (array[max_index], array[ind])
    return array

def isEnd():
    head = snake[0][0]
    tail = snake[-1][-1]
    count = 0
    if head == tail:
        for i in snake:
            for j in i:
                if j == head:
                    count += 1
    if count == 8 or len(player) == 0 or len(computer) == 0:
        return True

    return False

def endGame():
    if len(player) == 0 :
        print("Status: The game is over. You won!")
    elif len(computer) == 0:
        print("Status: The game is over. The computer won!")
    else:
        print("Status: The game is over. It's a draw!")

str0 = "It's your turn to make a move. Enter your command."
str1 = "Computer is about to make a move. Press Enter to continue..."
#   Initialize all the sets.
set = create_set()
while True:
    if starting_piece(set[0], set[1]) == -1:
        set = create_set()
    else:
        break

computer, player, stock = set[0], set[1], set[2]
snake = [starting_piece(computer, player)]
s = check_status(snake[-1], computer, player)
status, computer, player = s[0], s[1], s[2]

def main():
    # Game interface begins here.
    global status
    global computer
    interface()
    print("Status: ", status)

    while True:
        if status == str0:
            a = player_turn()
            if a == 0:
                break
            status = str1
            
        elif status == str1:
            enter = input()
            a = computer_turn()
            if a == 0:
                break
            status = str0
        interface()
        if isEnd():
            print(snake)
            break
        print("Status: ", status)

    endGame()

main()