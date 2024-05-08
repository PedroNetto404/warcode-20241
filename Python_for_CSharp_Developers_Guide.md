# Python for C# Developers Guide

This guide provides a comparison between Python and C# to help C# developers understand the similarities and differences when learning Python.

## 1. Syntax Differences
Python uses indentation to define blocks of code, whereas C# uses curly braces.

### Python
```python
if x > 10:
    print("x is greater than 10")
```

### C#
```csharp
if (x > 10)
{
    Console.WriteLine("x is greater than 10");
}
```

## 2. Variable Declaration
Python does not require explicit declaration of variable types. C# requires explicit types unless using the `var` keyword.

### Python
```python
x = 10  # Automatically an integer
```

### C#
```csharp
int x = 10;
```

## 3. Functions vs. Methods
Python functions are defined using the `def` keyword, and Python doesn't use static typing. C# methods are part of classes and use type annotations.

### Python
```python
def add_numbers(x, y):
    return x + y
```

### C#
```csharp
public int AddNumbers(int x, int y)
{
    return x + y;
}
```

## 4. Main Function
Python scripts typically check if they are the main module before executing the main code. C# uses a static main method in a class.

### Python
```python
if __name__ == "__main__":
    print("This script is the main program")
```

### C#
```csharp
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("This is the main method");
    }
}
```

## 5. Libraries and Using/Import
Python uses `import` to include libraries, while C# uses `using`.

### Python
```python
import math
```

### C#
```csharp
using System.Math;
```

### Conclusion
This guide highlights some of the key differences and similarities between Python and C#. This should help C# developers start their journey in learning Python.
