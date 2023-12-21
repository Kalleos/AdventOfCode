from math import lcm


class Module:

    def __init__(self, name, typ, destinations):
        self.name = name
        self.typ = typ
        self.is_flip_flop = typ == '%'
        self.is_conjunction = typ == '&'
        self.destinations = destinations
        if self.is_conjunction:
            self.memory = {}
        else:
            self.memory = False

    def __repr__(self):
        return f'[{self.name}, {self.typ}, {self.memory}]'


def parse_module(line: str):
    splitted = line.split(' -> ')
    if splitted[0][0] in ['%', '&']:
        typ = splitted[0][0]
        name = splitted[0][1:]
    else:
        typ = None
        name = splitted[0]
    dests = [dest.strip() for dest in splitted[1].split(',')]
    return Module(name, typ, dests)


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

        N = 0
        rx_signal = None
        cycles = {}
        result = None
        while rx_signal is not False and result is None:
            N += 1
            to_handle = [('button', 'broadcaster', False)]
            while to_handle:
                origin, module_name, sign_in = to_handle.pop(0)
                # print(f'{origin} -{sign_in}-> {module_name}')
                if module_name == 'rx' and sign_in is False:
                    rx_signal = False
                    print(N)
                    break
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

                        if module_name in ['jq', 'cc', 'sp', 'nx']:
                            if module_name not in cycles:
                                cycles[module_name] = N
                            if len(cycles) == 4:
                                result = lcm(*cycles.values())
                    for dest in module.destinations:
                        to_handle.append((module_name, dest, sign_out))

        print(N)
        print(result)


if __name__ == '__main__':
    solve('input')
