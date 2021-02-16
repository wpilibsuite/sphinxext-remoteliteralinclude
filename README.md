# sphinxext-remoteliteralinclude

![CI](https://github.com/wpilibsuite/sphinxext-remoteliteralinclude/workflows/CI/badge.svg)

Sphinx extension that extends the ``literalinclude`` directive to allow remote URLS

## Installation

Please install the extension via pip using the following command:

``python3 -m pip install sphinxext-remoteliteralinclude``

then in your ``conf.py`` under ``extensions``, it should look like the following:

```python
extensions = ["sphinxext.remoteliteralinclude"]
```

## Usage

Simply just use it as you normally would a normal ``literalinclude``

```
.. rli:: https://example.com/example.java
   :language: java
   :lines: 10-29
   :linenos:
   :lineno-start: 10
```

## Important Notes

This is simply a modification of the normal literalinclude extension. Near all of the code is the exact same. Modifications are made by Eli Barnett, with pip module creation by Dalton Smith. 

Using the extension to reference local files **will not** work. Use the regular ``literalinclude`` extension in that case.
