# python-hubgridcloud
The SimplyStack API allows you to manage Stacklets and resources within the SimplyStack cloud in a simple.

#### Install 
```bash
pip install hubgridcloud
```

#### Examples

```python
from hubgridcloud.client import Client
client = Client("KEY")
client.account()
client.stacklets()
client.create_tags(data={"name": "test"})
client.tags()
client.create_stacklets(data={"size": "b-1vcpu-1gb", "region": "fra", "private_networking": False, "name": "test", "image": "ubuntu-20-04-4-x64", "backups": False, "tags": []})
client.regions()
client.sizes()
client.distributions()
client.applications()
client.containers()
```
