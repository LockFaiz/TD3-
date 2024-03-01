import numpy as np
import matplotlib.pyplot as plt
import os

file_path = f'Path\To\Spiking_Results'
file_name_list = os.listdir(file_path)
# print(len(file_name_list))
 
for file in file_name_list:
    file_split = file.split("_")
    # print(file_split)
    data_path = os.path.join(file_path,file)
    data_name_list = os.listdir(data_path)
    evaluations = np.zeros((len(data_name_list), 201))
    # print(f'{env} v{version} T{T}')
    for i in range(len(data_name_list)):
        evaluation = np.load(os.path.join(data_path, data_name_list[i]))
        evaluations[i, :] = evaluation

                    
    evaluations_mean = evaluations.mean(axis=0)
    evaluations_std  = evaluations.std(axis=0)
    plt.rcParams['axes.facecolor']='whitesmoke'   # whitesmoke, aliceblue, linen, oldlace, cornsilk
    fig = plt.figure(figsize=(4, 3))
    # ax = plt.axes()
    # ax.set_facecolor('#eaeaf2')

    plt.plot(range(len(evaluations_mean)), evaluations_mean,color='#fb7f1d',lw='2.0')
    plt.fill_between(range(len(evaluations_std)), evaluations_mean-evaluations_std, evaluations_mean+evaluations_std, facecolor='#fb7f1d', alpha=0.25)
    
    # 去除图表左侧和底部的刻度线
    plt.tick_params(bottom=False,left=False)

    plt.grid(color='grey',linestyle=':',linewidth=0.5)
    plt.ylabel('D4RL Score',fontdict={'size':14})
    plt.xlabel('Iterations(×5000)',fontdict={'size':14})
    plt.yticks(range(0,12000,2000),labels=['0','20','40','60','80','100'],size=14)
    plt.xticks(size=14)
    env_name = f'{file_split[2]}_'+f'{file_split[3]}_'+f'{file_split[4]}'
    # plt.title('Spiking '+env_name)
    if not os.path.exists("./spiking_savefig_v2"):
        os.makedirs("./spiking_savefig_v2")
    plt.savefig('./spiking_savefig_v2/%s.pdf' % env_name, bbox_inches='tight',dpi=300)
    # plt.show()

