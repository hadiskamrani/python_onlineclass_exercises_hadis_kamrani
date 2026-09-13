player1 = input("sang,kaghaz ya gheychi ra vared konid(bazikon aval) ").lower()
player2 = input("sang,kaghaz ya gheychi ra vared konid(bazikon dovom) ").lower()
if player1 == "sang" and player2 == "gheychi":
    print("player1 boord")
elif player1 == "kaghaz" and player2 == "gheychi":
    print("player2 boord")
elif player1 == "gheychi" and player2 == "gheychi":
    print("mosavi")
elif player1 == "sang" and player2 == "sang":
    print("mosavi")
elif player1 == "gheychi" and player2 == "sang":
    print("player2 boord")
elif player1 == "kaghaz" and player2 == "kaghaz":
    print("mosavi")
elif player1 == "sang" and player2 == "kaghaz":
    print("player2 boord")
elif player1 == "kaghaz" and player2 == "sang":
    print("player1 boord")
elif player1 == "gheychi" and player2 == "kaghaz":
    print("player1 boord")
