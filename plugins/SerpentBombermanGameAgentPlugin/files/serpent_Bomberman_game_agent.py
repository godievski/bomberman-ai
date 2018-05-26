import time
import os
import pickle
#import serpent.cv

import numpy as np
import collections

from datetime import datetime


from serpent.frame_transformer import FrameTransformer
from serpent.frame_grabber import FrameGrabber
from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey

#from .helpers.game_status import Game
#from .helpers.terminal_printer import TerminalPrinter
#from .helpers.ppo import SerpentPPO


import random

class SerpentBombermanGameAgent(GameAgent):

		def __init__(self, **kwargs):
				super().__init__(**kwargs)

				self.frame_handlers["PLAY"] = self.handle_play

				self.frame_handler_setups["PLAY"] = self.setup_play
				self.frame_handler_setups["GAME_OVER"] = self.setup_gameover
				self.frame_handler_setups["START_GAME"] = self.setup_gameover

		def setup_play(self):
				game_inputs = {
						"Move Up": [KeyboardKey.KEY_UP],
						"Move Down": [KeyboardKey.KEY_DOWN],
						"Move Left": [KeyboardKey.KEY_LEFT],
						"Move Right": [KeyboardKey.KEY_RIGHT],
						"Leave Bomb": [KeyboardKey.KEY_SPACE]
				}
				self.game_inputs = game_inputs

				#self.ppo_agent = SerpentPPO(
				#		frame_shape=(125, 112, 4),
				#		game_inputs=game_inputs
				#)

				self.first_run = True
				self.game_over = False
				self.run_count = 0
				self.run_reward = 0

		def setup_gameover(self):
			game_inputs = {
				"Play again": [KeyboardKey.KEY_ENTER]
			}


		def handle_play(self, game_frame):
				inputs = [KeyboardKey.KEY_UP, KeyboardKey.KEY_DOWN,
									KeyboardKey.KEY_LEFT, KeyboardKey.KEY_RIGHT,
									KeyboardKey.KEY_SPACE]
									
				self.input_controller.tap_key(inputs[random.randint(0,4)])
