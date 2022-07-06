from aiohttp import web

k_prefix = "__meta_prefix__"
k_route = "__meta_route__"
k_method = "__meta_method__"


class Snek:
    def __init__(self):
        self.app = web.Application()
        self.modules = []

    def register_module(self, module):
        self.modules.append(module())
        return self

    def listen(self, host="localhost", port=9091):
        for module in self.modules:
            providers = [provider() for provider in module.providers]
            controller = module.controller(*providers)

            routes = []

            for attr in dir(controller):
                handler = getattr(controller, attr, None)

                if not getattr(handler, k_route, None):
                    continue

                method = getattr(handler, k_method)
                prefix = getattr(controller, k_prefix)
                route = getattr(handler, k_route)

                aio_handler = getattr(web, method)(
                    f"{prefix}{route if route != '/' else ''}", handler
                )

                routes.append(aio_handler)

            self.app.add_routes(routes)
            web.run_app(self.app, host=host, port=port)

    @staticmethod
    def from_defaults():
        return Snek()
