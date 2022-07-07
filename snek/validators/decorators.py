from typing import Any


def Validator():
    def decorate(classDef):
        def validate(self, field_name: str, value: Any):
            validator = getattr(self, field_name, None)

            if validator is None:
                return

            validator.validate(field_name, value)

        def init(self, **kwargs):
            for key, value in kwargs.items():
                self.validate(key, value)

        classDef.__init__ = init
        classDef.validate = validate

        return classDef

    return decorate
