"""Recreate the README benchmark figure from saved scores; no models are rerun."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
a = pd.read_csv(ROOT / 'results/mae/test_scores.csv')
b = pd.read_csv(ROOT / 'results/model-comparison/test_scores.csv')
fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
colors = ['#2364aa', '#25856c']
for i, (scores, label, color) in enumerate(zip([a, b], ['Initial MAE search', 'Expanded model search'], colors)):
    axes[0].scatter([i]*5, scores.mae, color=color, alpha=.65, s=45)
    axes[0].scatter(i, scores.mae.mean(), marker='_', linewidth=3, s=250, color=color)
    axes[0].text(i, scores.mae.max()+.009, f'{scores.mae.mean():.4f} eV', ha='center', color=color, weight='bold')
    axes[1].plot(scores.fold+1, scores.mae, marker='o', label=label, color=color)
axes[0].set(xticks=[0,1], xticklabels=['Initial MAE search','Expanded model search'], xlim=(-.5,1.5), title='Five-fold mean and individual test scores')
axes[1].set(xticks=range(1,6), xlabel='Official outer fold', title='Paired test scores on the same outer splits')
axes[1].legend(frameon=False)
for ax in axes:
    ax.set_ylabel('Held-out test MAE (eV)')
    ax.set_ylim(.34,.48)
    ax.grid(axis='y', alpha=.2)
    ax.spines[['top','right']].set_visible(False)
fig.suptitle('Experimental bandgap prediction from composition', fontsize=15, weight='bold')
fig.text(.5,.015,'Lower is better. Each test prediction excludes its own outer fold from training and tuning.\nRepeated benchmark development is documented; results are not an official leaderboard submission.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.08,1,.93])
fig.savefig(ROOT/'results/model-comparison/benchmark-progress.png',dpi=180)
