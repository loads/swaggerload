from swagger_parser import SwaggerParser
from pprint import pprint

parser = SwaggerParser(swagger_path='shavar.yaml')


print('Endpoints:')
print('')
for path, spec in parser.specification['paths'].items():
    print('%s %s' % (list(spec.keys())[0].upper(), path))

#pprint(parser.specification['info'])
