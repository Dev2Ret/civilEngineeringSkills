import pandas as pd

class Tables:
    def __init__(self):
        self.type1 = pd.DataFrame(data={'Ground Type': ["A", "B", "C", "D", "E"],
                                       'S': [1, 1.2, 1.15, 1.35, 1.4],
                                       'T1': [0.15, 0.15, 0.2, 0.2, 0.15],
                                       'T2': [0.4, 0.5, 0.6, 0.8, 0.5],
                                       'T3': [2, 2, 2, 2, 2]})
        self.type2 = pd.DataFrame(data={'Ground Type': ["A", "B", "C", "D", "E"],
                                       'S': [1, 1.35, 1.5, 1.8, 1.6],
                                       'T1': [0.05, 0.05, 0.1, 0.1, 0.05],
                                       'T2': [0.25, 0.25, 0.25, 0.3, 0.25],
                                       'T3': [1.2, 1.2, 1.2, 1.2, 1.2]})