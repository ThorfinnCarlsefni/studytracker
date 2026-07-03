import os
import shutil

def export_web_files(target_dir=None):
    """
    Экспортирует веб-файлы в указанную директорию.
    Если директория не указана, создает папку 'studytracker-web' в текущей директории.
    """
    source_dir = os.path.join(os.path.dirname(__file__), 'web')
    
    if target_dir is None:
        target_dir = os.path.join(os.getcwd(), 'studytracker-web')
    
    # Копируем файлы
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    shutil.copytree(source_dir, target_dir)
    
    print(f"""
✅ Файлы экспортированы в: {target_dir}

📂 Структура:
   {target_dir}/
   ├── index.html
   ├── css/
   │   └── style.css
   └── js/
       └── app.js

💡 Просто откройте index.html в браузере!
    """)
    
    return target_dir

if __name__ == "__main__":
    export_web_files()