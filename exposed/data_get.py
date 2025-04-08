from typing import Any
from app.data import main_data as data

import eel


@eel.expose
def data_get(property_name: str) -> Any:
    return data.__getattribute__(property_name)
