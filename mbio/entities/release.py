from mbio.entities.entity import Entity
from mbio.utils import get_json
import datetime
import json

class Release(Entity):
    def __init__(self, data, *args, **kwargs):
        super(Release, self).__init__(*args, **kwargs)

        if isinstance(data, str):
            self.mbid = data
            json_struct = get_json("https://musicbrainz.org/ws/2/release/"+self.mbid+"?fmt=json")
        else:
            json_struct = data

        self.parse_json(json_struct)

    def json(self):
        json_struct = {}
        json_struct['country'] = self.country
        json_struct['status'] = self.status
        json_struct['date'] = datetime.datetime.strftime(self.date,"%Y-%m-%d")
        json_struct['barcode'] = self.barcode
        json_struct['disambiguation'] = self.disambiguation
        json_struct['title'] = self.title
        json_struct['asin'] = self.asin
        json_struct['quality'] = self.quality
        json_struct['packaging'] = self.packaging

        return json.dumps(json_struct, ensure_ascii=False).decode('utf-8')

    def parse_json(self, json_struct):
        self.country = json_struct['country']
        self.status = json_struct['status']
        self.date = datetime.datetime.strptime(json_struct['date'], "%Y-%m-%d")
        self.barcode = json_struct['barcode']
        self.disambiguation = json_struct['disambiguation']
        self.title = json_struct['title']
        self.asin = json_struct['asin']
        self.quality = json_struct['quality']
        self.packaging = json_struct['packaging']

        if "media" in json_struct:
            for m in json_struct['media']:
                for t in m['track']:
                    print("Doing recordings!")
