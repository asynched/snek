from typing import Generic, Protocol, TypeVar

T = TypeVar("T")


class ValidatorProtocol(Protocol, Generic[T]):
    def validate(self, field_name: str, data: T):
        ...


class BaseValidator(ValidatorProtocol[T]):
    ...


class StringValidator(BaseValidator[str]):
    def __init__(self, required=False, min_length=None, max_length=None):
        self.required = required
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, field_name, data: str):
        if type(data) is not str:
            raise TypeError(f"{field_name} must be a string")

        if self.required and not data:
            raise ValueError(f"{field_name} is required")

        if self.min_length and len(data) < self.min_length:
            raise ValueError(
                f"{field_name} must be at least {self.min_length} characters"
            )

        if self.max_length and len(data) > self.max_length:
            raise ValueError(
                f"{field_name} must be at most {self.max_length} characters"
            )


class IntegerValidator(BaseValidator[int]):
    def __init__(self, required=False, min_value=None, max_value=None):
        self.required = required
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, field_name: str, data: int):
        if type(data) is not int:
            raise TypeError("{} must be an integer")

        if self.required and not data:
            raise ValueError("{} is required")

        if self.min_value and data < self.min_value:
            raise ValueError("{} must be at least {}".format(self.min_value))

        if self.max_value and data > self.max_value:
            raise ValueError("{} must be at most {}".format(self.max_value))


class FloatValidator(BaseValidator[float]):
    def __init__(self, required=False, min_value=None, max_value=None):
        self.required = required
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, field_name: str, data: float):
        if type(data) is not float:
            raise TypeError(f"{field_name} must be a float")

        if self.required and not data:
            raise ValueError(f"{field_name} is required")

        if self.min_value and data < self.min_value:
            raise ValueError(f"{field_name} must be at least {self.min_value}")

        if self.max_value and data > self.max_value:
            raise ValueError(f"{field_name} must be at most {self.max_value}")
