import numpy as np
import matplotlib.pyplot as plt
import os

env_list=['Ant-v3','HalfCheetah-v2','HalfCheetah-v3','Hopper-v3','InvertedDoublePendulum-v2','InvertedPendulum-v2','Walker2d-v3','Reacher-v2']

file_path = f'Path\To\Results'
file_name_list = os.listdir(file_path)
# print(len(file_name_list))


for env in env_list:
    evaluations = np.zeros((5, 201))
    i = 0
    for file in file_name_list:
        # print(file)
        file_split = file.split("_")
        # print(file_split)
        data_path = os.path.join(file_path,file)
        # # print(f'{env} v{version} T{T}')
        if file_split[1] == env:
            evaluation = np.load(data_path)
            evaluations[i] = evaluation
            i += 1
    # print(f'env:{env} {evaluations.shape}')
    # print(evaluations)
    
                    
    evaluations_mean = evaluations.mean(axis=0)
    evaluations_std  = evaluations.std(axis=0)
    # # plt.rcParams['axes.facecolor']='whitesmoke'   # whitesmoke, aliceblue, linen, oldlace, cornsilk
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
    if env == 'Reacher-v2':
        plt.ylim((-40,0))
        reacher_range = np.arange(-40.0, 5, 5)
        plt.yticks(reacher_range)
    env_name = f'{env}'
    plt.title('Non-spiking '+env_name)
    if not os.path.exists("./master_savefig"):
        os.makedirs("./master_savefig")
    plt.savefig('./master_savefig/%s.png' % env_name, bbox_inches='tight',dpi=300)
    # plt.show()

