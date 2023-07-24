#file: 0XY_healthcare_data_analysis/backend/tests/test_eda.py

import unittest
import pandas as pd
import eda

class TestEDA(unittest.TestCase):
  def test_convert_binary_to_numerical(self):
    df = pd.DataFrame({
      'SEX': ['F', 'M', 'F', 'M'],
      'SOURCE': ['out', 'in', 'out', 'in']
    })
    df = eda.convert_binary_to_numerical(df)
    assert (df['SEX'] == [0, 1, 0, 1]).all()
    assert (df['SOURCE'] == [0, 1, 0, 1]).all()
    
  def test_identify_outliers(self):
    df = pd.DataFrame({
      'HAEMATOCRIT': [1, 2, 3, 4, 5, 100]
    })
    outliers = eda.identify_outliers(df, 'HAEMATOCRIT')
    assert outliers['HAEMATOCRIT'].tolist() == [100]
    
if __name__ == '__main__':
  unittest.main()