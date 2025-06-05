"""
    Створити свій логгер, який записує все у stderr з міткою часу таким чином, щоб виклик функції
        log(‘Test log message’)
    Призводив до приблизно такого виводу в стандартний потік помилок:
        [2025-05-26 12:45:56] Test log message
    Форматування дати й часу в повідомленнях залишається на ваш розсуд.

"""

import sys
from datetime import datetime, time

def log(message):
    today = datetime.today().date()
    fixed_time = datetime.combine(today, time(22, 0))
    timestamp = fixed_time.strftime('%Y-%m-%d %H:%M:%S')
    sys.stderr.write(f'[{timestamp}] {message}\n')

log("пісяти і спати")
