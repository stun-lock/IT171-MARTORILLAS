player_mark = 0
player_louie = 0
treasure_x = 19
treasure_y = 3
game_running = True
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
  move = input("Enter move (up/down/left/right): ")
  if move == "right":
    player_mark += 1 
  if move == "left":
    player_mark -= 1
  if move == "up":
    player_louie += 1
  if move == "down":
      player_louie -= 1
  print(f"Player position: ({player_mark}, {player_louie})")
  if player_mark == treasure_x and player_louie == treasure_y:
    print("win")
    break
  if move == "q":
    break
