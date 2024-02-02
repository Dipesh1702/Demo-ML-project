import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

Project_name='mlproject'
List_of_Files=[
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/data_ingestion.py",
    f"src/{Project_name}/components/data_transformation.py",
    f"src/{Project_name}/components/model_trainer.py",
    f"src/{Project_name}/components/model_monitering.py",
    f"src/{Project_name}/piplines/__init__.py",
    f"src/{Project_name}/piplines/traning_pipline.py",
    f"src/{Project_name}/piplines/prediction_pipline.py",
    f"src/{Project_name}/exception.py",
    f"src/{Project_name}/logger.py",
    f"src/{Project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in List_of_Files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating Directary:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"created empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exist")

