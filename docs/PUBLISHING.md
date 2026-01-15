# Publishing to PyPI

This document provides instructions for publishing the spintaxpy package to PyPI.

## Prerequisites

1. Create accounts on:
   - PyPI (production): https://pypi.org/account/register/
   - TestPyPI (testing): https://test.pypi.org/account/register/

2. Install required tools:
   ```bash
   pip install --upgrade build twine
   ```

## Build the Package

Build both source distribution (sdist) and wheel:

```bash
python -m build
```

This creates two files in the `dist/` directory:
- `spintax_py-1.0.0.tar.gz` (source distribution)
- `spintax_py-1.0.0-py3-none-any.whl` (wheel distribution)

## Test on TestPyPI (Recommended)

Before publishing to the real PyPI, test on TestPyPI:

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Install from TestPyPI to test
pip install --index-url https://test.pypi.org/simple/ spintaxpy
```

## Publish to PyPI

Once verified on TestPyPI, publish to the real PyPI:

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI credentials.

## Using API Tokens (Recommended)

For better security, use API tokens instead of passwords:

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token with scope "Entire account" or specific to this project
3. Create a `~/.pypirc` file:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Your token here

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw...  # Your token here
```

Then upload without being prompted:
```bash
python -m twine upload dist/*
```

## Verify Installation

After publishing, verify the package can be installed:

```bash
pip install spintaxpy
```

Test the installation:
```python
from spintaxpy import parse, count, choose

# Test basic functionality
result = list(parse('Hello, {world|friend}!'))
print(result)  # ['Hello, world!', 'Hello, friend!']
```

## Version Updates

When releasing a new version:

1. Update version in both:
   - `pyproject.toml` (line 6)
   - `spintaxpy/__init__.py` (line 11)
   - `setup.py` (line 10) - if keeping setup.py

2. Clean previous builds:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

3. Build and upload the new version:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

## Package Information

- **Package name on PyPI**: spintaxpy
- **Import name**: spintaxpy
- **Current version**: 1.0.0
- **License**: MIT
- **Python compatibility**: >=3.6

## Resources

- PyPI Project Page: https://pypi.org/project/spintaxpy/ (after first publish)
- Packaging User Guide: https://packaging.python.org/
- Twine Documentation: https://twine.readthedocs.io/
