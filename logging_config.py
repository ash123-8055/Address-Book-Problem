import logging


logging.basicConfig(filename='contact_book.log',
                    level=logging.DEBUG,
                    format='%(asctime)s, %(levelname)s %(message)s',
                    filemode='a')

logger=logging.getLogger()
