GRID_SERIAL_NO = 1309
GRID_SIZE = 300


def main():
    power_grid = get_power_grid()
    grid_maxes = get_grid_maxes(power_grid)
    max_coord = get_max_coord(grid_maxes)
    print(max_coord)
    return


def get_power_grid():
    grid = [[]] * GRID_SIZE
    for x in range(1, GRID_SIZE - 1):
        grid[x] = [0] * GRID_SIZE
        for y in range(1, GRID_SIZE - 1):
            grid[x][y] = get_power_level(x, y)
    return grid


def get_grid_maxes(power_grid):
    grid = [[]] * GRID_SIZE
    for x in range(1, GRID_SIZE - 1):
        grid[x] = [0] * GRID_SIZE
        for y in range(1, GRID_SIZE - 1):
            grid[x][y] = get_n_by_n_total(x, y, power_grid)
    return grid


def get_n_by_n_total(x, y, power_grid):
    max_pow = 0
    max_n = 0
    for box_size in range(GRID_SIZE - max([x, y])):
        power = 0
        for i in range(box_size):
            for j in range(box_size):
                power += power_grid[x+i][y+j]
        if power > max_pow:
            max_pow = power
            max_n = box_size
    return (max_n, max_pow)


def get_power_level(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += GRID_SERIAL_NO
    power *= rack_id
    power = int(power / 100) % 10 - 5
    return power


def get_max_coord(grid):
    max_pow = 0
    max_coord = (0, 0)
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            (n, power) = grid[x][y]
            if power > max_pow:
                max_pow = power
                max_coord = (x, y, n)
                # print('new max at ({} {}) with size {} of {}'.format(x, y, n, max_pow))
    return max_coord


if __name__ == '__main__':
    main()