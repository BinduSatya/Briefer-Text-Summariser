import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Briefer-Text-Summariser'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    # Create directories if they don't exist
    if filepath.parent != "":
        if not filepath.parent.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {filepath.parent}")
        else:
            logging.info(f"Directory already exists: {filepath.parent}")
    
    # Create empty files if they don't exist or are empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

