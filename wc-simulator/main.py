import random
import time
import gtts
from playsound import playsound

team_1 = ''
team_2 = ''
coin = random.randint(1, 2)
team_num = 0
team = ''
team_1_score = 0
team_2_score = 0
score_time = 10
winner = ''
penalty_shooter = 0
penalty_saver = 0


def game(team_1_score, team_2_score, time_score, penalty_shooter, penalty_saver, team_num):
  for i in range(0, 3):
    print()

  print('Today in the World Cup Final 2026 Australia we have...')
  print()
  time.sleep(3)
  print('A glorius team who has found themself in  a world cup final...')
  time.sleep(3)
  print(f'{team_1.upper()}!!!!!!')
  print()
  time.sleep(4)
  print('And we also have a team who has tried hard to get themself to a final...')
  time.sleep(3)
  print(f'{team_2.upper()}!!!!!!')
  time.sleep(4)
  print()
  print("Let's begin the match!")
  time.sleep(2)
  print()
  print('Coin Flip!')
  print()
  print(f'{team_1} is heads')
  print()
  print(f'{team_2} is tails')

  if coin == 1:
    print(f'Heads! {team_1} will take kickoff')
  else:
    print(f'Tails! {team_2} will take kickoff')
  print()

  for m in range(0, 90):
    time.sleep(0.50)
    gol = random.randint(0, 20)
    penalty = random.randint(2, 10)
    free_kick = random.randint(3, 10)
    saved = random.randint(3, 10)
    wall = random.randint(1, 2)
    free_kick_score = random.randint(1, 3)
   
    if gol == 5:
      if  not penalty == 2 or not free_kick == 10:
        team_num = random.randint(1, 2)
        if team_num == 1:
          team_1_score += 1
          print(f"{team_1} '{time_score} ")
        if team_num == 2:
          team_2_score += 1
          print(f"{team_2} '{time_score} ")
        print(f'{team_1} {team_1_score} - {team_2_score} {team_2} ')
      if penalty == 3 and not free_kick == 4:
        team_num = random.randint(1, 2)
        print('Foul!')
        if team_num == 1:
          print(f'Penalty for {team_1}')
          penalty_shooter = team_1
          penalty_saver = team_2
        if team_num == 2:
          print(f'Penalty for {team_2}')
          penalty_shooter = team_2
          penalty_saver = team_1
        print('Coach decide who kick...')
        time.sleep(3)
        print(f'{penalty_shooter} goes up for a kick')
        time.sleep(4)
        if not saved == 3:
          print('Its in! Gooooooooooooool!')
          if team_num == 1:
            team_1_score += 1
          if team_num == 2:
            team_2_score += 1
          print(f'{team_1} {team_1_score} - {team_2_score} {team_2} ')

        if saved == 3:
          print(f'{penalty_saver} saves the penalty!!!!!!')
      if free_kick == 10:
        print()
        print('There a Foul from outside the box')
        time.sleep(3)
        if team_num == 1:
          print(f'Free Kick for {team_1}')
          penalty_shooter = team_1
          penalty_saver = team_2
        if team_num == 2:
          print(f'Free Kick for {team_2}')
          penalty_shooter = team_2
          penalty_saver = team_1
        time.sleep(3)
        print('He shoots!')
        time.sleep(3)
        if wall == 3:
          print('The kick hits the wall')
        else:
          print('Over the Wall!')
          time.sleep(3)
          if free_kick_score == 1:
            print('Thats on target')
            time.sleep(3)
            print('Its in!')
            print('Top Bins!')
            if team_num == 1:
              team_1_score += 1
            if team_num == 2:
              team_2_score += 1
            print(f'{team_1} {team_1_score} - {team_2_score} {team_2} ')
            time.sleep(3)

          elif free_kick_score == 2:
            print('Miss, it went over the bar!')
          elif free_kick_score == 3:
            print('Thats on target')
            time.sleep(3)
            print('Its saved by the goalie!!!!!!')





        print('')

      print()
    time_score += 1
    if time_score == 45:
      print('Half Time!')
      print('Players go to their lockers')
      time.sleep(5)
      print('Half time Over!')
      print()

  print('Full Time!')



def penalty_shootout():
  pass

###game(team_1_score, team_2_score, score_time, penalty_shooter, penalty_saver, team_num)

#rematch = input('Rematch (y / n): ')

#if rematch == 'y':
#  team_1_score = 0
#  team_2_score = 0
#  game(team_1_score, team_2_score, score_time, penalty_shooter, penalty_saver, team_num)


# Intro
intro = gtts.gTTS("Here we have the 2026 World Cup for us to enjoy............. who will win the tournament and finish on top? who will be the best tean at soccer! Let us find out.... Lets begin")
intro.save('intro.mp3')
playsound("intro.mp3")

# Find Group stage
find_groups = gtts.gTTS("Lets see what groups we have")
find_groups.save('lets_see.mp3')
playsound("lets_see.mp3")

teams = ["Argentina", "Brazil", 'France', 'Australia', 'England', 'Croatia', 'Portugal', 'Poland', 'Chile', 'Germany', 'Austria', 'Qatar', 'India', 'Japan', 'Titilandia', 'Korea', 'Mexico', 'Italy', 'Ghana', 'Spain', 'Netherlands', 'North Korea', 'Uruguay', 'Saudi Arabia', 'Canada', 'Iceland', 'Nigeria', 'USA', 'China', 'Columbia', 'Denmark', 'Finland']

# We build 8 groups of 4
# groups i a dictionary that gives the LIST of teams in group i. For example group[3] = ["Arg", "Braz",  etc.]
groups = {}
groups_list = []
group = []

# Lets build 8 groups
for g in range(1, 9):
  group = []
  # For a group pick 4 teams
  for t in range(4):
    team = teams[random.randint(0, (len(teams) - 1))]
    teams.remove(team)
    group.append(team)
  groups[g] = group


# Group Stage
print('The Groups are.....')
print()

for i in range(1, 9):
  groups_list = ' '.join(groups[i])
  print(f"Group {i}: {', '.join(groups[i])}")
  group_sound = gtts.gTTS(f'Group {i} {groups_list}')
  group_sound.save('group_sound.mp3')
  playsound('group_sound.mp3')






# Knockouts




# Final