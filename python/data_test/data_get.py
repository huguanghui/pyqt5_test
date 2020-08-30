import warnings
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

warnings.filterwarnings('ignore')

city_df = pd.read_excel('NationalJob_da.xlsx')['city']
barh_series = city_df.value_counts()[:12].sort_values(ascending=True)
barh_series.plot.barh(grid=True, alpha=0.8, figsize=(12,7))
plt.xticks([])
plt.title('图2-1 全国数据分析岗位招聘条形图')