
from .initialization.build_conduit import build_conduit


class process_manager:
    def __init__(self, model: str, train_data: str, test_data: str, validation_data: str, epochs: str):
        self.grimoire = build_conduit(model, train_data, test_data, validation_data, epochs)
        # TODO Think of a proper way to define rule of engagement. Enum like maybe?
        # self.roe = rule_of_engagement()
