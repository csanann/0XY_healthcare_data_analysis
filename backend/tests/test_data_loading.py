# file: 0XY_healthcare_data_analysis/backend/tests/test_data_loading.py

import sys
from pathlib import Path

current_file = Path(__file__)
test_dir = current_file.parent
project_root = test_dir.parent
sys.path.insert(0, str(project_root))

import pandas as pd
from data_loading import load_data

def test_load_data():
    print("Current working directory:", project_root)

    data_dir = project_root / 'data'
    print("Contents of the 'data' directory:", list(data_dir.glob('*')))

    data_file_path = data_dir / 'data-ori.csv'
    df = load_data(data_file_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0
