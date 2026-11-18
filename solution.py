import uuid

def solve(value):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, value))
