from app.data import main_data
import eel

@eel.expose
def add_count():
    main_data.count += 1
    return main_data.count
