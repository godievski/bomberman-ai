from serpent.game import Game

from .api.api import BombermanAPI

from serpent.utilities import Singleton

from serpent.game_launchers.web_browser_game_launcher import WebBrowser


class SerpentBombermanGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "web_browser"

        kwargs["window_name"] = "Safari"
        
        kwargs["url"] = "http://bombergirl.matousskala.cz"
        kwargs["browser"] = WebBrowser.DEFAULT

        super().__init__(**kwargs)

        self.api_class = BombermanAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "GAME_REGION": (148, 124, 693, 540), ##545x416
            "GAME_OVER_REGION": (320,245, 480 ,270),
            "WIN_REGION": (320,245, 480 ,270),
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
