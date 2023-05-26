import typing
import inspect


def is_same_methods(method1: typing.Callable, method2: typing.Callable) -> bool:
    if method1.__name__ != method2.__name__:
        return False
        
    method1_sig = inspect.signature(method1)
    method2_sig = inspect.signature(method2)
    
    if method1_sig.parameters != method2_sig.parameters:
        return False
    
    if method1_sig.return_annotation != method2_sig.return_annotation:
        return False
    
    return True


def is_same_classes(class1: typing.Type, class2: typing.Type) -> bool:
    return set(dir(class1)) == set(dir(class2))


class InterfaceMeta(type):
    interfaceCls = None

    def __new__(cls, name, bases, args):
        if name == 'Interface' and cls.interfaceCls is None:
            cls.interfaceCls = super().__new__(cls, name, bases, args)
            return super().__new__(cls, name, bases, args)

        interfaces = [b for b in bases if is_same_classes(b.__bases__[0], cls.interfaceCls)]

        if interfaces:
            methods = {k: v for k, v in args.items() if callable(v)}

            for interface in interfaces:
                interface_methods = {k: v for k, v in interface.__dict__.items() if callable(v)}

                not_implemented_methods = []

                for method_name, method in interface_methods.items():
                    implementing_method = methods.get(method_name, None)

                    if implementing_method is None or not is_same_methods(method, implementing_method):
                        not_implemented_methods.append(method_name)
                
                if not_implemented_methods:
                    raise NotImplementedError(
                        f"{name} is not implementing methods from {interface.__name__}: {', '.join(not_implemented_methods)}")

        return super().__new__(cls, name, bases, args)


class Interface(metaclass=InterfaceMeta):
    pass


def implements(obj: typing.Union[typing.Type, typing.Any], interfaces: typing.Union[typing.Type[Interface], typing.Sequence[typing.Type[Interface]]]):
    if inspect.isclass(obj):
        return issubclass(obj, interfaces)
    return isinstance(obj, interfaces)