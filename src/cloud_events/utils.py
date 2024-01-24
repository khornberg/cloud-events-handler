from importlib import import_module


# https://github.com/django/django/blob/4b4e68a7a6847e8b449923bb882bed01f0d7b2a8/django/utils/module_loading.py
def import_string(dotted_path):
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path".format()) from err
    module = import_module(module_path)
    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class'.format()) from err
