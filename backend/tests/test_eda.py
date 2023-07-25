#file: 0XY_healthcare_data_analysis/backend/tests/test_eda.py
import sys
import os
import unittest
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(current_directory))

import eda

class TestEDA(unittest.TestCase):
  def test_convert_binary_to_numerical(self):
    df = pd.DataFrame({
      'SEX': ['F', 'M', 'F', 'M'],
      'SOURCE': ['out', 'in', 'out', 'in']
    })
    df = eda.convert_binary_to_numerical(df)
    self.assertTrue((df['SEX'] == [0, 1, 0, 1]).all())
    self.assertTrue((df['SOURCE'] == [0, 1, 0, 1]).all())
    
  def test_identify_outliers(self):
    df = pd.DataFrame({
      'HAEMATOCRIT': [1, 2, 3, 4, 5, 100]
    })
    outliers = eda.identify_outliers(df, 'HAEMATOCRIT')
    self.assertEqual(outliers['HAEMATOCRIT'].tolist(), [100])
    
if __name__ == '__main__':
  unittest.main()