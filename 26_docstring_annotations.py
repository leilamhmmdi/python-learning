# Docstring

def func(x, y, z):
    """
    Parameters:
        x (int): First number
        y (int): Second number
        z (int): Third value

    Returns:
        None
    """
    print(x, y, z)

print(func.__doc__)


# Type Annotations

def show_info(x: int, y: int, z: str):
    print(x, y, z)

show_info(1, 2, "Hello")


# Return Type Annotation

def add(x: int, y: int) -> int:
    return x + y

print(add(5, 7))


# Another Example

def multiply(a: float, b: float) -> float:
    return a * b

print(multiply(2.5, 4))
