import binascii

from graphene.types import Scalar
from graphql.language import ast
class Binary(Scalar):
    """
    BinaryArray is used to convert a BinaryField to the string form
    """
    @staticmethod
    def binary_to_string(value):
        return binascii.hexlify(value).decode("utf-8")

    serialize = binary_to_string
    parse_value = binary_to_string

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return binascii.hexlify(node.value).decode("utf-8")