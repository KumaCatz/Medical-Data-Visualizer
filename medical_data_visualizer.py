import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='feature', value_name='value')

    # 6
    df_cat = df_cat.groupby(['cardio', 'feature', 'value']).size().reset_index(name='counts')
    df_cat = df_cat.rename(columns={'feature': 'variable'})

    # 7
    df_cat = df_cat.loc[df_cat.index.repeat(df_cat['counts'])].drop(columns='counts')

    cat_plot = sns.catplot(
        data=df_cat,
        x='variable',
        hue='value',
        col='cardio',
        kind='count',
        )

    # # 8
    fig = cat_plot.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[~(
        (df['ap_lo'] > df['ap_hi']) |
        (df['height'] < df['height'].quantile(0.025)) |
        (df['height'] > df['height'].quantile(0.975)) |
        (df['weight'] < df['weight'].quantile(0.025)) |
        (df['weight'] > df['weight'].quantile(0.975))
        )]
    df_heat = df_heat.rename(columns={'sex': 'gender'})

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.tril(np.ones_like(corr, dtype=bool), k=-1)
    corr_upper = corr.where(mask)

    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(
        corr_upper,
        annot=True,
        fmt='.1f',
        linewidths=1,
        linecolor='white',
        cmap=sns.diverging_palette(240, 20, s=100, l=50, as_cmap=True),
        center=0,
        cbar_kws={"shrink": 0.6}
        )

    # 16
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()
