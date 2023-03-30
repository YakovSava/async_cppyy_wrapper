<p align="center">	
	<img alt="PyPI" src="https://img.shields.io/pypi/v/asynccppyy?color=green&label=PyPI">
	<img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/YakovSava/async_cppyy_wrapper/bug">
	<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/asynccppyy">
</p>

# What is it?
This is a small wrapper library for [cppyy](https://github.com/wlav/cppyy) ([PyPl](https://pypi.org/project/cppyy/)) in Python

## How to use this?
Here is an example of a small folder with examples:

tester.py
```Python
import asyncio

from asynccppyy import AsyncDownoload

downoload = AsyncDownoload(path='your_path')

...

async def main():
	await downoload.print('Hello world!')

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
```

test.cxx
```C++
# include <iostream>
using namespace std;

void print(string arg) {
	cout << arg << endl;
}
```

tree
```
Path
│   tester.py
│
└───your_path/
        test.cxx
```