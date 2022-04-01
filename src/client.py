import requests

from .schema.tags import schema_tag
from .schema.stacklets import schema_stacklet


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

    def create_stacklets(self, data):
        if schema_stacklet.is_valid(data):
            response = requests.post(
                "{}stacklets".format(self.url),
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Token {}".format(self.key),
                },
            )
            return response.json()
        else:
            return schema_stacklet.validate(data)

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


    def regions(self):
        response = requests.get(
            "{}regions".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def sizes(self):
        response = requests.get(
            "{}sizes".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def distributions(self):
        response = requests.get(
            "{}distributions".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def applications(self):
        response = requests.get(
            "{}applications".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()


    def containers(self):
        response = requests.get(
            "{}containers".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()

    def create_keys(self, data):
        if schema_key.is_valid(data):
            response = requests.post(
                "{}keys".format(self.url),
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Token {}".format(self.key),
                },
            )
            return response.json()
        else:
            return schema_key.validate(data)

    def keys(self):
        response = requests.get(
            "{}keys".format(self.url),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Token {}".format(self.key),
            },
        )
        return response.json()
