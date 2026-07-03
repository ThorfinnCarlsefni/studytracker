import os
import sys
import shutil
import webbrowser

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'export':
            export_files()
            return
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("""
StudyTracker - Систематизация обучения

Команды:
  studytracker          Запуск веб-сервера
  studytracker export   Копирование файлов в текущую папку
  studytracker --help   Эта справка
            """)
            return
    
    # Запуск сервера
    from .server import run_server
    web_dir = os.path.join(os.path.dirname(__file__), 'web')
    print("🚀 Запуск StudyTracker...")
    webbrowser.open('http://127.0.0.1:5000')
    run_server(web_dir)

def export_files():
    """Копирует файлы в текущую папку"""
    current_dir = os.getcwd()
    source_dir = os.path.join(os.path.dirname(__file__), 'web')
    target_dir = os.path.join(current_dir, 'studytracker-web')
    
    try:
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        
        shutil.copytree(source_dir, target_dir)
        
        print(f"""
✅ Файлы скопированы в: {target_dir}

📂 Содержимое:
   ├── index.html
   ├── css/
   │   └── style.css
   └── js/
       └── app.js

💡 Откройте index.html в браузере!
        """)
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()