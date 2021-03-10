class Jupyter_Graph:
    values = ""
    labels = ""
    graphs_count = 1
    post_fix = f"plt.ylabel('value')\n" \
              f"plt.xlabel('generation')\n" \
              f"plt.legend()\n" \
              f"plt.show()\n"
    middle_fix = f"plt.figure(figsize=(9, 6))\n"

    def load_opt_value(self, opt_value):
        # opt_value = get_opt_solution_value(filename)
        self.values += f"param_opt = [{opt_value}]\n"
        self.labels += f"plt.plot(param_opt, label=\"optimal value\")\n"

    def add_graph(self, value, label):
        self.values += f"param_{self.graphs_count} = {value}\n"
        self.labels += f"plt.plot(param_{self.graphs_count}, label=\"{label}\")\n"
        self.graphs_count += 1

    def __str__(self):
        return self.values + self.middle_fix + self.labels + self.post_fix
