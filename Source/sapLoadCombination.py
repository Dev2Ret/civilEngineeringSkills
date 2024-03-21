import comtypes.client

class LoadCombination:
    def __init__(self, model):
        self.model = model

    def add_load_combination(self, name):
        self.model.RespCombo.Add(name)

    def add_load_case_to_combination(self, combo_name, case_name, scale_factor):
        self.model.RespCombo.SetCaseList(combo_name, 0, case_name, scale_factor)