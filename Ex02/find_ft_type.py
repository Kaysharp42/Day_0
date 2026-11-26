from typing import Any

def all_thing_is_obj(object: Any) -> int:
    if type(object) in [list, tuple, set, dict]:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    elif type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42