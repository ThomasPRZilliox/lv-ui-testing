# Python

## Publish and Update PyPi

The package is published in the [lv-ui-testing project](https://pypi.org/project/lv-ui-testing/).

To update it follow the differente steps (there should be quite similar on all OS):

1. Got to the module directory
```
cd <your git path>\lv-ui-testing\src\python\lv_ui_testing>
```

2. Build the package
```
python -m build
```

3. Publish the package
```
python -m twine upload dist/*
```