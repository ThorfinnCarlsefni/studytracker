import os
import sys
import webbrowser
from .server import run_server

def main():
    # Получаем путь к веб-файлам
    web_dir = os.path.join(os.path.dirname(__file__), 'web')
    
    print(f"""
StudyTracker - готов к использованию!

📁 Файлы приложения находятся здесь:
   {web_dir}

🚀 Запуск веб-сервера...
    """)
    
    # Запускаем сервер и открываем браузер
    webbrowser.open('http://127.0.0.1:5000')
    run_server(web_dir)