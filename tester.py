from swagger_parser import SwaggerParser
from pprint import pprint
from urllib.parse import urlunparse


from ops import get_operation
import test_shavar


parser = SwaggerParser(swagger_path='shavar.yaml')

host = parser.specification['host']
schemes = parser.specification.get('schemes', ['https'])
scheme = schemes[0]


for path, spec in parser.specification['paths'].items():
    for verb, options in spec.items():
        operation = options['operationId']
        func = get_operation(options['operationId'])
        endpoint = urlunparse((scheme, host, path, '', '', ''))
        verb = verb.upper()
        print('Checking %s %s...' % (verb, endpoint))
        try:
            func(verb, endpoint, **options)
            print('OK')
        except Exception:
            print('FAIL')
