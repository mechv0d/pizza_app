from typing import Any
from app.data import main_data as data, debug

import eel


@eel.expose
def data_get(property_name: str) -> Any:
    attr = data.__getattribute__(property_name)
    if debug:
        print(f'Return as {property_name}: {attr}')
    return attr
