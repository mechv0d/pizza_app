import hashlib


def md5_hash(input_string, salt):
    """
    Генерирует MD5-хеш строки с добавлением соли.

    Args:
        input_string: Строка, для которой нужно сгенерировать хеш.
        salt: Соль (строка), которая добавляется к строке перед хешированием.

    Returns:
        MD5-хеш строки в шестнадцатеричном представлении.  Возвращает None, если входные данные некорректны.
    """
    if not isinstance(input_string, str) or not isinstance(salt, str):
        return None  # Обработка некорректных входных данных

    salted_string = salt + input_string
    encoded_string = salted_string.encode('utf-8')  # Кодируем строку в UTF-8
    md5_hash = hashlib.md5(encoded_string).hexdigest()
    return md5_hash
