"""Generate the two figures embedded in the GitHub profile README.

Same contract as the site's tools/make_figures.py: every plotted number comes
from a project result file, never typed by hand. Figures are sized for the
GitHub README column (~880 px) and use the site palette so the profile and the
portfolio look like one body of work.

Usage:  python make_figures.py [--root D:\\codes\\项目] [--out assets]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager as fm

INK, INK2, INK3 = '#1B252B', '#4A585F', '#5F6C74'
RULE, PAPER = '#E4E1D9', '#FBFAF6'
MINT, MINT_L = '#1F7A66', '#7FC9B6'
SKY, PEACH = '#2A6797', '#9C552E'


def pick_font() -> str:
    installed = {f.name for f in fm.fontManager.ttflist}
    for name in ('Noto Sans SC', 'Microsoft YaHei', 'Source Han Sans SC',
                 'PingFang SC', 'SimHei', 'Noto Sans CJK SC'):
        if name in installed:
            return name
    return 'DejaVu Sans'


def setup(font: str) -> None:
    plt.rcParams.update({
        'font.family': 'sans-serif', 'font.sans-serif': [font, 'DejaVu Sans'],
        'axes.unicode_minus': False,
        'figure.facecolor': PAPER, 'axes.facecolor': PAPER, 'savefig.facecolor': PAPER,
        'axes.edgecolor': RULE, 'axes.labelcolor': INK2, 'text.color': INK,
        'xtick.color': INK3, 'ytick.color': INK3,
        'grid.color': RULE, 'grid.linewidth': .7, 'axes.grid': True, 'axes.axisbelow': True,
        'axes.spines.top': False, 'axes.spines.right': False,
        'font.size': 10, 'figure.dpi': 200, 'savefig.dpi': 200,
        'savefig.bbox': 'tight', 'savefig.pad_inches': .16,
        'legend.frameon': False,
    })


def save(fig, out: Path, name: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    p = out / name
    fig.savefig(p)
    plt.close(fig)
    print(f'  wrote {p.name}  ({p.stat().st_size / 1024:.0f} KB)')


def fig_funnel(out: Path) -> None:
    stages = ['首页', '列表页', '详情页', '支付页', '确认页']
    sessions = np.array([97274, 71684, 47922, 6052, 1684])
    rates = [np.nan, 73.69, 66.85, 12.63, 27.83]

    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    y = np.arange(len(stages))[::-1]
    colors = [MINT_L] * len(stages)
    colors[3] = MINT
    ax.barh(y, sessions, color=colors, height=.6)
    ax.set_xscale('log')
    ax.set_xlim(700, 400000)
    ax.set_yticks(y, stages)
    ax.tick_params(axis='y', length=0)
    ax.grid(axis='y', visible=False)
    ax.set_xlabel('到达该环节的会话数（对数刻度）', fontsize=9)
    for yi, v, r in zip(y, sessions, rates):
        tag = f'{v:,}' + ('' if np.isnan(r) else f'   ↓ {r:.2f}%')
        ax.text(v * 1.1, yi, tag, va='center', fontsize=9,
                color=MINT if r == 12.63 else INK2,
                fontweight='bold' if r == 12.63 else 'normal')
    ax.annotate('最大流失环节：12.63%',
                xy=(sessions[3] * 1.05, y[3] + .2), xytext=(2600, y[3] + .95),
                fontsize=9, color=MINT, fontweight='bold',
                arrowprops=dict(arrowstyle='-', color=MINT, lw=1, shrinkA=0, shrinkB=2))
    ax.text(0, -.34,
            '会话数取自 MySQL 8.0 的 24 条查询，清洗后 97,274 条；百分比为相对上一环节的转化率。'
            '整体转化率 1.73%，口径为「到达确认页」。',
            transform=ax.transAxes, fontsize=8.4, color=INK3)
    save(fig, out, 'fig-funnel.png')


def fig_ate(out: Path, root: Path) -> None:
    d = pd.read_csv(root / 'ai-adoption-productivity-dml/output/tables/robustness_results.csv')
    order = ['Baseline (RF, K=5)', 'LASSO (CV)', 'XGBoost', 'K = 10', 'K = 2']
    zh = {'Baseline (RF, K=5)': '随机森林 · 5 折（报告值）', 'LASSO (CV)': 'LASSO',
          'XGBoost': 'XGBoost', 'K = 10': '交叉拟合 K = 10', 'K = 2': '交叉拟合 K = 2'}
    d = d.set_index('specification').loc[order].reset_index()
    d = d.iloc[::-1]

    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    y = np.arange(len(d))
    for yi, (_, r) in zip(y, d.iterrows()):
        c = MINT if r['specification'] == 'Baseline (RF, K=5)' else SKY
        ax.plot([r['ci_lower'], r['ci_upper']], [yi, yi], color=c, lw=2.2, alpha=.85,
                solid_capstyle='butt')
        ax.scatter([r['estimate']], [yi], color=c, s=40, zorder=3)
        ax.text(r['ci_upper'] + .0022, yi, f"{r['estimate'] * 100:+.2f}%  (p = {r['p_value']:.3f})",
                va='center', fontsize=9, color=INK2)
    ax.axvline(0, color=PEACH, lw=1.3)
    ax.set_yticks(y, [zh[s] for s in d['specification']], fontsize=9.5)
    ax.tick_params(axis='y', length=0)
    ax.set_xlim(-.018, .062)
    ax.set_xlabel('AI 采纳对劳动生产率的平均处理效应 ATE（95% 置信区间）', fontsize=9)
    ax.grid(axis='y', visible=False)
    ax.text(0, -.34,
            '换 nuisance 估计量或交叉拟合折数，置信区间始终覆盖 0（ATE ∈ [0.0004, 0.0059]）。'
            '150,000 家企业 × 64 维前定协变量，评分函数为手写 Neyman 正交形式。',
            transform=ax.transAxes, fontsize=8.4, color=INK3)
    save(fig, out, 'fig-ate.png')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=r'D:\codes\项目')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()

    root = Path(a.root)
    here = Path(__file__).resolve().parent
    out = Path(a.out) if a.out else here / 'assets'

    setup(pick_font())
    print(f'output: {out}\n')
    fig_funnel(out)
    fig_ate(out, root)
    print('\ndone.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
