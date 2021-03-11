# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
score_player_1 = 'Ruud Gullit'
score_player_2 = 'Marcel van Basten'

goal_0 = 32
goal_1 = 54

scorers = score_player_1 + ' ' + str(goal_0) + ', ' + score_player_2 + ' ' + str(goal_1)
print(scorers)


report = f"{score_player_1} scored in the {goal_0}nd minute \n{score_player_2} scored in the {goal_1}th minute"
print(report)

#part 2
player = 'Erwin Koeman'
print(player.find(' '))
first_name = player[0:5]

print(player.find(' '))
Last_name_len = len(player[5:12])
print(Last_name_len)

name_short = player[0] + '.' + player[5:12]
print(name_short)

chant = f"{first_name}! "*len(first_name)
print(chant)

good_chant = chant.rstrip(' ') != chant 
print(good_chant)