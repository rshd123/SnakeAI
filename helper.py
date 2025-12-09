import matplotlib.pyplot as plt

plt.ion()

def plot(scores, mean_scores):
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, color='blue', linewidth=2, label='Score')
    plt.plot(mean_scores, color='red', linewidth=2, label='Mean Score')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.show(block=False)
    plt.pause(0.1)
