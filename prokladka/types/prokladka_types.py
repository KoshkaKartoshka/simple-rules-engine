class ProkladkaTypes:

    SUPPORTED_TYPES = {
        "int": int,
        "float": float,
        "str": str,
        "custom_logic": "",
        "custom_data": "",
    }

    CUSTOM_TYPES = {}

    def _create_custom_data_value(self, data_rule, data):
        """
        TODO: create data_rule parser

        it will be smth like key_name_1__{operation_from_prokladka_operations}__key_name_2
        """

        return

    def add_custom_type(self, name, data_rule, data):
        self.CUSTOM_TYPES[name] = {
            "data_rule": data_rule,
            "data_value": self._create_custom_data_value(data_rule, data)
        }

    def get_custom_type(self, name):
        return self.CUSTOM_TYPES[name]["data_value"]

    def convert(self, value, value_type):
        return self.SUPPORTED_TYPES[value_type](value)
