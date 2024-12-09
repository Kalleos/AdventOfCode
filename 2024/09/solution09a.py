def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        disk_map = list(map(int, lines[0]))

        disk = generate_disk(disk_map)
        compact_disk(disk)
        result = checksum(disk)
        print(result)


def checksum(disk):
    return sum([i * file_id for (i, file_id) in enumerate(disk) if file_id != "."])


def compact_disk(disk):
    s = 0
    e = len(disk) - 1
    while s < e:
        s = disk.index(".", s)
        e = rfind_file(disk, e)
        if s < e:
            disk[s] = disk[e]
            disk[e] = "."


def rfind_file(s: list, e: int):
    for i in range(e, -1, -1):
        if s[i] != ".":
            return i


def generate_disk(disk_map):
    disk = []
    file_id = 0
    is_free = False
    for n in disk_map:
        if is_free:
            to_append = n * ["."]
        else:
            to_append = n * [file_id]
            file_id = file_id + 1
        disk = disk + to_append
        is_free = not is_free
    return disk


if __name__ == '__main__':
    solve('test_input')  # 1928
    solve('input')  # 6370402949053
