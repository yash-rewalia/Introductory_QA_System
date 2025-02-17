import os
from pathlib import Path

list_files = [
    'scripts/__init__.py',
    'scripts/data_ingestion.py',
    'scripts/model_api.py',
    'scripts/embedding.py',
    'streamlitapp.py',
    'logger.py',
    'exception.py',
    'setup.py'
]

for file in list_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)

    if  (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, 'w') as f:
            pass
