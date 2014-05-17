import logger
from fishfeed import FishTank

logger = logging.getLogger('fishfeed')
h = logging.StreamHandler()
logger.addHandler(h)

fish_tank = FishTank(tank_id='brenda')
fish_tank.monitor()
