import logging, logging.config
import sys
sys.path.append('../')
from config.settings import CONFIG

# general purpose functions
def open_file(filename):
    """
    Open file function with exceptions treatment
    """
    result = []
    try:
        f = open(filename, 'r')
        for line in f:
            result.append(line)
        f.close()
        return result
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    print('General utils!')