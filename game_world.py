world = [[], [], []]


def add_object(obj, depth=0):
    world[depth].append(obj)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(obj):
    for layer in world:
        if obj in layer:
            layer.remove(obj)
            return
    raise ValueError("Cannot delete non existing object")
