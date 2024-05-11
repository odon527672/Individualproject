import logging
import configparser
import argparse
from pynput import mouse

# Custom MouseEventHandler class to handle mouse events
class MouseEventHandler:
    def __init__(self, config):
        self.show_events = config.getboolean('Settings', 'show_events', fallback=True)
        self.show_clicks = config.getboolean('Settings', 'show_clicks', fallback=True)
        self.show_moves = config.getboolean('Settings', 'show_moves', fallback=True)
        self.show_scroll = config.getboolean('Settings', 'show_scroll', fallback=True)
        self.log_file = config.get('Settings', 'log_file', fallback=None)

        # Configure logging to file if log_file is specified
        if self.log_file:
            logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_move=self.on_move,
            on_scroll=self.on_scroll
        )

    def start(self):
        self.mouse_listener.start()
        self.mouse_listener.join()

    def on_click(self, x, y, button, pressed):
        if self.show_events and self.show_clicks:
            action = 'Click ({}): {}'.format('Pressed' if pressed else 'Released', button)
            self.log_action(action)

    def on_move(self, x, y):
        if self.show_events and self.show_moves:
            action = 'Move: ({}, {})'.format(x, y)
            self.log_action(action)

    def on_scroll(self, x, y, dx, dy):
        if self.show_events and self.show_scroll:
            action = 'Scroll: ({}, {})'.format(dx, dy)
            self.log_action(action)

    def log_action(self, action):
        if self.log_file:
            logging.info(action)
        else:
            print(action)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Command line mouse event logger')
    parser.add_argument('-c', '--config', type=str, default='config.ini', help='Path to configuration file')
    args = parser.parse_args()

    # Read configuration file
    config = configparser.ConfigParser()
    config.read(args.config)

    # Initialize and start mouse event handler
    event_handler = MouseEventHandler(config)
    event_handler.start()

if __name__ == '__main__':
    main()
