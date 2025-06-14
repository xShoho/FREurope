import os
import logging
from logging.handlers import RotatingFileHandler


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok= True)


def init_logger(name: str = "scrapper") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        return logger
    
    formatter = logging.Formatter(
        fmt= "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt= "%d/%m/%Y %H:%M:%S"
    )
    
    # INFO handler
    
    info_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, f"{ name }_info.log"),
        maxBytes= 5_000_000,
        backupCount= 10
    )
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    
    # WARNING handler
    
    warning_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, f"{ name }_warning.log"),
        maxBytes= 5_000_000,
        backupCount= 10
    )
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)
    
    # ERROR handler
    
    error_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, f"{ name }_error.log"),
        maxBytes= 5_000_000,
        backupCount= 10
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    
    logger.addHandler(warning_handler)
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    
    return logger