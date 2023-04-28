 
import os

# Set up the file structure
project_name = "real-time-data-analysis-with-streamlit-and-kafka"
os.mkdir(project_name)
os.chdir(project_name)

folders = ["data", "kafka", "streamlit", "spark-flink-beam"]
for folder in folders:
    os.mkdir(folder)
    with open(f"{folder}/.gitkeep", "w") as f:
        pass
