# unicode-segmentation-py

```python

>>> import unicode_segmentation
>>> [g.decode("utf-8") for g in unicode_segmentation.graphemes("a̐éö̲\r\n".encode("utf-8"))]
["a̐", "é", "ö̲", "\r\n"]
```
