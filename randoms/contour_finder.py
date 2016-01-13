import os

from matplotlib import pyplot as plt

from queue import Queue
from random import randrange

# pip install pillow
from PIL import Image

TOTAL = 5
COUNT = 0

# directional vectors for graph traversal
DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DIR2 = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
DEBUG = False

# USAGE: change the directories to the folder containing the png files
#        make sure the out directory already exists
OUT_DIRECTORY = "/Users/brady/code/research/VolRoverN/data/VolRoverN-sample/traces/another_test"
IMG_DIRECTORY = "/Users/brady/Downloads/RhoANA_red_dendrite_2k_left"

OUT_DIRECTORY = "/Users/brady/code/research/VolRoverN/data/VolRoverN-sample/traces/test"
IMG_DIRECTORY = "/Users/brady/code/research/VolRoverN/data/VolRoverN-sample/ocp"

# change this to limit number of contours
CONTOUR_LIMIT = 1000000

# change this if you want a minimum size
MIN_SIZE = 1000

def det(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])


def colinear(a, b, c):
    return det(a, b, c) == 0


def cw_turn(a, b, c):
    return det(a, b, c) < 0


def ccw_turn(a, b, c):
    return not cw_turn(a, b, c) and not colinear(a, b, c)

# returns the connected components of a graph
def components_of(all_points):
    def bfs(x, y):
        que = Queue()
        que.put((x, y))

        contour = [(x, y)]
        visited.add((x, y))

        while not que.empty():
            cx, cy = que.get()

            for dx, dy in DIR2:
                xp = cx + dx
                yp = cy + dy

                if (xp, yp) not in all_points_set or (xp, yp) in visited:
                    continue

                visited.add((xp, yp))
                que.put((xp, yp))
                contour.append((xp, yp))

        return contour

    contours = list()
    visited = set()

    all_points_set = set(all_points)

    for point in all_points:
        if point not in visited:
            contours.append(bfs(*point))

    return contours


def find_connected_components(image, ROW, COL, to_write):
    # utility generator function to find valid neighbors
    def neighbors(x, y):
        for dx, dy in DIR:
            xp, yp = x + dx, y + dy
            bounds = True
            if xp < 0 or xp >= ROW or yp < 0 or yp >= COL:
                bounds = False
            yield xp, yp, bounds

    def bfs(x, y):
        que = Queue()
        que.put((x, y))

        res = set()
        res.add((x, y))

        result_list = list()
        result_list.append((x, y))

        visited[x][y] = True

        while not que.empty():
            cx, cy = que.get()

            for xp, yp, in_bounds in neighbors(cx, cy):
                # if the current point is a border, add it to the contour
                if not in_bounds or pix[cx, cy] != pix[xp, yp]:
                    if (cx, cy) not in res:
                        result_list.append((cx, cy))
                    res.add((cx, cy))
                    continue
                elif visited[xp][yp]:
                    continue

                visited[xp][yp] = True
                que.put((xp, yp))

        return result_list

    # 2D array of colors
    pix = image.load()
    # visited array for breadth first search
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    # map of color to list of connected components (which are lists)
    components = dict()

    # iterate through entire picture
    for i in range(ROW):
        for j in range(COL):
            color = pix[i, j]
            # ignore black
            if color == (0, 0, 0):
                continue
            elif visited[i][j]:
                continue
            if color != (0, 0, 21):
                continue

            visited[i][j] = True

            # HACK to limit number of contours
            if color in to_write or len(to_write) < CONTOUR_LIMIT:
                all_points = bfs(i, j)

                # the minimum size of a contour
                if len(all_points) < MIN_SIZE:
                    continue

                # one bfs can have several contours
                for contour in components_of(all_points):
                    # order the points to be written
                    ordered_contour = orderedV2(contour)

                    # if there is a valid contour
                    if ordered_contour and len(ordered_contour) >= MIN_SIZE:
                        # add the current color to be written
                        to_write.add(color)

                        # make sure the contour goes into the same color
                        if color in components:
                            components[color].append(ordered_contour)
                        else:
                            components[color] = [ordered_contour]

    return components


def write_xml(index, val, color_to_name, used_names, ROW, COL):
    # generate random names that havent been used yet
    def random_name(color):
        name = None

        while not name or name in used_names:
            name = "".join(map(chr, (randrange(97, 123) for _ in range(6))))

        color_to_name[color] = name
        used_names.add(name)

        return name

    # name of trace file
    out = open(os.path.join(OUT_DIRECTORY, "test."+index), "w")

    # necessary metadata stuff
    out.write('<?xml version="1.0"?>\n')
    out.write("<!DOCTYPE Section SYSTEM 'section.dtd'>\n")
    out.write('<Section alignLocked="true" index="' + str(index) + '" thickness="0.05">\n')

    # iterate through each color
    for color in val:
        if color in color_to_name:
            name = color_to_name[color]
        else:
            name = random_name(color)

        for contour in val[color]:
            # contour is an empty list
            if not contour:
                continue

            # required stuff
            out.write('\t<Transform dim="0"\n')
            out.write('\t\txcoef=" 0 1 0 0 0 0"\n')
            out.write('\t\tycoef=" 0 0 1 0 0 0">\n')
            out.write('\t\t<Contour border="0 1 0" closed="true" fill="0 1 0" hidden="false" mode="9"\n')
            out.write('\t\t\tname="' + str(name) + '"\n')

            for i, coord in enumerate(contour):
                x, y = coord
                rx, ry = x, COL - y

                if i == 0:
                    out.write('\t\t\tpoints="' + str(rx) + " " + str(ry) + ",\n")
                elif i == len(contour) - 1:
                    out.write("\t\t\t\t" + str(rx) + " " + str(ry) + '"\n')
                else:
                    out.write("\t\t\t\t" + str(rx) + " " + str(ry) + ",\n")

            out.write('\t\tsimplified="true"/>\n')
            out.write('\t</Transform>\n')

    out.write("</Section>\n")
    out.close()


