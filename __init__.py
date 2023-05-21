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


class InterfaceMeta(type):
    interfaceCls = None
    
    def __new__(cls, name, bases, args):        
        if name == 'Interface' and cls.interfaceCls is None:
            cls.interfaceCls = super().__new__(cls, name, bases, args)
            return super().__new__(cls, name, bases, args)
        
        parent_class = bases[0] or None
        if set(dir(cls.interfaceCls)) == set(dir(parent_class.__bases__[0])):
            methods = {k: v for k,v in args.items() if callable(v)}
            parent_methods = {k: v for k,v in parent_class.__dict__.items() if callable(v)}

            not_implemented_methods = []
            
            for methodNameP, methodP in parent_methods.items():
                methodCh = methods.get(methodNameP, None)
                if methodCh is None:
                    not_implemented_methods.append(methodNameP)
                    continue
                
                if not is_same_methods(methodP, methodCh):
                    raise NotImplementedError(f"{name}.{methodCh.__name__} method signature differs from {parent_class.__name__}.{methodP.__name__} signature")
            
            if len(not_implemented_methods) != 0:
                raise NotImplementedError(f"{name} is not implementing {parent_class.__name__} methods: {' '.join(not_implemented_methods)}")
        
        return super().__new__(cls, name, bases, args)


class Interface(metaclass=InterfaceMeta):
    pass