# Pynterface

<p align=center><img src="https://user-images.githubusercontent.com/81781443/239869723-3b9e2504-bca5-4bd1-b81e-f668bce91ae0.png" width=320/></p>

The `pynterface` library provides a mechanism for enforcing strict adherence to interfaces in Python. It allows you to define interfaces using the `Interface` class and ensures that all implementing classes properly implement the required methods defined in the interface.

## Installation

You can install the `pynterface` library using pip:

```shell
pip install pynterfacelib
```

## Usage

### Defining Interfaces

To define an interface, create a class that inherits from the `Interface` class:

```python
from pynterfacelib import Interface

class Car(Interface):
    def beep(self) -> str: ...
```

In this example, the `Car` interface defines a single method called `beep` which should return a string value.

### Implementing Interfaces

To implement an interface, create a class that inherits from the interface class:

```python
class Toyota(Car):
    def beep(self) -> str:
        # Implementation code here
        pass
```

The `Toyota` class implements the `beep` method defined in the `Car` interface.

### Checking Interface Compliance

The `pynterface` library automatically checks if a class properly implements the methods defined in its interfaces when the class is defined. If the implementation is incomplete or the method signatures differ from the interface, a `NotImplementedError` will be raised.

The `InterfaceMeta` metaclass automatically performs the interface checking process. It compares the methods defined in the implementing class with those defined in the interface and raises appropriate errors if any inconsistencies are found.

### Example

Here's a complete example that demonstrates the usage of the `pynterface` library:

```python
from pynterfacelib import Interface

class Car(Interface):
    def beep(self) -> str: ...

class Toyota(Car):
    def beep(self) -> str:
        # Implementation code here
        pass
```
In this example, the `Toyota` class properly implements the `beep` method defined in the `Car` interface.

<br>

```python
class Car(Interface):
    def beep(self) -> str: ...


class Animal(Interface):
    def roar(self) -> str: ...


class Toyota(Car, Animal):
    def beep(self) -> str:
        # Implementation code here
        pass
```

This code raises a `NotImplementedError` because the `Toyota` class inherits from the `Animal` class but does not implement the `roar` method defined in the interface.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/bekha-io/pynterface). Additionally, pull requests are also appreciated.
