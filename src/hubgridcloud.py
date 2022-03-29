import requests

from src.schema.tags import schema_tag


class Client(object):
    def __init__(self, key):
        self.key = key
        self.url = "https://cloud.hubgridcloud.com/api/v1/"

    def account(self):
        response = requests.get(
            "{}account/profile".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def stacklets(self, tag=""):
        response = requests.get(
            "{}stacklets?tag_name=".format(self.url, tag),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def tags(self):
        response = requests.get(
            "{}tags".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def create_tags(self, data):
        if schema_tag.is_valid(data):
            response = requests.post(
                "{}tags".format(self.url),
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Token {}".format(self.key),
                },
            )
            return response.json()
        else:
            return schema_tag.validate(data)