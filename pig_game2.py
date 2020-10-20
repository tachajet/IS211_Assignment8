from random import randint,seed
from time import time
import argparse
seed(0)

class Dice:
		"""
		This program unfortunately does not work as I'd hoped, but at least I think I can explain why
		"""
		@staticmethod
		def roll():
			return randint(1, 6)


class Player:
		"""
		Dice and Player classes are OK, I think
		"""
		def __init__(self):
				self.total_score = 0
				self.play = True
				self.human = True

		
class ComputerPlayer(Player):
	"""
	Class that creates a Computer version of the Player object.
	"""
	human = False
class PlayerFactory:

	def __init__(self):
		return None

	def createPlayer(player_type):
		"""Man or machine?"""

		if player_type.upper()== "HUMAN":
			return Player()
		elif player_type.upper()=="COMPUTER":
			return ComputerPlayer()
		else:
			print("Neither human nor machine!")
			


class Pig:
		
		def __init__(self, pig_players):
			self.pig_players=pig_players
		def play(self):
				# this is the current player
				p = 0
				winner = False
				current_player = self.pig_players[p]
				if not current_player.human:
					print(p)
					print(p.human)
					while not winner:
						current_player.play = True
						while current_player.play:
							roll_score = Dice.roll()
							print("test")
							current_score = 0
							low_score=25
							high_score=(100 - current_player.score)
							if low_score <= high_score:
								mk_point = low_score
							else:
								mk_point = high_score
							if current_score>=mk_point:
								roll_score = Dice.roll()
								if roll_score == 1:
									print(f"Sorry Computer! You have rolled a 1 and your turn is over.")
									current_player.play = False
								else:
									current_score += roll_score
									print(f"Congratulations Computer! You rolled a {roll_score}, "
															f" and your current score is {current_score} "
															f" and your possible total score is {current_player.total_score + current_score} "
															)
									if current_player.total_score + current_score >= 100:
										winner = True
										current_player.play = False
										current_player.total_score += current_score
										print(f"The Computer is the winner with {current_player.total_score}")
							else:
								current_player.total_score += current_score
								print(current_player.total_score)
								current_player.play = False
							if not winner:
								p += 1
								if p == len(self.pig_players):
									p = 0
				else:
					print(p)
					while not winner:
						# Looping through the player objects doesn't work
						# once you run out of players! It just terminates the loop without meeting endgame conditions.
						# I should have broken this up further for any hope of making it functional
						current_player.play = True
						current_score = 0
						while current_player.play:
							choice = input(f"Human, would you like to hold (h) or  roll (r)? ")
							if choice.upper() == "H":
									current_player.total_score += current_score
									current_player.play = False
							elif choice.upper() == "R":
									roll_score = Dice.roll()
									if roll_score == 1:
											print(f"Sorry Human! You have rolled a 1 and your turn is over.")
											current_player.play = False
									else:
											current_score += roll_score
											print(f"Congratulations Human, you rolled a {roll_score}, "
															f" and your current score is {current_score} "
															f" and your possible total score is {current_player.total_score + current_score} "
															)
												# check if the current player won
											if current_player.total_score + current_score >= 100:
													winner = True
													current_player.play = False
													current_player.total_score += current_score
													print(f"The Human is the winner with {current_player.total_score}")
							else:
									print("Not a valid input, please try again")
						else:
							current_player.total_score += current_score
							current_player.play = False
							
						if not winner:
							p += 1
							if p == len(self.pig_players):
								p = 0# Move to next player
				
class TimedPig(Pig):
	"""Timed version of pig
	"""
	def __init__(self):
		self.start_game=time()
		

def main():
		parser = argparse.ArgumentParser()
		parser.add_argument('--player1', type=str, default="computer")
		parser.add_argument('--player2', type=str, default="computer")
		args = parser.parse_args()
		pig_game_maker = PlayerFactory
		pig_game_player_one=pig_game_maker.createPlayer(args.player1)
		pig_game_player_two=pig_game_maker.createPlayer(args.player2)
		pig_game=Pig([pig_game_player_one,pig_game_player_two])
		pig_game.play()

if __name__ == "__main__":
		main()

