import json
from os.path import exists
from typing import Callable, Iterable, Union


def json_or_fetch(keys: Union[str, Iterable[str]], fetcher: Callable, path: str=None, reload: bool=False) -> dict:
    """
    Loads JSON data from path, then iterates through the keys collection to see if any data is not present.
    
    If that is the case, then it will use the fetcher callback on the key element to get the data and add it.

    If data was added, it saves the data to the path as a new JSON file.

    :param keys: Iterable of keys with which to store and get data.
    :param fetcher: Callback function for retrieving data. Should take a key as argument.
    :param path: Path to the JSON file.
    :param reload: If True, will reload data from the fetcher callback even if it is already in the JSON file.
    
    :returns: Data in a dict.
    """
    # You could make it so only the keys provided are retrieved in the final dict.
    # You would make a clone that gets the data from the existing dict if the keys match, and otherwise finds new data.
    # Any key in the original that was not provided to be retrieved would be ignored.
    # New entries would be added to the existing dict so that it can be saved to the file.
    # Alternatively, you could save the returned dict to file, essentially deleting any data that was not retrieved.
    
    if isinstance(keys, str):
        keys = keys,
    
    # init empty dict
    data = {}
    changed = False
    # loads from json file if exists
    if path and exists(path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

    # if data from collection is not in the existing json file (or we reload), we get data from callback
    for key in keys:
        if key not in data.keys() or reload:
            data[key] = fetcher(key)
            changed = True

    # overwrite existing json file with fresh data if something new was added
    if path and changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    
    return data