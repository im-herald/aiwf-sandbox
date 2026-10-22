# Coding standards

- STD-1: Standard library only; no third-party imports.
- STD-2: Every public function has a docstring stating its parameters, return value and raised exceptions.
- STD-3: No `print` calls in `slugkit/core.py`; output belongs to `slugkit/__main__.py`.
- STD-4: Exceptions are the built-in types named by the spec, with the exact messages the spec gives.
- STD-5: Every behaviour change has unit tests in `tests/` using `unittest`, through the public `slugkit` interface.
- STD-6: Module-level constants for compiled regular expressions; no regex compilation inside loops.
