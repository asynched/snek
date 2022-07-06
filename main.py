from snek import Snek
from snek.decorators import Controller, Module
from snek.decorators.http import Get
from snek.http import Request, Response


@Controller("/hello")
class HelloController:
    @Get("/{name}")
    def say_hello(self, request: Request) -> Response:
        name = request.match_info["name"]
        return Response(body=f"Hello, {name}!")


@Module(controller=HelloController)
class HelloModule:
    ...


Snek.from_defaults().register_module(HelloModule).listen()
