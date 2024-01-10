import string

LONG_URL_MAX_LENGHT = 256
SHORT_URL_MAX_LENGHT = 16
SHORT_URL_LENGHT = 6

ALLOW_SHORT_URL_CHARS = string.ascii_letters + string.digits
PATTERN_SHORT_URL = r'^[A-Za-z0-9_]{1,16}$'
PATTERN_LONG_URL = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'

WRONG_LENGTH = 'Некорректная длина ссылки!'
WRONG_BLANK = 'Это поле обязательное для заполнения!'
WRONG_URL = 'Некорректный URL адрес'
WRONG_CHARS_URL = 'Указано недопустимое имя для короткой ссылки'
WRONG_UNIQUE = 'Предложенный вариант короткой ссылки уже существует.'

WRONG_API_ID_NOT_FOUND = 'Указанный id не найден'
WRONG_API_NOT_DATA_IN_REQUEST = 'Отсутствует тело запроса'
WRONG_API_NOT_LONG_URL = '"url" является обязательным полем!'

FORM_LABEL_LONG_URL = 'Ссылка для укорачивания'
FORM_LABEL_SHOT_URL = 'Короткая ссылка'
FORM_LABEL_BUTTON_CREATE = 'Создать ссылку'
