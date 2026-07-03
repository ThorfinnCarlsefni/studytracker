from setuptools import setup, find_packages
from setuptools.command.install import install
import shutil
import os

class PostInstallCommand(install):
    """Копирует веб-файлы в текущую папку после установки"""
    def run(self):
        install.run(self)
        
        # Получаем текущую папку (где запущен pip install)
        current_dir = os.getcwd()
        
        # Путь к веб-файлам внутри пакета
        pkg_dir = os.path.join(self.install_lib, 'studytracker', 'web')
        
        # Куда копировать
        target_dir = os.path.join(current_dir, 'studytracker-web')
        
        if os.path.exists(pkg_dir):
            # Копируем файлы
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            shutil.copytree(pkg_dir, target_dir)
            
            print(f"""
╔══════════════════════════════════════════════════════╗
║  ✅ Файлы StudyTracker скопированы!                  ║
║                                                      ║
║  📁 Расположение: {target_dir}
║                                                      ║
║  🚀 Просто открой index.html в браузере!            ║
╚══════════════════════════════════════════════════════╝
            """)

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
    },
)