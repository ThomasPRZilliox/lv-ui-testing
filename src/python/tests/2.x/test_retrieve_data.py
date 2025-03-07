# Start the VI "example 10 - retrive data" first then run that script
import lv_ui_testing.front_most_vi as fmv
import pytest

# for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")


number_representations = {
    "EXT": 1.2345, "DBL":1.23, "SGL":1.2, "FXP":"0x000000001f7ced91", "I64":-64, "I32":-32, "I16":-16,
    "I8": -8, "U64":64, "U32":32, "U16":16, "U8":8, "CDB":(1.23+2j), "CXT":(1.2345+1j), "CSG":(1.2+3j)
}

string_representations = {
    "String":"Hello World",
    "String 1D": ["Hello", "World"],
    "String 2D": [["Hel","lo"],["Wor","ld"]]
}

bool_representations = {
    "Boolean": True,
    "Boolean 1D": [False, True],
    "Boolean 2D": [[False, True],[True, False]]
}

array_representations = {
    "I64 2D Row":[[0, 1]],
    "I64 2D Col": [[0], [1]],
    "I64 2D One": [[0]],
    "I64 2D Four": [[0, 1],[2, 3]]
}
@pytest.mark.parametrize("number_representation, value", [(x, y) for x,y in number_representations.items()])
def test_number(number_representation,value):
    resolve_value = fmv.resolve_value(number_representation)
    assert resolve_value == value

@pytest.mark.parametrize("number_representation, value", [(x, y) for x,y in number_representations.items()])
def test_number_1D(number_representation,value):
    number_representation = number_representation + " 1D"
    resolve_value = fmv.resolve_value(number_representation)
    assert resolve_value == [value,value]

@pytest.mark.parametrize("number_representation, value", [(x, y) for x,y in number_representations.items()])
def test_number_2D(number_representation,value):
    number_representation = number_representation + " 2D"
    resolve_value = fmv.resolve_value(number_representation)
    assert resolve_value == [[value,value]]

@pytest.mark.parametrize("string_representation, value", [(x, y) for x,y in string_representations.items()])
def test_string(string_representation,value):
    resolve_value = fmv.resolve_value(string_representation)
    assert resolve_value == value


@pytest.mark.parametrize("bool_representation, value", [(x, y) for x,y in bool_representations.items()])
def test_bool(bool_representation,value):
    resolve_value = fmv.resolve_value(bool_representation)
    assert resolve_value == value

@pytest.mark.parametrize("array_representation, value", [(x, y) for x,y in array_representations.items()])
def test_array(array_representation,value):
    resolve_value = fmv.resolve_value(array_representation)
    assert resolve_value == value

# for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
#     ctrl = ctrl + " 1D"
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")
#
# for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
#     ctrl = ctrl + " 1D"
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")
#
# for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
#     ctrl = ctrl + " 2D"
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")
#
# for ctrl in ["Row", "Col", "One", "Four"]:
#     ctrl = "I64 2D " + ctrl
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")
#
# for ctrl in ["String", "String 1D", "String 2D"]:
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")
#
# for ctrl in ["Boolean", "Boolean 1D", "Boolean 2D"]:
#     print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

