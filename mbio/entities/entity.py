
class Entity(object):
    RELEASE, RECORDING = range(0,2)
    def __init__(self, *args, **kwargs):
        pass

    def json(self):
        raise NotImplementedError

    def parse_json(self, json):
        raise NotImplementedError
