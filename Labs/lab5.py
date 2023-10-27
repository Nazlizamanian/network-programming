#Lab5 Nazli Zamanian Gustavsson

import socket

def play_game(player_type, server_ip):
    player_moves={'R': 'rock', 'P': 'paper', 'S':'scissors'}
    player_points={'server':0, 'client':0}
    
    if player_type =='S'