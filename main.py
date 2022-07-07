from snek.database.decorators import Collection
from snek.validators import IntegerValidator, StringValidator, BaseValidator
from snek.validators.decorators import Validator
from snek.database import Model, MongoClient

client = MongoClient("mongodb://localhost")
database = client["snek-test"]


@Validator()
class UserValidator(BaseValidator):
    name = StringValidator(required=True, min_length=4, max_length=20)
    age = IntegerValidator(required=True, min_value=0, max_value=99)


@Collection(database)
class User(Model):
    validator = UserValidator


user = User.insert({"name": "w", "age": 18})


# user = User.insert(
#     {
#         "name": "Eder",
#         "age": 20,
#     }
# )
