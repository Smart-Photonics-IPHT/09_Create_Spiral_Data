
import os
from pathlib import Path
from Create_Spirals_Dataset_Functions import generate_multiple_spirals

theta_maxes = [0.25, 0.5, 1, 2, 4, 6, 8, 10, 12]
theta_maxes = [10]
max_noises = [0]


main_dir = os.path.abspath(os.getcwd())
# main_dir = r'C:\Sobhi\Nov_24_paper'


for index3, theta_max in enumerate(theta_maxes):
    subfolder3 = f'theta_max={theta_max}'
    for index4, max_noise in enumerate(max_noises):  # to be done 0, 0.1, 0.2,
        # encode the input dataset and create a mask
        subfolder4 = f'max_noise={max_noise}'
        work_dir = f'{main_dir}/Dataset/{subfolder3}/{subfolder4}'
        if not Path(work_dir).exists():
            Path(work_dir).mkdir(parents=True, exist_ok=True)
        # dataimport = load_dat.DataImport(dataset, 'PF')    # normtype='PF' for normalization
        generate_multiple_spirals(work_dir, theta_max, totalpoints=250, spirals_number=4,
             max_noise=max_noise, save_results_in_text_file=True, save_plot=True, show_plot=False, normalizing=True)
