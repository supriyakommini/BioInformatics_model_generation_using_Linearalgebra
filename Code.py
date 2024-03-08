from Bio import PDB
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def extract_pdb_header(pdb_path):
    try:
        parser = PDB.PDBParser(QUIET=True)
        structure = parser.get_structure('temp', pdb_path)
        header_lines = structure.header.get('head', [])
        header_str = ''.join(header_lines)
        return header_str
    except Exception as e:
        print(f"Error: {e}")
        return None

pdb_id = "xxxx"
pdb_filename = f"path of the pdb file downloaded"
structure = PDB.PDBParser(QUIET=True).get_structure(pdb_id, pdb_filename)

atom_coords = [] 
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                atom_coords.append(atom.get_coord())

atom_coords_array = np.array(atom_coords)

pdb_header = extract_pdb_header(pdb_filename)
print(pdb_header)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(atom_coords_array[:, 0], atom_coords_array[:, 1], atom_coords_array[:, 2], marker='o', s=10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'{pdb_header} ({pdb_id})')

plt.show()
