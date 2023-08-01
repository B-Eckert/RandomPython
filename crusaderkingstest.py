import random
from datetime import datetime
threshhold = 72
x = []
rand = random.Random()
seed = datetime.now().microsecond * datetime.now().second
rand.seed(seed)

class Stats:
    def __init__(self, diplomacy, stewardship, intrigue, martial, learning):
        self.stats = [diplomacy, stewardship, intrigue, martial, learning]
class Lord:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
class fief:
    def __init__(self):
        return
    
def year(lordset, fiefset):
    # do stuff
    return