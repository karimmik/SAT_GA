class Jupyter_Scatter:
    y_label = ''
    pre_fix = f"plt.figure(figsize=(12, 6))\n"

    post_fix = f"plt.ylabel('time in ms')\n" \
               f"plt.xlabel('instance')\n" \
               f"plt.legend()\n" \
               f"plt.show()\n"

    def __init__(self):
        self.scatters = ""

    def add_scatter(self, values, folder_name):
        self.scatters += f"plt.scatter({[x for x in range(0, len(values))]},{values}, label=\"{folder_name.split('/')[-1]}\")\n"

    def __str__(self):
        return self.pre_fix + self.scatters + self.post_fix
