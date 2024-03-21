import comtypes.client

class LoadPattern:
    def __init__(self, model):
        self.model = model

    def add_load_pattern(self, name, pattern_type, self_weight_multiplier=0):
        self.model.LoadPatterns.Add(name, pattern_type, self_weight_multiplier)