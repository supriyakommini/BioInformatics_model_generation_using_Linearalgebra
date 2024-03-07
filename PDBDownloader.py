import os
import requests
from Bio.PDB import PDBParser

class PDBDownloader:
    def __init__(self, download_path="PDB_files"):
        self.download_path = download_path

    def download_pdb(self, pdb_id):
        try:
            if not os.path.exists(self.download_path):
                os.makedirs(self.download_path)

            pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

            response = requests.get(pdb_url)
            if response.status_code == 200:
                pdb_filename = f"{pdb_id.lower()}.pdb"
                pdb_path = os.path.join(self.download_path, pdb_filename)

                with open(pdb_path, 'wb') as pdb_file:
                    pdb_file.write(response.content)

                print(f"Successfully downloaded {pdb_id} to {pdb_path}")

                header = self.extract_header(pdb_path)
                print("Header:")
                print(header)

            else:
                print(f"Failed to download {pdb_id}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")

    def extract_header(self, pdb_path):
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure('temp', pdb_path)
        header_lines = structure.header.get('head', [])
        header_str = ''.join(header_lines)
        return header_str

if __name__ == "__main__":
    pdb_downloader = PDBDownloader()
    pdb_id_to_download = 'xxxx'
    pdb_downloader.download_pdb(pdb_id_to_download)
