import os
import logging

from config import *

logging.basicConfig(level=logging.INFO)


def send_to_asr_api(filename):
    result = os.popen(
        "{binary} -P {port} -p '{bearer}' -addr {addr} -w {filename} -verbose".format(
            binary=BINARY,
            port=PORT,
            bearer=BEARER,
            addr=ADDR,
            filename=filename,
        )).read()

    command = result.strip().split("\n")[-2]
    logging.info("Recognized command: {}".format(command))
    return command


def main():
    pass


if __name__ == '__main__':
    send_to_asr_api("sample16kHz.wav")
