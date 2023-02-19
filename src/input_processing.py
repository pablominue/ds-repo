import pandas as pd
from .logging.log import PabLog
from abc import ABC, abstractmethod
# import matplotlib.pyplot as plt
# import seaborn as sns
# import xgboost as xgb

# plt.style.use('fivethirtyeight')

lg = PabLog()

class InputProcessing(ABC):

    def __init__(self, df:pd.DataFrame)-> None:
        lg.add_title('Starting Data Processing...')
        #self.color_pal = sns.color_palette()
        self.data = df
    
    @abstractmethod
    def process_data(self):
        pass

    def display_data(self):
        lg.add_table(self.data, title = "Data Preview", max_rows=15)
        # self.data.plot(
        #     style = '.',
        #     figsize=(15,5),
        #     color = self.color_pal[0]
        # )

    def get_processed_data(self) -> pd.DataFrame:
        return self.data


class ElectriciyInput(InputProcessing):
    def __init__(self, df) -> None:
         super().__init__(df)

    def process_data(self):
        lg.log.info(f'Processing the data...')
        self.data.set_index('Datetime')
        self.data.index = pd.to_datetime(self.data.index)

        self.train = self.data.loc[self.data.index < '01-01-2015']
        self.test = self.data.loc[self.data.index >= '01-01-2015']

        self.data['hour'] = self.data.index.hour
        self.data['dayofweek'] = self.data.index.dayofweek
        self.data['quarter'] = self.data.index.quarter
        self.data['month'] = self.data.index.month
        self.data['year'] = self.data.index.year
        self.data['dayofyear'] = self.data.index.dayofyear


