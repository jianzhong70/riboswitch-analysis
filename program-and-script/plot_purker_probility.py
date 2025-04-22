import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

def format_func(value, tick_number):
    return "{:.2f}".format(value)  # 保留两位小数

#python 3.8+
#plt.style.use('seaborn-v0_8')
#python 3.7-
#plt.style.use('seaborn')

file_paths_3lxl = ['E:/cjzdata2/riboswitch3/riboswitchdat/apodat/mddat/pucker66.agr',
                   'E:/cjzdata2/riboswitch3/riboswitchdat/3d2gdat/mddat/pucker66.agr', 
                   'E:\cjzdata2\/riboswitch3\/riboswitchdat\/3d2vdat\mddate\/pucker66.agr',
                   'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/pucker66.agr']
labels_3lxl = ['APO', 'TPP', 'PYI','D2X']
#labels_3lxk = ['MI1-WT', 'MI1-SP', 'MI1-DP']
colors = ['blue', 'red', 'green', 'cyan']

save_path_3lxl = 'E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/g66-puker.png'
#save_path_3lxk = 'E:/cjzdata2/jak3/timepicture/rmsf_images/mi1-209chi1-line.png'


file_paths = file_paths_3lxl
labels = labels_3lxl
save_path = save_path_3lxl

xlabel = 'Pucker($^\circ$) of G66'
ylabel = 'Probability'

auto_set = True  # you can run auto True first time to see min,max, and bin. Set False if you set user_min, user_max, and user_bin
user_min = 0
user_max = 360
user_bin = 0.4
show_grid = True


all_data = []

for file_path in file_paths:
    data = np.loadtxt(file_path) # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。
    all_data.append(data)

min_val = 0.0
max_val = 0.0
bin = 3

x_lst = []

for data in all_data:
    y = data[:, 1]
    min_local_val = min(y)
    min_val = min(min_val, min_local_val)
    max_local_val = max(y)
    max_val = max(max_val, max_local_val)

if auto_set:
    print("----- auto setting mode ---------")
    print("min_val:", min_val, 'ignore if you set user_min')
    print("max_val:", max_val, 'ignore if you set user_max')
    print("bin:", bin, 'ignore if you set user_bin')
else :
    print("----- user setting mode ---------")
    print("user_min:", user_min)
    print("user_max:", user_max)
    print("user_bin:", user_bin)

if not auto_set:
    min_val = user_min
    max_val = user_max
    bin = user_bin

x_lst = [min_val, min_val + bin]
while x_lst[-1] < max_val:
    last = x_lst[-1]
    x_lst.append(last + bin)

# print("x_sticks:", x_lst)

fig, ax = plt.subplots()
j = 0
for data in all_data:
    y = data[:, 1]
    y_sticks = np.zeros(len(x_lst) - 1, dtype=float)
    for val in y:
        if val == x_lst[-1]:
            y_sticks[-1] = y_sticks[-1] + 1
        else:
            i = int((val - min_val) / bin)
            if i >= 0 and i < len(y_sticks):
                y_sticks[i] = y_sticks[i] + 1
    y_sticks = y_sticks / len(y)
    ax.plot(x_lst[1:], y_sticks, label=labels[j],color=colors[j], linewidth=3)
    j = j + 1
ax.axis([0, 360, 0, 0.10])
ax.set_xlabel(xlabel, fontweight='bold', fontsize=18)
ax.set_ylabel(ylabel, fontweight='bold', fontsize=18)

ax = plt.gca()
# 设置y轴标签格式化器
ax.yaxis.set_major_formatter(FuncFormatter(format_func))

# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(16)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(16)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# plt.title('')
plt.legend()
legend = plt.legend()

# 设置图例的字体大小和粗体
for text in legend.get_texts():
    text.set_fontsize(16)  # 设置字体大小
    text.set_fontweight('bold')  # 设置字体粗体

for line in legend.get_lines():
    line.set_linewidth(4)  # 设置图例线条的粗细

plt.grid(show_grid)
plt.tight_layout()
# plt.savefig(save_path, dpi=600, bbox_inches='tight')
plt.savefig(save_path, dpi=600)
plt.show()
