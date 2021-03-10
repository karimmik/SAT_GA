import random
import os
import gc
import timeit

from SAT_SE_Instance import SAT_SE_Instance
from SAT_File import get_opt_solution_value
from Jupyter_Graph import Jupyter_Graph
from Jupyter_Scatter import Jupyter_Scatter

# Solve instance multiple times
# CONST_FILENAME = "./data/wuf20-78-R/wuf20-017.mwcnf"
# jupyter_graph = Desk()
# jupyter_graph.load_opt_value(get_opt_solution_value(CONST_FILENAME))
#
# for label in [f"run_{n}" for n in range(0, 10)]:
#     problem = SAT_SE_Instance()
#     problem.set_configuration(recombination_multiple=1/2,
#                               tournament_size_multiple=1/5)
#     problem.load_from_file(CONST_FILENAME)
#     problem.run()
#     jupyter_graph.add_graph(problem.value_evolution, label)
#
# print(jupyter_graph)

# Solve entire folder

# valuesRobAvg = [1.1717399999998296e-05, 1.1615999999994742e-05, 1.1661399999988831e-05, 1.159979999999372e-05]
# valuesRobMax = [1.3099999999988121e-05, 1.2499999999970868e-05, 1.2499999999970868e-05, 1.2299999999854094e-05]
# X = ['inst n94', 'inst n149', 'inst n207', 'inst n435']
# _X = np.arange(len(X))
# plt.ylabel('seconds')
# plt.bar(_X-0.2, valuesRobAvg, width=0.4, color='y', align='center')
# plt.bar(_X+0.2, valuesRobMax, width=0.4, color='g', align='center')
# plt.xticks(_X, X) # set labels manually
# plt.title('Elapsed avg and max time of GREEDY for instance permutations')
# plt.show()

# CONST_FOLDER_NAME = "./data/wuf50-201-R"
# rel_error = []
# time = []
# # time
# for entry in os.scandir(CONST_FOLDER_NAME):
#     # if len(time) > 100:
#     #     break
#     if entry.path.endswith(".mwcnf") and entry.is_file():
#         filename = entry.path.replace('\\', '/')
#         if get_opt_solution_value(filename) == -1:
#             continue
#
#         print(filename)
#
#         problem = SAT_SE_Instance()
#         problem.set_configuration(pop_reborn=True)
#         problem.load_from_file(filename)
#
#         gc.collect()
#         timerStart = timeit.default_timer()
#
#         problem.run()
#
#         timerEnd = timeit.default_timer()
#         time.append(
#             round((timerEnd - timerStart) * 1000)
#         )
#         apx_value = max(problem.value_evolution)
#         opt_value = get_opt_solution_value(filename)
#         rel_error.append(
#             (opt_value - apx_value) / max(opt_value, apx_value)
#         )
# print(rel_error)
# print(time)
# print(max(rel_error))
#
# bar = Jupyter_Scatter()
# bar.add_scatter(time, CONST_FOLDER_NAME)
# print(bar)
