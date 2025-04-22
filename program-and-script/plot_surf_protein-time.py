import matplotlib.pyplot as plt
import numpy as np
import os


file_paths_3lxl = ['E:/cjzdata2/riboswitch3/riboswitchdat/apodat/mddat/surf.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2gdat/mddat/surf.dat', 
              'E:\cjzdata2\/riboswitch3\/riboswitchdat\/3d2vdat\mddate\/surf.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/surf.dat']

#file_paths_3lxk = ['E:\cjzdata2\jak3\/time\/3lxk\surf.dat',  'E:\cjzdata2\jak3\/time\/3lxkp\surf.dat', 
#              'E:\cjzdata2\jak3\/time\/3lxkb\surf.dat']

labels_3lxl = ['APO', 'TPP', 'PYI', 'D2X']
#labels_3lxk = ['MI1-WT', 'MI1-SP', 'MI1-DP']
colors = ['blue', 'red', 'green', 'cyan']
#labels_3lxk = ['MI1-WT', 'MI1-SP', 'MI1-DP']

file_paths = file_paths_3lxl
labels = labels_3lxl
#colors = ['blue', 'orange', 'green', 'red']

all_data = []
for file_path in file_paths:
    data = np.loadtxt(file_path)
    all_data.append(data)

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = 0.004*data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x, y, label=labels[i],color=colors[i])
    i = i + 1

ax.axis([0, 4000, 10600, 13400])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('Surface($\mathring{A}^2$)',fontweight='bold', fontsize=18)
#xlabel = 'Surface($\mathring{A}^2$)'

save_path_3lxl = 'E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/surf-time.png'
#save_path_3lxk = 'E:/cjzdata2/jak3/timepicture/rmsf_images/mi1-surf-time.png'

show_grid=True

save_path = save_path_3lxl

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(16)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(15)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), framealpha=0.5)
# 设置图例的字体大小和粗体
for text in legend.get_texts():
    text.set_fontsize(16)  # 设置字体大小
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