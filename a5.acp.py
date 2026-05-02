import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

sns.set_theme(style="whitegrid")

sns.jointplot(data=df, x="total_bill", y="tip", hue="sex", kind="kde")
plt.show()

sns.pairplot(df, hue="smoker", palette="husl", diag_kind="hist")
plt.show()

corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()

g = sns.FacetGrid(df, col="time", row="sex", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", hue="day")
g.add_legend()
plt.show()

sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True, inner="quart")
plt.show()