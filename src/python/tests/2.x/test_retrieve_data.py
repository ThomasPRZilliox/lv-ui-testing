# Start the VI "example 10 - retrive data" first then run that script
import lv_ui_testing.front_most_vi as fmv

for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
    ctrl = ctrl + " 1D"
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

for ctrl in ["EXT", "DBL", "SGL", "FXP", "I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8", "CDB", "CXT", "CSG"]:
    ctrl = ctrl + " 2D"
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

for ctrl in ["Row", "Col", "One", "Four"]:
    ctrl = "I64 2D " + ctrl
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

for ctrl in ["String", "String 1D", "String 2D"]:
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

for ctrl in ["Boolean", "Boolean 1D", "Boolean 2D"]:
    print(f"{ctrl} : {fmv.resolve_value(ctrl)}")

