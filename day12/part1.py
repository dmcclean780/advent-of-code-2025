def is_break_line(line):
    # Matches patterns like "4x4: 0 0 0 0 2 0"
    if ":" not in line:
        return False
    left = line.split(":")[0]
    if "x" not in left:
        return False
    w, h = left.split("x")
    return w.isdigit() and h.isdigit()

with open('day12/input.txt', 'r') as f:
    lines = [line.strip() for line in f]

shapes = {}
current_id = None
current_grid = []
current_area = 0
remaining_lines = lines.copy()
for line in lines:
    
    
    
    if is_break_line(line):
        break
    remaining_lines.remove(line)
    
    if not line:
        continue

    if line.endswith(":") and line[:-1].isdigit():
            # Save previous grid if any
        if current_id is not None and current_grid:
            shape = {'grid': [list(row) for row in current_grid],
                     'area': sum(char == '#' for row in current_grid for char in row)}
            shapes[current_id] = shape
        current_id = int(line[:-1])
        current_grid = []
    else:
        # Must be a row of the grid
        current_grid.append(line)

    

    # Save the last one
if current_id is not None and current_grid:
    shape = {'grid': [list(row) for row in current_grid],
                     'area': sum(char == '#' for row in current_grid for char in row)}
    shapes[current_id] = shape

areas = []
for line in remaining_lines:
    area = {}
    area["length"] = int(line.split()[0].strip(":").split("x")[0])
    area["width"] = int(line.split()[0].strip(":").split("x")[1])
    area["area"] = area["length"] * area["width"]
    area["parcels"] = [int(x) for x in line.split()[2:]]
    areas.append(area)

possible_areas = 0
for area in areas:
    print("Max Area:", area["area"])
    total_needed_area = 0
    for i in range(len(area["parcels"])):
        shape_quantity = area["parcels"][i]
        shape_id = i
        total_shape_area = 9 * shape_quantity
        total_needed_area += total_shape_area
    print("Total Needed Area:", total_needed_area)
    if total_needed_area <= area["area"]:
        possible_areas += 1

print("Total Areas:", len(areas))
print("Possible Areas:", possible_areas)

