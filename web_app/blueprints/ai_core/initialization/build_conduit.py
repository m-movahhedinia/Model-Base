
from pathlib import Path
from logging import getLogger
from typing import Any

log = getLogger()


class build_conduit:
    base_models_path = Path("./web_app/blueprints/ai_core/models")
    base_data_path = Path("./web_app/blueprints/data_archive")

    def __setattr__(self, attr: str, value: Any):
        """
        Prevents changing the attributes when created.

        :param str attr: Attribute name.
        :param Any value: The value of the attribute.
        """
        if self.__dict__.get("locked", False) and attr != "locked":
            log.critical("This object is locked. Values of the attributes cannot be modified and new attributes "
                         "cannot be added. You can unlock it by setting its \"locked\" attribute to False. Make sure "
                         "you lock it again afterwards.")
        elif self.__dict__.get("locked", False) and value is False:
            log.warning("Object unlocked. The values of the attributes of this object are not secure anymore.")
            self.__dict__[attr] = value
        else:
            self.__dict__[attr] = value

    def __init__(self, model: str, train_data_file: str, test_data_file: str, validation_data_file: str, epochs: str):
        self.model_location = model
        self.train_data_file = self.base_data_path.joinpath(train_data_file)
        # TODO Read data. There must not be any None attribute in the instance of this class.
        self.train_data = None
        self.test_data = self.base_data_path.joinpath(test_data_file)
        self.test_data = None
        self.validation_data = self.base_data_path.joinpath(validation_data_file)
        self.validation_data = None
        self.epochs: int = int(epochs)
        self.locked = True
