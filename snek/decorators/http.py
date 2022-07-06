def get_decorator_function(method: str, route: str):
    def decorate(fn):
        fn.__meta_method__ = method
        fn.__meta_route__ = route or "/"
        return fn

    return decorate


def Get(route=None):
    return get_decorator_function("get", route)


def Post(route=None):
    return get_decorator_function("post", route)
