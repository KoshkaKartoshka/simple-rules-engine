import operator


class ProkladkaOperations:
    SUPPORTED_OPERATIONS = {
        # 'abs': operator.abs,
        'add': operator.add,
        'eq': operator.eq,
        'floordiv': operator.floordiv,
        'ge': operator.ge,
        'gt': operator.gt,
        'le': operator.le,
        'lt': operator.lt,
        'matmul': operator.matmul,
        'mod': operator.mod,
        'mul': operator.mul,
        'ne': operator.ne,
        'neg': operator.neg,
        'or_': operator.or_,
        'pow': operator.pow,
        'sub': operator.sub,
        'truediv': operator.truediv,
    }

    @classmethod
    def get_operation(cls, operation_name):
        return cls.SUPPORTED_OPERATIONS[operation_name]