def process_image(filename, index, color_to_name, used_names, to_write):
    image = Image.open(filename)
    ROW, COL = image.size
    components = find_connected_components(image, ROW, COL, to_write)
    write_xml(index, components, color_to_name, used_names, ROW, COL)
    return ROW, COL


# orders the points to be plotted correctly
def orderedV2(contour):
    def adjacent_cells(x, y):
        return {(x+dx, y+dy) for dx, dy in DIR2 if (x+dx, y+dy) in contour}

    def bfs(start, end):
        que = Queue()
        que.put(start)

        parent = {start: (-1, -1)}

        while not que.empty():
            cell = que.get()
            if cell == end:
                break
            for adj in graph[cell]:
                if adj in parent:
                    continue
                parent[adj] = cell
                que.put(adj)

        result = list()
        backtrack = end

        while backtrack in parent:
            result.append(backtrack)
            backtrack = parent[backtrack]

        return result

    # construct the graph
    graph = {cell: adjacent_cells(*cell) for cell in contour}
    # points that have more than 2 neighbors
    problem = list()

    # start and end of graph traversal
    start = (-1, -1)
    end = (-1, -1)

    for cell in graph:
        if len(graph[cell]) > 2:
            problem.append(cell)
        # find a potential starting point
        if start == (-1, -1):
            candidate = len(graph[cell]) == 2
            for n1 in graph[cell]:
                candidate = candidate and len(graph[n1]) == 2
                for n2 in graph[n1]:
                    candidate = candidate and len(graph[n2]) == 2
            if candidate:
                start = cell

    # found a valid starting point
    if start != (-1, -1):
        end = graph[start].pop()

    # reduce number of edges for an easier traversal
    for cell in problem:
        if len(graph[cell]) > 2:
            new_neighbors = set()
            for neighbor in graph[cell]:
                if len(graph[neighbor]) == 2:
                    new_neighbors.add(neighbor)
            if len(new_neighbors) >= 2:
                for old in graph[cell]:
                    if old not in new_neighbors:
                        graph[old].remove(cell)
                graph[cell] = new_neighbors

    contour = set(contour)

    # if there is a valid contour
    if start != (-1, -1) and end != (-1, -1):
        result = bfs(start, end)
    else:
        result = list()

    # plot stuff if something failed
    if not result and DEBUG:
        print(len(contour))
        for c in contour:
            print(" ".join(map(str, c)))

    # ordered by CCW
    if result:
        top_index = -1

        for i in range(len(result)):
            point = result[i]
            if top_index == -1 or point[1] > result[top_index][1]:
                top_index = i

        top_point = result[top_index]
        right_neighbor = result[(top_index + 1) % len(result)]
        left_neighbor = result[(top_index - 1) % len(result)]

        if cw_turn(top_point, right_neighbor, left_neighbor):
            result = result[top_index::-1] + result[:top_index:-1]
        else:
            result = result[top_index:] + result[:top_index]

        global COUNT
        COUNT += 1
        ax1 = plt.subplot(5, 3, COUNT)
        ax1.plot([p[0] for p in result], [p[1] for p in result], "g,")
        ax1.plot(result[0][0], result[0][1], "bo")
        h = len(result) // 2
        ax1.plot([p[0] for p in result[:h]], [p[1] for p in result[:h]], "r-")

    return result


def generate_contours():
    # metadata
    xdim = 0
    ydim = 0
    min_index = 100000
    max_index = -1

    color_to_name = dict()
    used_names = set()
    to_write = set()

    # goes through each png
    for filename in os.listdir(IMG_DIRECTORY):
        if filename[-4:] != ".png":
            continue

        # filenaming stuff
        fullname = os.path.join(IMG_DIRECTORY, filename)
        index = filename.lstrip("labels_").rstrip(".png").lstrip("0")

        if not index:
            index = "0"

        # finding bounds of pictures - used in vrs file
        min_index = min(min_index, int(index))
        max_index = max(max_index, int(index))

        # creates a single series file
        print("PROCESSING: " + filename)
        xdim, ydim = process_image(fullname, index, color_to_name, used_names, to_write)

    plt.show()

    # write vrs config file
    vrs = open(os.path.join(OUT_DIRECTORY, "test.vrs"), "w")
    vrs.write("VRS 1.0\n")
    vrs.write("BB_XMIN 0\n")
    vrs.write("BB_XMAX " + str(xdim) + "\n")
    vrs.write("BB_YMIN 0\n")
    vrs.write("BB_YMAX " + str(ydim) + "\n")
    vrs.write("BB_ZMIN " + str(min_index) + "\n")
    vrs.write("BB_ZMAX " + str(max_index) + "\n")
    vrs.write("ZSPACING 0.05")
    vrs.close()

    # write ser config file
    ser = open(os.path.join(OUT_DIRECTORY, "test.ser"), "w")
    ser.write('<?xml version="1.0"?>\n')
    ser.write('<!DOCTYPE Series SYSTEM "series.dtd">\n')
    ser.write('<Series\n')
    ser.write('\tfirst3Dsection="'+str(min_index)+'"\n')
    ser.write('\tlast3Dsection="'+str(max_index)+'"\n')
    ser.write('\t>\n')
    ser.write('</Series>')
    ser.close()


if __name__ == "__main__":
    generate_contours()
