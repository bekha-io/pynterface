# Pynterface

The `pynterface` library provides a mechanism for enforcing strict adherence to interfaces in Python. It allows you to define interfaces using the `Interface` class and ensures that all implementing classes properly implement the required methods defined in the interface.

## Installation

You can install the `pynterface` library using pip:

```shell
pip install pynterface
```

## Usage

### Defining Interfaces

To define an interface, create a class that inherits from the `Interface` class:

```python
from pynterface import Interface

class Car(Interface):
    def beep() -> str: ...
```

In this example, the `Car` interface defines a single method called `beep` which should return a string value.

### Implementing Interfaces

To implement an interface, create a class that inherits from the interface class:

```python
class Toyota(Car):
    def beep() -> str:
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
from pynterface import Interface

class Car(Interface):
    def beep() -> str: ...

class Toyota(Car):
    def beep() -> str:
        # Implementation code here
        pass
```

In this example, the `Toyota` class properly implements the `beep` method defined in the `Car` interface.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/bekha-io/pynterface). Additionally, pull requests are also appreciated.