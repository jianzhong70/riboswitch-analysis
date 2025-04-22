import matplotlib.pyplot as plt
import numpy as np


file_paths = ['E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/v0.out', 
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/v1.out',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/v2.out',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/v3.out',
              'E:/cjzdata2/riboswitch3/riboswitchdat/3d2xdat/mddat/v4.out']
labels = ['D2X@OAJ...G66@H1', "D2X@NAC...G28@H22", 'D2X@OAX...C65@H41', 
          'D2X@H15...G28@N3', "D2X@OAJ...G66@H21"]
colors = ['black','blue', 'red', 'green', 'cyan']

all_data = []
for file_path in file_paths:
    data = np.loadtxt(file_path)
    all_data.append(data)

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x, y, label=labels[i], color=colors[i], linewidth=3.0)
    i = i + 1

ax.axis([0, 100, 0.83, 1])

ax.set_xlabel('τ(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('C(τ)',fontweight='bold', fontsize=18)

save_path='E:/cjzdata2/riboswitch3/riboswitchdat/timepicture/rmsf_images/d2x-time-correlation.png'
show_grid=True

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
for label in ax.get_xticklabels():
    label.set_fontsize(14)  
    label.set_fontweight('bold')  

for label in ax.get_yticklabels():
    label.set_fontsize(14)  
    label.set_fontweight('bold') 

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)

for text in legend.get_texts():
    text.set_fontsize(13)  
    text.set_fontweight('bold')  

for line in legend.get_lines():
    line.set_linewidth(3) 
#for residue in residue_lst:
    #plt.axvline(x=residue, color='black', linestyle='--', dashes=(5, 2))

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
#plt.ion()
#plt.pause(300)
plt.show()