def solve(filename):
    current_path = '/'
    files = []
    paths = ['/']

    with (open(filename) as file):
        lines = file.read().splitlines()
        is_in_ls = False
        for line in lines:
            if line.startswith('$'):
                splitted = line.split(' ')
                is_in_ls = False
                if splitted[1] == 'ls':
                    is_in_ls = True
                if splitted[1] == 'cd':
                    if splitted[2] == '/':
                        pass
                    elif splitted[2] == '..':
                        current_path = current_path[0:current_path.rindex('/', 0, -1) + 1]
                    else:
                        current_path += splitted[2] + "/"
                    if current_path not in paths:
                        paths.append(current_path)
            elif is_in_ls:
                splitted = line.split(' ')
                if splitted[0] == 'dir':
                    pass
                    # paths.append(current_path + splitted[1] + '/')
                else:
                    files.append((current_path + splitted[1], int(splitted[0])))
        # print(paths)
        # print(files)
        result = 0
        dirs = []
        for path in paths:
            size = 0
            for (file, file_size) in files:
                if file.startswith(path):
                    size += file_size
            dirs.append((path, size))
            if size <= 100000:
                result += size
        print(result)
        sorted_dirs = sorted(dirs, key=lambda dir: dir[1])
        _, total_size = sorted_dirs[-1]
        space_needed = 30000000 - (70000000 - total_size)
        for _, size in sorted_dirs:
            if size > space_needed:
                print(size)
                break


if __name__ == '__main__':
    solve('test_input')
    solve('input')
