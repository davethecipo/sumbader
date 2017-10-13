import argparse


def parse_cli():
    """Return the arguments as parsed from argparse"""
    parser = argparse.ArgumentParser(description="Sum the Bader charges of some atoms")
    parser.add_argument('filename', help='the ACF.dat file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--range', help='a range of atom in the form N-M')
    group.add_argument('--atoms', nargs='*', help='list of integers indicating the atom indexes, e.g 2 3 9 7')
    cliargs = parser.parse_args()
    return cliargs

def check_duplicates(lst):
    """Raise ValueError if lst containes duplicates"""
    for elem in lst:
        if lst.count(elem) > 1:
            raise ValueError('The value {} is present more than once'.format(elem))

def charge_of_atoms(fileobj, *atom_idx):
    """Return list of floats of the Bader charge corresponding to atoms of index atom_idx"""
    charges = []
    text_lines = fileobj.readlines()[2:-1]
    for idx in atom_idx:
        line = text_lines[idx-1]
        charge = float(line.split()[4])
        charges.append(charge)
    return charges


def main():
    cliargs = parse_cli()
    if cliargs.range:
        start, finish = [int(i) for i in cliargs.range.split('-')]
        indexes = range(start, finish + 1)
    else:
        check_duplicates(cliargs.atoms)
        indexes = [int(i) for i in cliargs.atoms]
    # since the QM calculations don't have a lot of atoms, we can load the ACF.dat file all in memory
    with open(cliargs.filename, 'rt') as f:
        charges = charge_of_atoms(f, *indexes)
    total_charge = sum(charges)
    print(total_charge)

