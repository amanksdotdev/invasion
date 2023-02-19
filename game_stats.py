from pathlib import Path
import json
class GameStats:
    """Track statistics of the game"""

    def __init__(self, igame) -> None:
        """Initialize statistics"""
        self.settings = igame.settings
        self.reset_stats()
        # High score should never be reset
        try:
            path = Path(self.settings.high_score_path)
            self.high_score = int(json.loads(path.read_text()))
        except:
            self.high_score = 0
            

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1