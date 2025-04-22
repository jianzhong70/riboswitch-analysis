import matplotlib.pyplot as plt
import numpy as np


file_paths = ['E:/cjzdata2/riboswitch3/riboswitchdat/3d2gdat/mddat/81-66.dat', 
              'E:\cjzdata2\/riboswitch3\/riboswitchdat\/3d2vdat\mddate\/82-66.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/82-66.dat']
labels = ['TPP', 'PYI','D2X']
colors = ['red', 'green', 'cyan']

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
    ax.scatter(x, y, label=labels[i], color=colors[i], s=0.5)
    i = i + 1

ax.axis([0, 4000, 0, 12])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=16)
ax.set_ylabel('Ligand-G66 distance(Å)',fontweight='bold', fontsize=16)

save_path='E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/dist66-time.png'
show_grid=True

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(14)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(14)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)
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