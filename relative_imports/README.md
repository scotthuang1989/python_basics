This is a almost copy of [this blog](https://www.napuzba.com/story/import-error-relative-no-parent/). I turn it into actionable code for better understanding
## Meet the Error

Here is the structure of package module:
```
project/
├── config.py
└── package
    ├── demo.py
    └── __init__.py
```
The `config.py` contains some variable which `demo.py`  will use.
if I run `demo.py` like this, I will get an error.

```
mydevice$ python project/package/demo.py
Traceback (most recent call last):
  File "project/package/demo.py", line 1, in <module>
    from .. import config
ValueError: attempted relative import beyond top-level package
```

## Theory

### PEP328:

Relative imports use a module’s __name__ attribute to determine that module’s position in the package hierarchy. If the module’s name does not contain any package information (e.g. it is set to __main__) then relative imports are resolved as if the module were a top level module, regardless of where the module is actually located on the file system.

### PEP328 In English

In other words, the algorithm to resolve the module is based on the values of __name__ and __package__ variables. Sometimes those variables does not contain any package information – When __name__ = __main__ and __package__ = None the python interpreter does not know the package the module is belong to. In this case, any relative imports are resolved as if the module were a top level module, regardless of where the module is actually located on the file system.

### Action

you can add following code into any file you want to inspect

```
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
count = 5
```

## Solution

### 1

Change the structure of code.

* convert project into a package.
* create `main.py` in parent directory of project directory.

Here is the new structure:

```
solution1/
├── main.py
└── project
    ├── config.py
    ├── __init__.py
    ├── package
    │   ├── demo.py
    │   ├── __init__.py
```
### ２

change the way of running script:
run the script as a module by add `-m` option.

```
python -m project.package.demo
```
