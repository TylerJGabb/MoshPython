from pathlib import Path


def use_glob():
    """
    demonstration of using glob.
    """
    path = Path("../ecommerce_modules")

    #  find all the .py files in the path directory
    print(f'things found in {path} using .glob("*.py")')
    for p in path.glob("*.py"):
        print(f'\t{p}')

    #  find all the .py files in the path directory recursively
    print(f'things found in {path} using .glob("**/*.py"')
    for p in path.glob("**/*.py"):
        print(f'\t{p}')



def use_iterdir():
    """
    demonstration of using the iterdir() method. This does not recursively list files
    """
    path = Path("../ecommerce_modules")
    result = path.iterdir()  # this returns a generator, so we will have to iterate over it.
    paths = [p for p in path.iterdir()]
    print(f'Things found in \"{path}\" using iterdir():')
    [print(f'\t{p}') for p in paths]


def useful_method_demo():
    """
    A demonstration of various useful methods of the Path class
    """
    path = Path('../ecommerce_modules/__init__.py')
    print(f'path={path}')
    print(f'path.is_file()={path.is_file()}')
    print(f'path.is_dir()={path.is_dir()}')
    print(f'path.exists()={path.exists()}')
    print(f'path.name={path.name}')
    print(f'path.stem={path.stem}')
    print(f'path.suffix={path.suffix}')
    print(f'path.parent={path.parent}')
    print(f'path.with_name("foo.bar")={path.with_name("foo.bar")}')
    print(f'path.absolute()={path.absolute()}')
    print(f'path.with_suffix(".txt")={path.with_suffix(".txt")}')
