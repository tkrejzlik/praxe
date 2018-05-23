import matplotlib.pyplot as plt
lines = []


def opening(name):
    with open(name,"r") as f:

        for line in f:
            words = line.split()
            lines.append(words)
        del lines[0]
        del lines[0]
        del lines[-1]
        del lines[-1]
def draw_graph():
    for i in range(len(lines)):
        loc = int(lines[i][1])
        tested_loc = int(lines[i][2])
        plt.title(lines[i][0])
        plt.plot([1],[loc],'ro',label = "loc")
        plt.plot([1],[tested_loc],'bs',label = "tested_loc")
        plt.legend()
        plt.show()

opening("/home/tkrejzlik/Desktop/data/praxe-master/data/praxe-master/data/praxe-master/data/fabric8-analytics-worker.coverage.0.txt")

dict = {}
for i in range(len(lines)):
    dict.update({lines[i][0]:(lines[i][1],lines[i][2])})
draw_graph()