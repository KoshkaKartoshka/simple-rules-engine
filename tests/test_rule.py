import pytest

from prokladka import Prokladka


@pytest.fixture
def rules():
    return [
        {
            "name": "Jolteon first rule",
            "description": "o.O",

            "first_value": "name",
            "first_value_type": "str",
            "first_value_from_data": True,

            "second_value": "3",
            "second_value_type": "str",

            "operation": "ge",
        },
        {
            "name": "Jolteon first rule",
            "description": "o.O",

            "first_value": "age",
            "first_value_type": "int",
            "first_value_from_data": True,

            "second_value": "ears_count",
            "second_value_type": "int",
            "second_value_from_data": True,

            "operation": "lt",
        }
    ]


@pytest.fixture
def data():
    return {
        "name": "Zuhra",
        "age": 123,
        "ears_count": 2,
        "eyes_count": 2,
        "fingers_count": 20,
    }


@pytest.fixture
def prokladka(data, rules):
    return Prokladka(data_to_evaluate=data, evaluation_rules=rules)


def test_prokladka(prokladka):
    prokladka.validate()
    resolving_results = prokladka.resolve_rules()
    assert isinstance(resolving_results, list)
