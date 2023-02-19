from sklearn.cluster import KMeans
import pandas as pd


class Clusterization():

    def __init__(self, processed_input:pd.DataFrame, clusters) -> None:
        self.model = KMeans(
            n_clusters=clusters,
            max_iter= 500
        )
        self.data = processed_input

    def modelize(self):
        self.model.fit_predict(self.data.to_numpy())
        print(self.model)
        