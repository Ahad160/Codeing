import logging

# logging.basicConfig(filename="logFile.log",filemode='w',level=logging.DEBUG,style="{",format="{asctime}:{name}:{levelname}:{message}:{lineno}")

logging.basicConfig(filename="logFile.log",filemode='w',level=logging.DEBUG)


logger = logging.getLogger("Raiden")


logger.debug("Be ware this is a bug")
logger.info("Be ware this is a info")
logger.error("Be ware this is a error")
logger.critical("Be ware this is a CRITICAL")
logger.warning("Be ware this is a warning")










#Defult Style =%()s



