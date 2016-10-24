from swagger_parser import SwaggerParser
from pprint import pprint

parser = SwaggerParser(swagger_path='api-with-examples.yaml')

pprint(parser.specification['info'])

