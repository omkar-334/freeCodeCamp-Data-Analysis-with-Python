import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
# Add 'overweight' column
overweight = []
x = 0
for i in range(0, len(df)):
  x = df["weight"][i] / (((df["height"][i]) / 100)**2)
  if (x > 25):
    overweight.append(1)
  else:
    overweight.append(0)
  x = 0
df["overweight"] = overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'].replace(1, 0, inplace=True)
df['cholesterol'].replace([2, 3], value=1, inplace=True)
df['gluc'].replace(1, 0, inplace=True)
df['gluc'].replace([2, 3], value=1, inplace=True)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,
                   id_vars='cardio',
                   value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight',
                     'smoke'
                   ])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

  # Draw the catplot with 'sns.catplot()'

  # Get the figure for the output
  fig = sb.catplot(data=df_cat,
                   kind='count',
                   hue='value',
                   x="variable",
                   col="cardio").set(ylabel='total').fig

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi'])
               & (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(corr)

  # Set up the matplotlib figure
  fig, ax = plt.subplots()

  # Draw the heatmap with 'sns.heatmap()'
  ax = sb.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
