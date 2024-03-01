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
    # plt.rcParams['axes.facecolor']='whitesmoke'   # whitesmoke, aliceblue, linen, oldlace, cornsilk
    fig = plt.figure(figsize=(4, 3))
    ax = plt.axes()
    ax.set_facecolor('#eaeaf2')
    plt.plot(range(len(evaluations_mean)), evaluations_mean,color='blue',lw='1.0')
    plt.fill_between(range(len(evaluations_std)), evaluations_mean-evaluations_std, evaluations_mean+evaluations_std, alpha=0.25)
    
    # 去除图表左侧和底部的刻度线
    plt.tick_params(bottom=False,left=False)

    plt.grid(color='grey',linestyle=':',linewidth=0.5)
    plt.ylabel('Evaluation')
    plt.xlabel('Time steps(1e6)')
    # time_step_range = np.arange(0,1.2,0.2)
    # plt.xticks([1,2,3,4,5],time_step_range)
    env_name = f'{file_split[2]}_'+f'{file_split[3]}_'+f'{file_split[4]}'
    plt.title('Spiking '+env_name)
    if not os.path.exists("./spiking_savefig"):
        os.makedirs("./spiking_savefig")
    plt.savefig('./spiking_savefig/%s.png' % env_name, bbox_inches='tight',dpi=300)
    # plt.show()

