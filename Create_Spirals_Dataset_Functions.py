import numpy as np
import matplotlib.pyplot as plt
import os

#Normalized 2D Archimedean Spirals
def generate_multiple_spirals(saving_dir, theta_max, totalpoints=250, spirals_number=4, max_noise=0,
                              save_results_in_text_file=True, save_plot=True, show_plot=False, normalizing=True):
    #return a * np.exp(b * t) * np.array([np.cos(t), np.sin(t)])

    step = theta_max*np.pi/totalpoints
    t = np.linspace(step, theta_max*np.pi, totalpoints)

    Spirals = []
    if normalizing:
        for i in range(0, spirals_number):
            Spirals.append((t/(theta_max*np.pi)) * np.array([np.cos(t + i*2*np.pi/spirals_number),
                        np.sin(t + i*2*np.pi/spirals_number)]) + np.random.uniform(-max_noise/(theta_max*np.pi),
                        max_noise/(theta_max*np.pi), totalpoints))
    else:
        for i in range(0, spirals_number):
            Spirals.append(t * np.array([np.cos(t + i*2*np.pi/spirals_number),
                        np.sin(t + i*2*np.pi/spirals_number)]) + np.random.uniform(-max_noise,
                        max_noise, totalpoints))
    #plot results
    plt.figure(figsize=(16, 16))

    if spirals_number == 4:
        [spiral1, spiral2, spiral3, spiral4] = Spirals[:spirals_number]

        plt.scatter(spiral1[0], spiral1[1], s=50, label='Spiral 1', color='blue')
        plt.scatter(spiral2[0], spiral2[1], s=50, label='Spiral 2', color='green')
        plt.scatter(spiral3[0], spiral3[1], s=50, label='Spiral 3', color='red')
        plt.scatter(spiral4[0], spiral4[1], s=50, label='Spiral 4', color='black')

    else:
        for index, spiral_i in enumerate(Spirals):
            plt.scatter(Spirals[index][0], Spirals[index][1], s=50, label=f'Spiral {index+1}')

    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    pi_symbol = '\u03c0'
    plt.title(f'{spirals_number} Spirals_Theta-Max={theta_max}{pi_symbol}_Max-Noise={max_noise}_ '
              f'points-count-per-spiral={totalpoints}', fontsize=24)
    plt.gca().set_aspect('equal')
    #plt.legend(fontsize=14, loc='upper left')

    if save_plot:
        plt.legend(loc='center', bbox_to_anchor=(1.061, 0.5), fontsize=14)
        plt.savefig(f'{saving_dir}/Dataset_{spirals_number}-Spirals_theta-max={theta_max}pi_max-noise={max_noise}.png')
    if show_plot:
        plt.legend(loc='center', bbox_to_anchor=(1.13, 0.5), fontsize=14)
        plt.show()

    plt.close()
    spirals_data = []
    for index, spiral_i in enumerate(Spirals):
        combined_array = np.column_stack(((index+1)*np.ones(len(spiral_i[0])), spiral_i[0].flatten(),
                                          spiral_i[1].flatten()))
        spirals_data.append(combined_array)
    all_labels_coordinates = np.vstack([combined_array_i for combined_array_i in spirals_data])

    if save_results_in_text_file:
        filename = f'{saving_dir}/Dataset_{spirals_number}-Spirals_theta-max={theta_max}pi_max-noise={max_noise}' \
                   f'_points-count-per-spiral={totalpoints}.txt'
        np.savetxt(filename, all_labels_coordinates, fmt='%1.4f', delimiter=',')

    return all_labels_coordinates



