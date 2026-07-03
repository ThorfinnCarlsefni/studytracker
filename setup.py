from setuptools import setup, find_packages

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
)