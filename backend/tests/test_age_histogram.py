# file: 0XY_healthcare_data_analysis/backend/tests/test_age_histogram.py

import matplotlib.pyplot as plt
import pandas as pd
from plot_age_histogram import plot_age_histogram

def test_age_histogram():
  df = pd.DataFrame({'AGE': [18, 25, 33, 48, 55, 63, 70, 80, 90, 95]})  # Example ages for testing

  plot_age_histogram(df)

  plt.show()
