#!/usr/bin/env python3

from sys import argv, exit
from svgnarrative import Model
import json

earth_prefix = 'earth'

def read_description (filename):
    with open(filename) as fo:
        return json.load(fo)

# handle command-line arguments
if len(argv) != 6:
    print('Syntax: %s PATH_TO_JSON_DESCRIPTION PATH_TO_TEMPLATE PATH_TO_MAP PATH_TO_ROAST OUTPUT_FILENAME' % argv[0])
    print('        %s ../var/coffees/kenya_matunda.json ../var/templates/default.svg ../var/templates/roast.svg ../var/templates/World_map_blank_with_blue_sea.svg kenya_matunda.svg' % argv[0])
    exit(1)
description_filename = argv[1]
template_filename    = argv[2]
map_filename         = argv[3]
roast_filename       = argv[4]
output_filename      = argv[5]

template    = Model(template_filename)
earth       = Model(map_filename)
roast       = Model(roast_filename)
description = read_description(description_filename)

template.set_text('name', description['name'])
template.insert(earth, earth_prefix, 15, 10, 0.03)
template.fill(map(lambda o: '%s%s' % (earth_prefix, o), description['origin']), '#880000')
for i in range(2):
    roast_prefix = 'roast%d' % i
    template.insert(roast, roast_prefix, 5, 60+70*i)
    template.set_text('%stspan2411-1-5'%roast_prefix, description['date'] if 'date' in description else '')
    

template.store(output_filename)

