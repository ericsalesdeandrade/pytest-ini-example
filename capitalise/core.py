import time

import logging

# Set Logging
logging.basicConfig(level=logging.BASIC_FORMAT)


def capitalise(value: str) -> str:
    """
    Function to Capitalise a String
    :param value: Input string, str
    :return: Capitalised string
    """
    if isinstance(value, str):
        logging.debug(f"Input Value: {value}")
        # time.sleep(10)  # ADD Delay - Comment if not needed
        cap_value = value.upper()
        logging.info(f"Capitalised Value: {cap_value}")
        return cap_value
    else:
        logging.error("Incorrect Input Value!!")
        raise ValueError("Input Value MUST be string")
