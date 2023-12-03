#Lab5 Nazli Zamanian 
import socket

def serversideGetPlaySocket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 60003))
    server_socket.listen(1)
    
    print("Waiting for a client to connect...")
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    return server_socket, client_socket

def clientsideGetPlaySocket(host):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 60003))
    
    return client_socket

def main():
    role = input("Do you want to be a client (C) or server (S)? ").strip().upper()
    
    if role == 'S':
        server_socket, client_socket = serversideGetPlaySocket()
    elif role == 'C':
        host = input("Enter the server's IP address: ")
        client_socket = clientsideGetPlaySocket(host)
    else:
        print("Invalid role. Please enter 'C' or 'S.")
        return

    player_points = 0
    opponent_points = 0

    while True:
        print(f"({player_points},{opponent_points}) Your move: ", end='', flush=True)
        player_move = input().strip().upper()

        while player_move not in ('R', 'P', 'S'):
            print("Invalid move. Please enter R, P, or S: ", end='', flush=True)
            player_move = input().strip().upper()

        client_socket.send(player_move.encode('utf-8'))

        opponent_move = client_socket.recv(1).decode('utf-8')
        print(f"(opponent's move: {opponent_move})")

        result = determine_winner(player_move, opponent_move)

        if result == "win":
            print("You won this round!")
        elif result == "lose":
            print("Opponent won this round!")

        if result == "win":
            player_points += 1
        elif result == "lose":
            opponent_points += 1

        print(f"({player_points},{opponent_points})")

        if check_game_over(player_points, opponent_points):
            break

    client_socket.close()
    if role == 'S':
        server_socket.close()

def determine_winner(player, opponent):
    if player == opponent:
        return "draw"
    elif player == 'R' and opponent == 'S':
        return "win"
    elif player == 'S' and opponent == 'P':
        return "win"
    elif player == 'R' and opponent == 'P':
        return "win"
    else:
        return "lose"

def check_game_over(player_points, opponent_points):
    if player_points == 10 or opponent_points == 10:
        print("Game over!")
        if player_points > opponent_points:
            print(f"You won {player_points} against {opponent_points}")
        else:
            print(f"You lost {player_points} against {opponent_points}")
        return True
    return False

if __name__ == "__main__":
    main()
