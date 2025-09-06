import config_log # you can configure logging here, it is enough to import this module
import logging
import app
import sys

logging.info('config_log module imported successfully.')

cube_app = app.Display()
logging.info('App instance created successfully.')

try:
    cube_app.inizialize()
    logging.info('App initialized successfully.')

    cube_app.run()
    logging.info('App run method executed successfully.')
except Exception as e:
    logging.critical(f"Unhandled exception in main: {e}", exc_info=True)
    sys.exit('critical error in main, exiting...')
finally:
    logging.info('exit from the code...')