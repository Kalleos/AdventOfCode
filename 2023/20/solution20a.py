class Module:

    def __init__(self, name, type, destinations):
        self.name = name
        self.type = type
        self.is_flip_flop = type == '%'
        self.is_conjunction = type == '&'
        self.destinations = destinations
        if self.is_conjunction:
            self.memory = {}
        else:
            self.memory = False

    def __repr__(self):
        return f'[{self.name}, {self.type}, {self.memory}]'


def parse_module(line: str):
    splitted = line.split(' -> ')
    if splitted[0][0] in ['%', '&']:
        type = splitted[0][0]
        name = splitted[0][1:]
    else:
        type = None
        name = splitted[0]
    dests = [dest.strip() for dest in splitted[1].split(',')]
    return Module(name, type, dests)


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        modules = dict([(module.name, module) for module in [parse_module(line) for line in lines]])
        for name, module in modules.items():
            for dest in module.destinations:
                if dest in modules:
                    dest_module = modules[dest]
                    if dest_module.is_conjunction:
                        dest_module.memory[name] = False

        print(modules)

        lows = 0
        highs = 0
        for _ in range(1000):
            to_handle = [('button', 'broadcaster', False)]
            while to_handle:
                origin, module_name, sign_in = to_handle.pop(0)
                if sign_in:
                    highs += 1
                else:
                    lows += 1
                # print(f'{origin} -{sign_in}-> {module_name}')
                if module_name not in modules:
                    continue
                module = modules[module_name]
                if not module.is_flip_flop and not module.is_conjunction:
                    for dest in module.destinations:
                        to_handle.append((module_name, dest, sign_in))
                if module.is_flip_flop is True and sign_in is False:
                    module.memory = not module.memory
                    for dest in module.destinations:
                        to_handle.append((module_name, dest, module.memory))
                if module.is_conjunction is True:
                    module.memory[origin] = sign_in
                    if all([status for status in module.memory.values()]):
                        sign_out = False
                    else:
                        sign_out = True
                    for dest in module.destinations:
                        to_handle.append((module_name, dest, sign_out))

        print(lows, highs, lows * highs)


if __name__ == '__main__':
    solve('test_input')
    solve('test_input2')
    solve('input')
