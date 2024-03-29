# BioInformatics Model Generation
## Steps to run the code
### 1)  PDBDownloader.py
- Make sure you have Python installed on your system. If not, download and install it from the official Python website: https://www.python.org/downloads/
- Ensure you have the required libraries installed. You can install them using pip, the Python package manager.
- Copy the code provided in PDBDownloader.py file into a Python file.
- In the 45th line of this code, replace the 'xxxx' with your desired pdb id.
- Run the Python script.
- After running the script, it will download the PDB file corresponding to the given PDB ID (in this case, 'xxxx') and print its header information.
- You should see output indicating whether the download was successful and the header information extracted from the downloaded PDB file.

### 2)  Code.py
- Ensure you have the required libraries to run this code installed. You can install them using pip, the Python package manager.
- Copy the code you provided in Code.py file into a Python file.
- In the 17th line of the code, replace the pdb id 'xxxx' with your desired pdb id whose PDB file was downloaded by running the code in PDBDownloader.py file.
- In the 18th line of the code, relace the "path of the pdb file downloaded" with the path of the PDB file that you downloded previously.
- Run the Python script.
- The script will read the specified PDB file, extract the coordinates of atoms, visualize them in a 3D plot.
- It will display the PDB header along with the PDB ID as the title of the plot.
- You should see a 3D plot window displaying the atoms' coordinates from the PDB file.

### For Examples:
1) Refer to the file 'Example set.pdf' to see a few examples with code and output. It containd structures of the following:
- FIBRONIGON -(3GHG)
-  HYDROLASE  -(1G0A)
-  LYSOZYME   -(2LZM)
- RNA        -(1EHZ)
2) Refer to the PPT.key for theorey related information about how Linear Algebra plays an important role in BioInformatics model generation.

  # Contributors
K Supriya
