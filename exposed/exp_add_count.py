from app.data import main_data
import eel


def add_count() -> float:
    main_data.count += 1
    return main_data.count
