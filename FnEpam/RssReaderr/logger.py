"""logger redefinition"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger()
