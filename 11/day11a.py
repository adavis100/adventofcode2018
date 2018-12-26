GRID_SERIAL_NO = 1309
GRID_SIZE = 300

def main():
    grid = get_grid_totals()
    max_coord = get_max_coord(grid)
    print(max_coord)
    return


def get_grid_totals():
    grid = [[]] * GRID_SIZE
    for x in range(1, GRID_SIZE - 1):
        grid[x] = [0] * GRID_SIZE
        for y in range(1, GRID_SIZE - 1):
            grid[x][y] = get_three_by_three_total(x, y)
    return grid


def get_three_by_three_total(x, y):
    return (get_power_level(x, y) + get_power_level(x+1, y) + get_power_level(x+2, y) +
            get_power_level(x, y+1) + get_power_level(x+1, y+1) + get_power_level(x+2, y+1) +
            get_power_level(x, y+2) + get_power_level(x+1, y+2) + get_power_level(x+2, y+2))


def get_power_level(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += GRID_SERIAL_NO
    power *= rack_id
    power = int(power / 100) % 10 - 5
    return power


def get_max_coord(grid):
    max = 0
    max_coord = (0, 0)
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            if grid[x][y] > max:
                max = grid[x][y]
                max_coord = (x, y)
                print('new max at ({} {}) of {}'.format(x, y, max))
    return max_coord


if __name__ == '__main__':
    main()