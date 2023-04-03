import os

from loguru import logger


homeDir = os.path.expanduser('~')
if not os.path.isdir(f"{homeDir}/log"):
    os.mkdir(f"{homeDir}/log")
logger.add(f'{homeDir}/log/test.log',
           format="{time} {level} {message}",
           level="DEBUG",
           rotation="100 MB",
           compression="zip")
