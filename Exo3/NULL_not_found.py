from types import NoneType
from typing import Any

def NULL_not_found(object: Any) -> int:

    print(object)
    if type(object) == NoneType:
        print(f"Nothing : None {object.__class__}")
    elif type(object) == float and str(object) == "nan":
        print(f"Cheese : {object} {object.__class__}")
    elif type(object) == int and object == 0:
        print(f"Zero : 0 {object.__class__}")
    elif type(object) == str and object == "":
        print(f"Empty : {object.__class__}")
    elif type(object) == bool:
        print(f"Fake : {object} {object.__class__}")
    else:
        print("Type not Found")
    return 1