#agent.py

from session.session import Session

class Agent:
    def __init__(self):
        self.session = Session()

    def new_episode(self):
        if self.session.expired():
            self.session = Session()
        self.session.touch()
        return self.session
