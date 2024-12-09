def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        disk_map = list(map(int, lines[0]))

        disk, max_file_id = generate_disk(disk_map)
        disk = compact_disk(disk, max_file_id)
        result = checksum(disk)
        print(result)


def generate_disk(disk_map):
    disk = []
    file_id = 0
    is_free = False
    for n in disk_map:
        if is_free:
            disk.append((n, "."))
        else:
            disk.append((n, file_id))
            file_id = file_id + 1
        is_free = not is_free
    return disk, file_id - 1


def compact_disk(disk, max_file_id):
    for id in range(max_file_id, 0, -1):
        i = [file_id for (n, file_id) in disk].index(id)
        (n, _) = disk[i]
        for j in range(i):
            (m, file_id) = disk[j]
            if file_id == "." and n <= m:
                if m == n:
                    disk = disk[:j] + [disk[i]] + disk[j + 1:i] + [disk[j]] + disk[i + 1:]
                else:
                    disk = disk[:j] + [disk[i]] + [(m - n, ".")] + disk[j + 1:i] + [(n, ".")] + disk[i + 1:]
                break
    return disk


def checksum(disk):
    checksum = 0
    pos = 0
    for (n, file_id) in disk:
        if file_id == ".":
            pos = pos + n
        else:
            for _ in range(n):
                checksum = checksum + pos * file_id
                pos = pos + 1
    return checksum


if __name__ == '__main__':
    solve('test_input')  # 2858
    solve('input')  # 6398096697992
