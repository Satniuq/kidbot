import time
from state.state import State
from state.memory import Memory

class Session:
    def __init__(self):
        self.state = State()
        self.memory = Memory()
        self.started_at = time.time()
        self.last_interaction = None

    def touch(self):
        self.last_interaction = time.time()

    def expired(self, timeout=120):
        if self.last_interaction is None:
            return False
        return (time.time() - self.last_interaction) > timeout

