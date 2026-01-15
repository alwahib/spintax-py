# Release Checklist for spintaxpy

## Pre-Release Verification

- [x] All tests pass (24/24 tests passing)
- [x] Package builds without warnings
- [x] Package metadata is correct
- [x] README.md includes PyPI installation instructions
- [x] LICENSE file is included
- [x] No security vulnerabilities (CodeQL scan passed)

## Package Information

- **PyPI Package Name**: spintaxpy
- **Import Name**: spintaxpy
- **Current Version**: 1.0.0
- **License**: MIT
- **Python Compatibility**: >=3.6

## Files Included in Distribution

✓ Source code (spintaxpy/__init__.py, spintaxpy/spintax.py)
✓ README.md
✓ LICENSE
✓ Tests (tests/test_spintax.py)
✓ Metadata files

## Quick Publishing Steps

### 1. Clean previous builds
```bash
rm -rf dist/ build/ *.egg-info
```

### 2. Build the package
```bash
python -m build
```

### 3. (Optional) Test on TestPyPI first
```bash
python -m twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ spintaxpy
```

### 4. Upload to PyPI
```bash
python -m twine upload dist/*
```

### 5. Verify installation
```bash
pip install spintaxpy
python -c "from spintaxpy import parse; print(list(parse('Hello {world|friend}!')))"
```

## Post-Release

- [ ] Verify package appears on https://pypi.org/project/spintaxpy/
- [ ] Test installation from PyPI
- [ ] Update GitHub release tags
- [ ] Announce release

## Notes

- The package is configured to use modern Python packaging standards (PEP 517/518)
- License is specified using SPDX format (MIT) to avoid deprecation warnings
- Both source distribution (.tar.gz) and wheel (.whl) are built
- All metadata is consistent between pyproject.toml and setup.py

## Support

For detailed publishing instructions, see [PUBLISHING.md](PUBLISHING.md)
