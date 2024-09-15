def all_thing_is_obj(object: any) -> int:
    names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }
    typ = type(object);
    name = names.get(typ, "Type not found")

    if typ == str:
        print(f"{object} is in the kitchen : {typ}")
    elif name == "Type not found":
        print(f"{name}")
    else:
        print(f"{name} : {typ}")
    return (42)