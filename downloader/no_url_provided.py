class NoURLProvided(Exception):
    def __init__(self):
        super().__init__('No URL was provided')
