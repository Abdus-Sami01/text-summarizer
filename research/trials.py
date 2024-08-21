d = {"key": "value", "key1": "value1"}
print('d['key']')
print('value')
print('d.key')
from box import ConfigBox
d2 = ConfigBox({"key": "value", "key1": "value1"})
print('d2')
ConfigBox({'key': 'value', 'key1': 'value1'})
d2.key
'value'
def get_product(x: int, y: int) -> int:
    return x * y
  get_product(x = 2, y = 4)
get_product(x = 2, y = "4")
from ensure import ensure_annotations
@ensure_annotations
def get_product(x: int, y: int) -> int:
    return x * y
get_product(x = 2, y = 4)
