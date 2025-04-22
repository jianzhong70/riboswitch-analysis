import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


file_paths_3lxl = ['E:/cjzdata2/riboswitch3/riboswitchdat/apodat/mddat/gry.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2gdat/mddat/gry.dat', 
              'E:\cjzdata2\/riboswitch3\/riboswitchdat\/3d2vdat\mddate\/gry.dat',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/gry.dat']

#file_paths_3lxk = ['E:\cjzdata2\jak3\/time\/3lxk/surf.dat',  'E:\cjzdata2\jak3\/time\/3lxkp/surf.dat', 
#              'E:\cjzdata2\jak3\/time\/3lxkb/surf.dat']

labels_3lxl = ['APO', 'TPP', 'PYI', 'D2X']
#labels_3lxk = ['MI1-WT', 'MI1-SP', 'MI1-DP']
colors = ['blue', 'red', 'green', 'cyan']

file_paths = file_paths_3lxl
labels = labels_3lxl

all_data = []
category_lst = []
i = 0
for file_path in file_paths:
    data = np.loadtxt(file_path)  # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。
    for row in data:
        all_data.append(row[1])
        category_lst.append(labels[i])
    i = i + 1

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

df = pd.DataFrame({
    'value': np.array(all_data),
    'category': category_lst
})

#ax.boxplot(all_data)
#sns.boxplot(x="category", y="value", data=df)
#sns.boxplot(x="category", y="value", data=df)
sns.violinplot(x="category", y="value", data=df, palette=colors)
#sns.boxplot(x="category", y="value", data=df, palette=colors)
#ax.axis([0, 3000, 0, 20])

ax.set_xlabel('System indexes', fontweight='bold',fontsize=18)
ax.set_ylabel('Radius of gyration($\mathring{A}$)',fontweight='bold', fontsize=18)

save_path_3lxl = 'E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/rna-gry-violin.png'
#save_path_3lxk = 'E:/cjzdata2/jak3/timepicture/rmsf_images/mi1-surf-violin.png'

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
    label.set_fontsize(16)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)
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