def _get_decorator_function(method: str, route: str):
    def decorate(fn):
        fn.__meta_method__ = method
        fn.__meta_route__ = route or "/"
        return fn

    return decorate


def Get(route: str = None):
    return _get_decorator_function("get", route)


def Post(route=None):
    return _get_decorator_function("post", route)
