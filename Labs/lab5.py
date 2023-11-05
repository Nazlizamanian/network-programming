#Lab5 Nazli Zamanian Gustavsson
import socket

def main():
    role = input("Do you want to be a client (C) or server (S)? ").strip().upper()
    
    if role == 'S':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 60003)) 
        server_socket.listen(1)

        print("Waiting for a client to connect...")
        client_socket, addr = server_socket.accept() #server set ut to accept incoming c
        print(f"Connected to {addr}")

        player_points = 0
        opponent_points = 0

        while True:
            print(f"({player_points},{opponent_points}) Your move: ", end='', flush=True)
            player_move = input().strip().upper()

            while player_move not in ('R', 'P', 'S'):
                print("Invalid move. Please enter R, P, or S: ", end='', flush=True)
                player_move = input().strip().upper()

            client_socket.send(player_move.encode('utf-8')) #sends clients move.

            opponent_move = client_socket.recv(1).decode('utf-8')
            print(f"(opponent's move: {opponent_move})")

            result = determine_winner(player_move, opponent_move)

            if result == "win":
                print("You won this round!")
            elif result == "lose":
                print("Opponent won this round!")

            # Update points
            if result == "win":
                player_points += 1
            elif result == "lose":
                opponent_points += 1

            print(f"({player_points},{opponent_points})")

            if check_game_over(player_points, opponent_points):
                break

        client_socket.close()
        server_socket.close()

    elif role == 'C':
        # Client code
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_ip = input("Enter the server's IP address: ")  
        client_socket.connect((server_ip, 60003))

        player_points = 0
        opponent_points = 0

        while True:
            player_move = input(f"({player_points},{opponent_points}) Your move: ").strip().upper()

            while player_move not in ('R', 'P', 'S'):
                print("Invalid move. Please enter R, P, or S.")
                player_move = input().strip().upper()

            client_socket.send(player_move.encode('utf-8'))

            opponent_move = client_socket.recv(1).decode('utf-8')
            print(f"(opponent's move: {opponent_move})")
            
            result = determine_winner(player_move, opponent_move)

            if result == "win":
                print("You won this round!")
            elif result == "lose":
                print("Opponent won this round!")

            # Update points
            if result == "win":
                player_points += 1
            elif result == "lose":
                opponent_points += 1

            if check_game_over(player_points, opponent_points):
                break

    else:
        print("Invalid role. Please enter 'C' or 'S.")
        
def determine_winner(player, opponent): #Game Logic
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
    
def check_game_over(player_points, opponent_points): #Game rules, first to 3. 
    if player_points == 3 or opponent_points == 3:
        print("Game over!")
        if player_points > opponent_points:
            print(f"You won {player_points} against {opponent_points}")
        else:
            print(f"You lost {player_points} against {opponent_points}")
        return True
    return False
    
if __name__ == "__main__":
    main()