from molmod import deg
from molmod.ic import bend_angle, dihed_angle
from molmod.molecules import Molecule

from collections import deque


# generator for bonds of length k
def kth_neighbor(mol, start, k):
    que = deque()
    que.append([start])
    current_level = 1

    # level order bfs
    while len(que) > 0 and current_level < k:
        level_size = len(que)
        current_level += 1

        # iterate through the next level
        for _ in range(level_size):
            path = que.popleft()
            current_node = path[-1]

            for next_node in mol.graph.neighbors[current_node]:
                # make sure we do not visit the same node
                if next_node not in path:
                    que.append(path+[next_node])

    # if there is nothing left, there are no bonds of degree k
    while len(que) > 0:
        yield que.popleft()


# list of all unique bonds of length k
def kth_bonds(mol, k=4):
    # inner help function to check if suspect is already in unique
    def is_unique(suspect):
        for bond in unique:
            if sorted(bond) == sorted(suspect):
                return False
        return True

    # result list of unique bonds
    unique = list()

    # iterate through each atom as the starting point
    for i in range(mol.size):
        # find kth degree neighbors
        for bond in kth_neighbor(mol, i, k):
            # add bond to result set if it is unique
            if is_unique(bond):
                unique.append(bond)
                yield bond


# util to print
def pretty(it, delimiter="\n"):
    print(delimiter.join(map(str, it)))


# util to print symbols
def symbolify(mol, it):
    return map(lambda x: mol.symbols[x], it)


# initialize molecule from pdb
def setup(filename="ethane.pdb"):
    mol = Molecule.from_file(filename)

    # setup stuff
    mol.set_default_graph()
    mol.set_default_symbols()

    return mol


if __name__ == "__main__":
    # initialize molecule
    mol = setup("1IRA_R_B_clean.pdb")

    # all bonds of degree 3
    for bond in kth_bonds(mol, 3):
        # find the coordinates of the bonds
        bond_coor = list(map(lambda x: mol.coordinates[x], bond))

        # print symbols of bond and bond angle in degrees
        to_print = [bond]+symbolify(mol, bond)+[bend_angle(bond_coor)[0]/deg]
        pretty(to_print, "\t")

    # all bonds of degree 4
    for bond in kth_bonds(mol, 4):
        # find the coordinates of the bonds
        bond_coor = list(map(lambda x: mol.coordinates[x], bond))

        # print symbols of bond and dihed angle in degrees
        to_print = [bond]+symbolify(mol, bond)+[dihed_angle(bond_coor)[0]/deg]
        pretty(to_print, "\t")
