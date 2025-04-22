# 假设已经加载了pymol模块并打开了一个PyMOL实例
import pymol
from pymol import cmd
from extract_pc_test4 import *
from pymol.cgo import *    # get constants
from math import *
from pymol import cmd

all_pc_coords = []

vec_filename = '../evecs.dat'
principal_components, pc_obj_list = parse_eigenvector_file(vec_filename)

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

    tmp_coords = obj.coordinates
    # 缩放坐标
    scale = 30.0
    coords = [(x*scale, y*scale, z*scale) for x, y, z in tmp_coords]
    all_pc_coords.append(coords)

# 连接到 PyMOL
pymol.finish_launching()

# 加载蛋白质
cmd.load('../comp.pdb')

# 获取所有CA原子的索引
ca_indices = cmd.get_model("comp and name C1'").atom

cutoff = 0
cut = 0.0
factor = 1.0
cutoff_counter = 0
arrow_head_length = 1.4
arrow_head_radius = 0.5
arrow_tail_radius = 0.3
notail = 0
hr, hg, hb, tr, tg, tb = 1.0, 0.0, 1.0, 1.0, 0.0, 1.0

arrow = []

coords_pc1 = all_pc_coords[1]
coords = coords_pc1

# 遍历CA原子
for i, ca_atom in enumerate(ca_indices):
    if i <= -1:
        continue
    # 获取当前CA原子的位置
    ca_position = (ca_atom.coord[0], ca_atom.coord[1], ca_atom.coord[2])
    x1, y1, z1 = ca_atom.coord[0], ca_atom.coord[1], ca_atom.coord[2]
    # 获取目标坐标
    target_position = coords[i]
    x2, y2, z2 = x1 + coords[i][0], y1 + coords[i][1], z1 + coords[i][2]
    print(f"----->{x2},{y2},{z2}")

    vectorx = x2 - x1
    vectory = y2 - y1
    vectorz = z2 - z1
    length = sqrt(vectorx ** 2 + vectory ** 2 + vectorz ** 2)
    if length < cutoff:
        cutoff_counter += 1
        continue
    t = 1.0 - (cut / length)
    x2 = x1 + factor * t * vectorx
    y2 = y1 + factor * t * vectory
    z2 = z1 + factor * t * vectorz
    vectorx = x2 - x1
    vectory = y2 - y1
    vectorz = z2 - z1
    length = sqrt(vectorx ** 2 + vectory ** 2 + vectorz ** 2)
    d = arrow_head_length
    t = 1.0 - (d / length)
    if notail:
        t = 0
    tail = [
        CYLINDER, x1, y1, z1, x1 + (t + 0.01) * vectorx, y1 + (t + 0.01) * vectory, z1 + (t + 0.01) * vectorz, arrow_tail_radius, tr, tg, tb, tr, tg, tb
    ]
    if notail == 0:
        arrow.extend(tail)

    x = x1 + t * vectorx
    y = y1 + t * vectory
    z = z1 + t * vectorz
    dx = x2 - x
    dy = y2 - y
    dz = z2 - z
    intfactor = int(factor)
    
    head = [
        CONE, x, y, z, x + d * dx, y + d * dy, z + d * dz, arrow_head_radius, 0.0, hr, hg, hb, hr, hg, hb, 1.0, 1.0
    ]
    arrow.extend(head)
    
# cmd.show(representation="cartoon", selection='comp')
# 将箭头的 CGO 对象添加到场景中
cmd.load_cgo(arrow, 'arrow')
cmd.bg_color(color="white")

# 调整蛋白质的显示大小和位置
cmd.zoom(0.5)  # 缩小蛋白质，缩放因子为 0.8
cmd.center()  # 将蛋白质居中显示

# 设置需要调整的视角参数
angle = 180   # 旋转的角度
axis = 'x'   # 旋转的轴，可以是 'x'、'y' 或 'z'

# 调整视角
cmd.turn(axis, angle)

cmd.set('ray_shadows', 0)
# 保存图像
cmd.png('arrowc.png', width=800, height=600, dpi=300)