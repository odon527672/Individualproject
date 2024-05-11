from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configure logging
app.logger.setLevel(logging.DEBUG)

# Create a file handler for logging
log_file = 'flask_errors.log'
file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)

# Set the log format
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
file_handler.setFormatter(formatter)

# Add the file handler to the Flask app
app.logger.addHandler(file_handler)

@app.route('/')
def index():
    app.logger.debug('This is a debug message')
    app.logger.info('This is an info message')
    app.logger.warning('This is a warning message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    return 'Hello, Flask!'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)