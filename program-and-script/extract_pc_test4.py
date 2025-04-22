import re
import numpy as np

class PCObject:
    def __init__(self, pc_number, pc_ratio):
        self.pc_number = pc_number
        self.pc_ratio = pc_ratio
        self.coordinates = []
        self.num_residues = 0

def parse_eigenvector_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # 在最后一行后面追加一个回车
    lines.append('\n')

    principal_components = []
    pc_obj_list = []
    num_lines = len(lines)

    num_residues = 0

    is_reading_coordinates = False
    is_reading_header = False
    stop_parse_header = False
    current_pc_obj = None

    count = 0
    for line in lines:
        count += 1
        if 'Eigenvector file' in line:
            is_reading_coordinates = False
            is_reading_header = True
        elif "****" in line or count == num_lines:
            if "****" in line:
                principal_components.append(line.strip())
            is_reading_coordinates = False
            is_reading_header = False
            if current_pc_obj is not None:
                print(f"current pc number: {current_pc_obj.pc_number}, coordinates shape: {len(current_pc_obj.coordinates)}")
                # reshape the coordinates before append it to the list
                current_pc_obj.coordinates = np.array(current_pc_obj.coordinates).reshape(-1, 3)
                current_pc_obj.num_residues = int(num_residues)
                pc_obj_list.append(current_pc_obj)
                current_pc_obj = None
        elif not is_reading_coordinates and not is_reading_header:
            info = line.split()
            component_number = info[0].strip()
            component_ratio = float(info[1])
            pc_str = f":  {component_number} : {component_ratio}"
            principal_components[-1] += pc_str
            current_pc_obj = PCObject(component_number, component_ratio)
            is_reading_coordinates = True
        elif not is_reading_coordinates and is_reading_header:
            info = line.split()
            if not stop_parse_header:
                total_coordinates = int(info[0])
                num_residues = total_coordinates/3
                stop_parse_header = True
                print(f"\nTotal Residues: {num_residues}")
        else:
            coords = list(map(float, re.findall(r"[-+]?\d*\.\d+|\d+", line)))
            current_pc_obj.coordinates.extend(coords)

    return principal_components, pc_obj_list

if __name__ == "__main__":
    filename = 'evecs3.dat'
    principal_components, pc_obj_list = parse_eigenvector_file(filename)

    for pc in principal_components:
        print(pc)

    for obj in pc_obj_list:
        if obj.num_residues != obj.coordinates.shape[0]:
            print(f"Residues number({obj.num_residues}) is not equal to the coordinates number/3({obj.coordinates.shape[0]}).")
            break
        print(f"\nPrincipal Component {obj.pc_number} Coordinates:")
        for j in range(obj.num_residues):
            print(f"Residue {j+1}: \
                X={obj.coordinates[j][0]}, \
                Y={obj.coordinates[j][1]}, \
                Z={obj.coordinates[j][2]}")