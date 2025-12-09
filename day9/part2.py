with open('day9/input.txt', 'r') as f:
    lines = [tuple(map(int, line.strip().split(','))) for line in f]

edges = []
for i in range(len(lines)):
    x1, y1 = lines[i]
    x2, y2 = lines[(i + 1) % len(lines)]
    if x1 == x2:
        edges.append((min(y1, y2), max(y1, y2), x1, 'V'))
    else:
        edges.append((min(x1, x2), max(x1, x2), y1, 'H'))
    
max_area = 0
for a in lines:
    for b in lines:
        
        min_x = min(a[0], b[0])+0.5
        max_x = max(a[0], b[0])-0.5
        min_y = min(a[1], b[1])+0.5
        max_y = max(a[1], b[1])-0.5

        valid = True

        delta_x = abs(a[0] - b[0]) + 1
        delta_y = abs(a[1] - b[1]) + 1
        area = delta_x * delta_y
        print(a, b, delta_x, delta_y, area)

        for i in range(len(edges)):
            edge = edges[i]
            if edge[3] == 'V':
                y_start, y_end, x, _ = edge

                
                perp_inside = (min_x < x < max_x)
                range_overlap = not (y_end < min_y or y_start > max_y)

                if perp_inside and range_overlap:
                    valid = False
                    break

            else:  
                x_start, x_end, y, _ = edge 

                
                perp_inside = (min_y < y < max_y)
                range_overlap = not (x_end < min_x or x_start > max_x)

                if perp_inside and range_overlap:
                    valid = False
                    break

        if not valid:
            continue

        if area > max_area:
            max_area = area

print(max_area)