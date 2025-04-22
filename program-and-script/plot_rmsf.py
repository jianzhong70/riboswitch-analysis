import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_paths_3lxl = ['E:/cjzdata2/riboswitch3/riboswitchdat/apodat/mddat/rmsf.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2gdat/mddat/rmsf.dat', 
              'E:\cjzdata2\/riboswitch3\/riboswitchdat\/3d2vdat\mddate\/rmsf.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/rmsf.dat']

#file_paths_3lxk = ['D:/cjzdat/jak3/time/3lxk/bfact.dat',  'D:/cjzdat/jak3/time/3lxkp/bfact.dat', 
#              'D:/cjzdat/jak3/time/3lxkb/bfact.dat']

labels_3lxl = ['APO', 'TPP', 'PYI', 'D2X']
#labels_3lxk = ['MI1-WT', 'MI1-SP', 'MI1-DP']
colors = ['blue', 'red', 'green', 'cyan']

xlabel='Nucleotide Sequence'
ylabel='RMSF(Å)'
offset=0

save_path_3lxl = 'E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/rmsf.png'
#save_path_3lxk = 'D:/cjzdat/jak3/picture/mi1-bfact.png'
show_grid=True

file_paths = file_paths_3lxl
labels = labels_3lxl
save_path = save_path_3lxl

all_data = []

for file_path in file_paths:
    data = np.loadtxt(file_path) # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。
    all_data.append(data)

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x + offset, y, label=labels[i], color=colors[i], linewidth=2.0)
    i = i + 1

ax.set_xlabel(xlabel, fontweight='bold', fontsize=20)
ax.set_ylabel(ylabel, fontweight='bold', fontsize=20)
ax.axis([0, 77, 0, 6])
plt.xticks(fontweight='bold', fontsize=18)
plt.yticks(fontweight='bold', fontsize=18)





#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(13)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(13)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
plt.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), framealpha=0.5)
# 设置图例的字体大小和粗体
for text in legend.get_texts():
    text.set_fontsize(13)  # 设置字体大小
    text.set_fontweight('bold')  # 设置字体粗体

for line in legend.get_lines():
    line.set_linewidth(3)  # 设置图例线条的粗细

#for residue in residue_lst:
    #plt.axvline(x=residue, color='black', linestyle='--', dashes=(5, 2))

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
#plt.ion()
#plt.pause(300)
plt.show()