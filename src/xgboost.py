import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from abc import ABC, abstractmethod

class XGBooster(ABC):

    def __init__(self, df) -> None:
        self.data = df

    @abstractmethod
    def modelize(self):
        pass

class XGBoost_Electricity(XGBooster):
    def __init__(self, df) -> None:
        super().__init__(df)

    def modelize(self):
        xg = xgb.Booster().predict()
