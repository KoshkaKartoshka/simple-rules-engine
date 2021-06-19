PROKLADA is rules engine 
made to accept people have a dialog 
with your system through rules they/you have created

To run tests install pytest and fo 
```bash
$ pytest tests/
```

# How to use?

So, we have rules, they look like this (don`t forget, that it has to be list of rules)
```python
{
    "name": "Jolteon first rule",   # just some text, better to keep unique
    "description": "o.O",           # just some text

    "first_value": "name",          # value that we will use
    "first_value_type": "str",      # we will convert our value to this type
    "first_value_from_data": True,  # [optional key] we will get value from data, not from rule if it is True

    "second_value": "3",
    "second_value_type": "str",

    "operation": "ge",              # operation that we want to do with our two values (no less 2, no more 2)
}
```

Besides, we have data, let it be like this:
```python
{
    "name": "Zuhra",
    "age": 24,
    "ears_count": 2,
    "eyes_count": 2,
    "fingers_count": 20,
}
```

And then our Prokladka takes these two objects and does magic.

