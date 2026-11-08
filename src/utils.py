import sys
from dataclasses import dataclass
import os
import pandas as pd
import numpy as np
from src.logger import logging
from src.exceptions import CustomException
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            import pickle
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)