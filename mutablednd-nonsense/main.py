import random
from datetime import datetime
import d20
rand = random.Random()
seed = datetime.now().microsecond * datetime.now().second
rand.seed(seed)

print(d20.roll("1d20"))