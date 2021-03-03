# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

import json
import logging


logging.basicConfig(filename='/tmp/log.log',
                    level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s : %(message)s')


def get_color_code(color_name):
    
    color_name = color_name.lower()

    with open('color_check/data/css-color-names.json', 'r') as color_file:
        color_data = color_file.read()

    colors_dict = json.loads(color_data)

    if color_name in colors_dict:
        logging.debug(f'User entered valid color: {color_name} for hex code {colors_dict[color_name]}')
        return colors_dict[color_name]
    else:
        logging.debug(f'User entered INVALID color: {color_name}')
        return 'error'
