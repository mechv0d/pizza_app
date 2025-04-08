import eel


@eel.expose
def load_component() -> str: #path: str
    print('hello')
    return 'hi!'
    # try:
    #     with open(path, 'r', encoding='utf-8') as file:
    #         return file.read()
    # except Exception as _:
    #     return f"IO Error: Couldn't resolve file in path `{path}`"
