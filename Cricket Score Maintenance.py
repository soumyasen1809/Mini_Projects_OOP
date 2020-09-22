# https://www.codewithc.com/cricket-score-sheet-project-c/
# Cricket Score Maintenance - OOP to maintain a cricket team

import random


class Player:                                   # Defining the class Player with name and team
    def __init__(self, name, team):
        self.name = name
        self.team = team


class Bowler(Player):                           # subclass Bowler inheriting from Player class
    wicket = 0

    def __init__(self, name, team):
        Player.__init__(self, name, team)

    def addWicket(self):
        self.wicket = self.wicket + 1           # adding a wicket count to the bowler when successfully takes a wicket


class Batsman(Player):
    run = 0
    balls_played = 0

    def __init__(self, name, team):
        Player.__init__(self, name, team)

    def addRun(self, run_hit):
        self.run_hit = run_hit                  # adding run count to the batsman when successfully scores run
        self.run = self.run + run_hit           # run_hit is the runs hit by the batsman in a ball (values from 0 to 6)

    def addBallsPlayed(self):
        self.balls_played = self.balls_played + 1       # number of balls played by the batsman


class MatchScore:                               # class defines the various operations in a cricket match

    def __init__(self, batsquad, bowlsquad):    # takes the entire batting and bowling squad
        self.batsquad = batsquad
        self.bowlsquad = bowlsquad

    def takeRun(self):
        play_num = random.randint(0,1)          # randomly chooses from the 1st two batsmen (players currently on field)
        self.batsquad[play_num].addRun(random.randint(0,6))     # batsman randomly hits a run (from 0 to 6)
        self.batsquad[play_num].addBallsPlayed()                # 1 ball played added to the batsman

    def takeWicket(self):
        play_num = random.randint(0, len(bowlsquad)-1)    # randomly chooses from all bowlers (players currently on field)
        self.bowlsquad[play_num].addWicket()                    # bowler takes a wicket
        self.batsquad[0].addBallsPlayed()                       # 1 ball played added to the batsman (wicket drop ball)
        for i in range(len(batsquad) - 1):
            batsquad[i], batsquad[i + 1] = batsquad[i + 1], batsquad[i]     # Push the batsman to the back (don't pop)


# Squad lineup
Bats1 = Batsman("Kevin Peterson", "England")
Bats2 = Batsman("Ricky Ponting", "England")
Bats3 = Batsman("Brian W. Lara", "England")
Bats4 = Batsman("Adam Gilchrist", "England")
Bowl1 = Bowler("Shane M. Warne", "Australia")
Bowl2 = Bowler("Nathan P. Bold", "Australia")
batsquad = [Bats1, Bats2, Bats3, Bats4]        # Create list of batting squad
bowlsquad = [Bowl1, Bowl2]                     # Create list of bowling squad

# Game play
wick_count = 0
balls_count = 0
for i in range(0, 20):                         # Playing a max of 20 balls
    input_val = random.randint(0,1)            # Randomly playing the game - if 0: run scored, if 1: wicket drop
    if wick_count < len(batsquad):             # Check if all wickets have fallen already
        balls_count = balls_count + 1
        if input_val == 0:
            MatchScore(batsquad, bowlsquad).takeRun()
        else:
            MatchScore(batsquad, bowlsquad).takeWicket()
            wick_count = wick_count + 1


# Printing the score-card
print ("-------------- England vs Australia -------------- \n")
print ("-------------- England Batting --------------")
print ("Name of player" + "\t" + "Runs" + "\t" + "Balls")
for i in range(len(batsquad)):
    print (str(batsquad[i].name) + "\t" + str(batsquad[i].run) + "\t \t" + str(batsquad[i].balls_played))

print ("-------------- Australia Bowling --------------")
print ("Name of player" + "\t" + "Wickets taken")
for i in range(len(bowlsquad)):
    print (str(bowlsquad[i].name) + "\t \t" + str(bowlsquad[i].wicket))

print ("-------------- Total Stats --------------")
total_runs = 0
for i in range(len(batsquad)):
    total_runs = total_runs + batsquad[i].run
print ("Total runs scored:" + "\t" + str(total_runs))
print ("Total balls delivered:" + "\t" + str(balls_count))
print ("Total wickets taken:" + "\t" + str(wick_count))
