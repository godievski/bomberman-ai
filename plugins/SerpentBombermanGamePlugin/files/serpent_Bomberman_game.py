from serpent.game import Game

from .api.api import BombermanAPI

from serpent.utilities import Singleton

from serpent.game_launchers.web_browser_game_launcher import WebBrowser


class SerpentBombermanGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "web_browser"

        kwargs["window_name"] = "Safari"
        
        kwargs["url"] = "https://gd-bomberman.herokuapp.com"
        kwargs["browser"] = WebBrowser.DEFAULT

        super().__init__(**kwargs)

        self.api_class = BombermanAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "GAME_REGION": (0, 0, 545, 416), ##545x416
            "GAME_OVER_REGION": (0,0, 160 ,25),
            "WIN_REGION": (0,0, 160 ,25),
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
