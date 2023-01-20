from schema import Schema

schema_stacklet = Schema(
    {
        "name": str,
        "size": str,
        "region": str,
        "image": str,
        "backups": bool,
        "private_networking": bool,
        "tags": list,
        "ssh_keys": list,
        "password": str,
    }
)
