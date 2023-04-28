import json
from os.path import exists
from typing import Callable, Iterable, Union


def json_or_fetch(fetcher: Callable,
                  keys: Union[str, Iterable[str]],
                  args: Union[tuple, tuple[tuple]]=None,
                  kwargs: Union[dict, tuple[dict]]=None,
                  path: str=None,
                  reload: bool=False
                  ) -> dict:
    """
    Loads JSON data from path, then iterates through the keys collection to see if any data is not present.
    
    If that is the case, then it will use the fetcher callback with corresponding args and kwargs to get the data and add it.

    If data was added, it saves the data to the path as a new JSON file.
    
    Keys can be a single string, or an iterable of strings. If it is a single string, then args and kwargs must be a single tuple and dict.
    
    If the same args or kwargs are used for all keys, then you can use `functools.partial` to create a new function with those arguments.
    It would be nice if giving a single tuple or dict would be interpreted as the same args or kwargs for all keys, but that is currently not supported.

    :param keys: Iterable of keys with which to store and get data.
    :param fetcher: Callback function for retrieving data.
    :param args: Iterable of tuples of args to pass to the callback.
    :param kwargs: Iterable of dicts of kwargs to pass to the callback.
    :param path: Path to the JSON file.
    :param reload: If True, will reload data from the fetcher callback even if it is already in the JSON file.
    
    :returns: Data in a dict.
    """
    # Process if keys is a single string.
    # I assume that the shape of args and kwargs fit if the keys is a single string.
    if isinstance(keys, str):
        keys = keys,
        args = (args,) if args else None
        kwargs = (kwargs,) if kwargs else None
    
    # Process if args and kwargs are None.
    if args is None:
        args = ((),)*len(keys)
        
    if kwargs is None:
        kwargs = ({},)*len(keys)
        
    # Also a way to assign if falsy.
    # args = args or ((),)*len(keys)
    # kwargs = kwargs or ({},)*len(keys)
    
    # init empty dict
    data = {}
    changed = False
    # loads from json file if exists
    if path and exists(path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

    # if data from collection is not in the existing json file (or we reload), we get data from callback
    for key, arg, kwarg in zip(keys, args, kwargs):
        if key not in data or reload:
            data[key] = fetcher(*arg, **kwarg)
            changed = True

    # overwrite existing json file with fresh data if something new was added
    if path and changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    
    return data

# You could make it so only the keys provided are retrieved in the final dict.
# You would make a clone that gets the data from the existing dict if the keys match, and otherwise finds new data.
# Any key in the original that was not provided to be retrieved would be ignored.
# New entries would be added to the existing dict so that it can be saved to the file.
# Alternatively, you could save the returned dict to file, essentially deleting any data that was not retrieved.