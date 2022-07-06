def Injectable():
    def decorate(classDef):
        classDef.__injectable__ = True
        return classDef

    return decorate


def Controller(route):
    def decorate(classDef):
        classDef.__meta_prefix__ = route
        return classDef

    return decorate


def Module(controller, providers=[]):
    def decorate(classDef):
        def init(self, controller, providers):
            self.controller = controller
            self.providers = providers

        classDef.__init__ = init

        return lambda: classDef(controller, providers)

    for provider in providers:
        if not getattr(provider, "__injectable__", False):
            raise Exception(
                "Cannot instantiate a module with an un-injectable provider"
            )

    return decorate
