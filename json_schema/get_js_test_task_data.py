from jsonschema import validate


def check_json_schema(instance, search_word):
    schema = {
        'type': 'object',
        'properties': {
            'total_count': {'type': 'integer'},
            'current_page': {'type': 'integer'},
            'previous_page_url': {'type': 'boolean'},
            'next_page_url': {'type': 'string'},
            'products': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'pattern': search_word},
                        'image': {'type': 'string'},
                        'price': {'type': 'integer', 'minimum': 0}
                    }
                }
            }
        }
    }
    validate(instance=instance, schema=schema)
