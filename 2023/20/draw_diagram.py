from solution20b import parse_module

with open('input') as file:
    lines = file.read().splitlines()
    modules = dict([(module.name, module) for module in [parse_module(line) for line in lines]])

    with open('diagram.mermaid', 'w') as diagram:
        diagram.write('stateDiagram-v2\n')
        for module in modules.values():
            for d in module.destinations:
                diagram.write(f'    {module.name.replace("broadcaster", "[*]")} --> {d.replace("rx", "[*]")}\n')
