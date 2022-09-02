import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable()
logging.debug("start of program....")
for i in range(1,16):
    print(str(i))
    logging.debug('the value of val is '+str(i))
