import typing
from copy import deepcopy

from .types import ProkladkaTypes
from .operations import ProkladkaOperations
from .errors import *


class RulesResolvingMixin:
    def _get_value_from_data_for_rule(self, value, value_type, from_data=False):
        if from_data:
            value = self.data_to_evaluate[value]
        return ProkladkaTypes().convert(value, value_type)

    def resolve_rule(self, rule):
        rule_resolving_result = deepcopy(rule)

        operation = ProkladkaOperations.get_operation(rule["operation"])

        first_value = self._get_value_from_data_for_rule(
            rule["first_value"],
            rule["first_value_type"],
            rule.get("first_value_from_data") or False,
        )

        second_value = self._get_value_from_data_for_rule(
            rule["second_value"],
            rule["second_value_type"],
            rule.get("second_value_from_data") or False,
        )

        rule_resolving_result["resolving_result"] = operation(first_value, second_value)

        rule_resolving_result["first_value_from_source"] = first_value
        rule_resolving_result["second_value_from_source"] = second_value

        return rule_resolving_result

    def resolve_rules(self):
        if not self.validated:
            raise NotValidatedRulesAndData("first you have to run validate() method")

        if self.errors:
            raise ValidationError(f"Can`t resolve `cause of validation errors:\n {self.errors}")

        rules_resolving_result = []

        if not self.evaluation_rules:
            raise EmptyRulesList()

        for rule in self.evaluation_rules:
            rules_resolving_result.append(self.resolve_rule(rule))

        self.last_evaluation_results = rules_resolving_result

        return rules_resolving_result


class Prokladka(RulesResolvingMixin):

    def __init__(self, data_to_evaluate: typing.Dict, evaluation_rules: typing.List[typing.Dict]):
        self.data_to_evaluate = data_to_evaluate
        self.evaluation_rules = evaluation_rules
        self.last_evaluation_results = None

        self.validated = False
        self.errors = []

    def validate_rule(self, rule):

        if "operation" not in rule:
            raise NoOperationFieldInRule()

        try:
            ProkladkaOperations.get_operation(rule["operation"])
        except AttributeError:
            raise IncorrectOperator(f"Prokladka does not support '{rule['operation']}' operation")

    def validate(self):
        """
        This function checks rules and data for
        :return:
        """

        self.errors = []

        for rule in self.evaluation_rules:
            try:
                self.validate_rule(rule)
            except Exception as e:
                self.errors.append({
                    rule["name"]: e
                })

        self.validated = True
