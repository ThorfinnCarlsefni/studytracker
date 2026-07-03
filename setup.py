from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
import shutil
import sys

def copy_web_files():
    """Копирует веб-файлы в текущую директорию"""
    try:
        current_dir = os.getcwd()
        
        # Ищем где находятся файлы (несколько возможных путей)
        possible_paths = []
        
        # Путь при обычной установке
        import studytracker
        pkg_dir = os.path.join(os.path.dirname(studytracker.__file__), 'web')
        possible_paths.append(pkg_dir)
        
        # Путь при разработке (editable install)
        local_web = os.path.join(os.path.dirname(__file__), 'studytracker', 'web')
        possible_paths.append(local_web)
        
        web_dir = None
        for path in possible_paths:
            if os.path.exists(path):
                web_dir = path
                break
        
        if not web_dir:
            print("❌ Не удалось найти веб-файлы")
            return
        
        target_dir = os.path.join(current_dir, 'studytracker-web')
        
        # Копируем
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree(web_dir, target_dir)
        
        print(f"""
╔══════════════════════════════════════════════════════╗
║  ✅ Файлы StudyTracker скопированы!                  ║
║                                                      ║
║  📁 {target_dir}
║                                                      ║
║  🚀 Открой index.html в браузере!                   ║
╚══════════════════════════════════════════════════════╝
        """)
    except Exception as e:
        print(f"⚠️  Не удалось скопировать файлы: {e}")

class PostInstallCommand(install):
    def run(self):
        super().run()
        self.execute(copy_web_files, [], msg="Копирование веб-файлов...")

class PostDevelopCommand(develop):
    def run(self):
        super().run()
        self.execute(copy_web_files, [], msg="Копирование веб-файлов...")

setup(
    name="studytracker",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "studytracker=studytracker.cli:main",
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
        'develop': PostDevelopCommand,
    },
)