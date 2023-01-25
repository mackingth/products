import logging
import os
logging.basicConfig(level=logging.DEBUG)
from app import server
if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=8080)