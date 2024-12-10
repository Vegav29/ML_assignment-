import os

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define data paths
DATA_PATH_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PATH_INTERIM = os.path.join(BASE_DIR, "data", "interim")
DATA_PATH_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
FIGURES_PATH = os.path.join(BASE_DIR, "figures")