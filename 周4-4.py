import cirpy


def cutter(temp):
    element = temp
    count = 1
    for j, h in enumerate(temp):
        if h.isdigit():
            element = temp[:j]
            count = temp[j:]
            break
    return element, count


class Molecule(cirpy.Molecule):
    def __init__(self, mol):
        cirpy.Molecule.__init__(self, mol)

    def atom_count(self):
        dic = {}
        up = 0
        for i, c in enumerate(self.formula):
            if c.isupper() and i != 0:
                temp = self.formula[up:i]
                dic[cutter(temp)[0]] = cutter(temp)[1]
                up = i
        temp = self.formula[up:]
        dic[cutter(temp)[0]] = cutter(temp)[1]
        return dic


mol = Molecule('methane')
print(mol.atom_count())
