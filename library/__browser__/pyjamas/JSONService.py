# this you do not do in pyjs!
def create_object(items):
    return items

# nor call object_hook!
def _decode_response(self, json_str):
    return loads(json_str)

