class GameStats:
    """Track statistics of the game"""

    def __init__(self, igame) -> None:
        """Initialize statistics"""
        self.settings = igame.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
