# python-hubgridcloud
The SimplyStack API allows you to manage Stacklets and resources within the SimplyStack cloud in a simple.

#### Install 
```bash
pip install hubgridcloud
```

#### Examples

```python
from hubgridcloud import Client
client = Client("KEY")
client.account()
client.stacklets()
client.create_tags(data={"name": "test"})
client.tags()
```
