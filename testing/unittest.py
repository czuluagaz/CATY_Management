import unittest
import pandas as pd
import numpy as np
from core.graphical_analysis import plot_grouped_data

class TestGraphicalAnalysis(unittest.TestCase):

    def setUp(self):
        # Create sample data
        date_rng = pd.date_range(start='1/1/2020', end='1/01/2021', freq='D')
        self.data = pd.DataFrame(date_rng, columns=['date'])
        self.data['consumption'] = np.random.randint(0, 100, size=(len(date_rng)))

        # Group the data
        self.data.set_index('date', inplace=True)
        self.data_day = self.data.resample('D').sum()
        self.data_week = self.data.resample('W').sum()
        self.data_month = self.data.resample('M').sum()
        self.data_quarter = self.data.resample('Q').sum()
        self.data_season = self.data.resample('Q-FEB').sum()
        self.data_year = self.data.resample('Y').sum()

    def test_plot_grouped_data(self):
        try:
            plot_grouped_data(
                self.data_day,
                self.data_week,
                self.data_month,
                self.data_quarter,
                self.data_season,
                self.data_year,
                title="Test Plot",
                ylabel="Consumption",
                xlabel="Date",
                color="blue"
            )
        except Exception as e:
            self.fail(f"plot_grouped_data raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()