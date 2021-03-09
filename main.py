# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
score_player_1 = 'Ruud Gullit'
score_player_2 = 'Marcel van Basten'

goal_0 = 32
goal_1 = 54

print(score_player_1, + goal_0, score_player_2, + goal_1)
scorers = 'Ruud Gullit 32 Marcel van Basten 54'

report = f"{score_player_1} scored in the {goal_0}nd minute \n{score_player_2} scored in the {goal_1}th minute"
print(report)

#part 2
player = 'Erwin Koeman'
first_name = player[0:5:1]
print(first_name)

last_name_len = f"{player.find('Koeman')} {player[5:12:1]} {len(player[5:12])}"
print(last_name_len)


chant = f"{first_name[0:5]}! "*5
print(chant)



