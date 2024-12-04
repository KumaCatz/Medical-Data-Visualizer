import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', index_col=0)

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

draw_cat_plot()
# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
