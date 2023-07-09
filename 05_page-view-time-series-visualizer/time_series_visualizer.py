import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv",
                 parse_dates=['date'],
                 index_col="date")
df = df[(df["value"] >= df["value"].quantile(.025))
        & (df["value"] <= df["value"].quantile(.975))]


def draw_line_plot():
  # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax = sns.lineplot(data = df, legend="brief")
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel = "Date",ylabel = "Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


months = [
  'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
  'September', 'October', 'November', 'December'
]


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["year"] = df.index.year.values
  df_bar["month"] = df.index.month_name()
  # Draw bar plot
  fig, ax = plt.subplots(figsize=(15, 5))
  ax = sns.barplot(x="year",
                   hue="month",
                   y="value",
                   data=df_bar,
                   hue_order=months,
                   errorbar=None)
  ax.set(xlabel="Years", ylabel="Average Page Views")
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  df_box['monthnumber'] = df.index.month
  df_box = df_box.sort_values('monthnumber')
  fig, ax = plt.subplots(1, 2, figsize=(16, 6))
  sns.boxplot(y="value", x="year", data=df_box, ax=ax[0])
  ax[0].set(xlabel="Year",
            ylabel="Page Views",
            title="Year-wise Box Plot (Trend)")
  sns.boxplot(y="value", x="month", data=df_box, ax=ax[1])
  ax[1].set(xlabel="Month",
            ylabel="Page Views",
            title="Month-wise Box Plot (Seasonality)")
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
