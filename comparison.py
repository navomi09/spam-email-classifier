import matplotlib.pyplot as plt
import numpy as np

models = ['Naive Bayes (Our Model)', 'Bayesian Filter', 'Deep Learning', 'Rule-based Filter']
accuracy = [0.90, 0.92, 0.99, 0.85]
precision = [0.87, 0.90, 0.97, 0.80]
recall = [0.92, 0.94, 0.98, 0.85]
f1_score = [0.89, 0.92, 0.97, 0.82]

fig, ax = plt.subplots(figsize=(10, 6))


bar_width = 0.2


index = np.arange(len(models))

bar1 = ax.bar(index - 1.5 * bar_width, accuracy, bar_width, label='Accuracy', color='b')
bar2 = ax.bar(index - 0.5 * bar_width, precision, bar_width, label='Precision', color='r')
bar3 = ax.bar(index + 0.5 * bar_width, recall, bar_width, label='Recall', color='g')
bar4 = ax.bar(index + 1.5 * bar_width, f1_score, bar_width, label='F1-Score', color='y')


ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('Spam Filter Model Comparison')
ax.set_xticks(index)
ax.set_xticklabels(models)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
