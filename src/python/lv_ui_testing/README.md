# LabVIEW User Interface testing

The aim of that package is to create LabVIEW User Interface testing through scripts through pyTest.

## Requirements

This package allows python to communicate with the LabVIEW package "ui-testing". You need to have that package installed within your LabVIEW IDE and have the main.vi put in your top VI.

## Documentation

Examples can be found on the [wiki](https://github.com/ThomasPRZilliox/lv-ui-testing/wiki) of the project.

The following example will set a value to control labelled "myNumber", the boolean indicator "greater" should be TRUE when myNumber is > 5.

> **_NOTE:_**  Even tough it's recommended to start the VI first, it should also work as the python script is waiting to connect to it.

```python
# Start the VI "example 2 - value" first then run that script
from lv_ui_testing import ui_testing
import pytest

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi == "example 2 - value.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    # Set value to 0
    ui_testing.FMV_set_value_DBL("myNumber", number)
    data_number = ui_testing.FMV_get_value_DBL("myNumber")
    data_bool = ui_testing.FMV_get_value_bool("greater")

    assert data_bool == expected_bool
    assert data_number == number

```

Run the following command in your command line:

```
python -m pytest example2.py
```

You should see the following test happening:

![Example 2](https://raw.githubusercontent.com/ThomasPRZilliox/lv-ui-testing/main/doc/test_values.gif)



## License

Distributed under the MIT License. Copyrights Thomas Zilliox and others.