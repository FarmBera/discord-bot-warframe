from module.get_obj import get_obj
from module.color import color
from translator import ts


def cmd_obj_check(name):
    obj = get_obj(name)
    if not obj or obj is None:
        print(
            f"{color['red']}ERR in '{name}' command. Object is Empty or None{color['default']}"
        )
        return False

    return obj
