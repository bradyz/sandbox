from random import uniform

import numpy as np
import matplotlib.pyplot as plt


MAX = 20


def plot_line_segment(x1, y1, x2, y2, color="r"):
    plt.plot([p for p in [x1, x2]], [p for p in [y1, y2]], color)


def plot_box(x, y, w, h):
    plot_line_segment(x, y, x, y+h, "k-")
    plot_line_segment(x, y, x+w, y, "k-")
    plot_line_segment(x+w, y, x+w, y+h, "k-")
    plot_line_segment(x, y+h, x+w, y+h, "k-")


def rotate_axis(x, y, u, v):
    a = np.array([[x[0], y[0], 0],
                  [x[1], y[1], 0],
                  [   0,    0, 1]])
    b = np.array([[u[0], v[0], 0],
                  [u[1], v[1], 0],
                  [   0,    0, 1.5]])
    return np.dot(b, np.linalg.inv(a))


def translate_points(u, v):
    return np.array([[1, 0, v[0]-u[0]],
                     [0, 1, v[1]-u[1]],
                     [0, 0,        1]])

if __name__ == "__main__":
    x, y = uniform(1, MAX // 2), uniform(1, MAX // 2)
    w, h = uniform(1, MAX // 2), uniform(1, MAX // 2)

    p = np.array([x + w, y + h])

    t1 = np.array([uniform(MAX // 2, MAX), uniform(MAX // 2, MAX)])
    t2 = np.array([uniform(MAX // 2, MAX), uniform(MAX // 2, MAX)])

    t1t2 = t2 - t1
    t1t2_norm = t1t2 / np.linalg.norm(t1t2)

    n = np.array([-t1t2[1], t1t2[0]])
    n /= np.linalg.norm(n)

    x_axis = (1.0, 0.0)
    y_axis = (0.0, -1.0)
    n_x = (n[0], n[1])
    n_y = (t1t2_norm[0], t1t2_norm[1])

    normal_to_donkey = rotate_axis(x_axis, y_axis, n_x, n_y)

    tmp_o = np.array([[0],
                      [0],
                      [1]])
    tmp_x = np.array([[1],
                      [0],
                      [1]])
    tmp_y = np.array([[0],
                      [-1],
                      [1]])

    rot_o = np.dot(normal_to_donkey, tmp_o)
    rot_x = np.dot(normal_to_donkey, tmp_x)
    rot_y = np.dot(normal_to_donkey, tmp_y)

    # rotated x and -y to donkey axis
    plot_line_segment(rot_o[0], rot_o[1], rot_x[0], rot_x[1], "b-")
    plot_line_segment(rot_o[0], rot_o[1], rot_y[0], rot_y[1], "r-")

    donkey_to_normal = np.linalg.inv(normal_to_donkey)
    t1_to_origin = translate_points((t1[0], t1[1]), (0, 0))
    origin_to_xy = translate_points((0, 0), (x + w, y + h))

    t1_arr = np.array([[t1[0]],
                       [t1[1]],
                       [1]])
    t2_arr = np.array([[t2[0]],
                       [t2[1]],
                       [1]])
    n_arr = np.array([[t1[0] + n[0]],
                      [t1[1] + n[1]],
                      [1]])

    new_t1 = np.dot(origin_to_xy,
                    np.dot(donkey_to_normal, np.dot(t1_to_origin, t1_arr)))
    new_t2 = np.dot(origin_to_xy,
                    np.dot(donkey_to_normal, np.dot(t1_to_origin, t2_arr)))
    new_n = np.dot(origin_to_xy,
                   np.dot(donkey_to_normal, np.dot(t1_to_origin, n_arr)))

    new_t1[0][0] /= new_t1[2][0]
    new_t1[1][0] /= new_t1[2][0]

    new_t2[0][0] /= new_t2[2][0]
    new_t2[1][0] /= new_t2[2][0]

    new_n[0][0] /= new_n[2][0]
    new_n[1][0] /= new_n[2][0]

    # correct tail points
    plt.plot(new_t1[0], new_t1[1], "bo")
    plt.plot(new_t2[0], new_t2[1], "co")

    # correct tail lines
    plot_line_segment(new_t1[0], new_t1[1], new_n[0], new_n[1], "b-")
    plot_line_segment(new_t1[0], new_t1[1], new_t2[0], new_t2[1], "r-")

    # tail points
    plt.plot(t1[0], t1[1], "bo")
    plt.plot(t2[0], t2[1], "co")

    # tail lines
    plot_line_segment(t1[0], t1[1], t1[0] + n[0], t1[1] + n[1], "b-")
    plot_line_segment(t1[0], t1[1], t2[0], t2[1], "r-")

    # donkey
    plot_box(x, y, w, h)
    plt.plot(x+w, y+h, "yo")

    # normal axis
    plot_line_segment(0, 0, 1, 0, "b-")
    plot_line_segment(0, 0, 0, -1, "r-")

    # scale
    plt.ylim([-1, 1.1 * MAX])
    plt.xlim([-1, 1.1 * MAX])

    plt.show()
