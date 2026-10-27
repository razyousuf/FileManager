from create_structure import CreateStructure
from run import run_file_manager

create_structure = CreateStructure()
create_structure.create_folders()
create_structure.create_files()

run_file_manager()