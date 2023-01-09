import pandas as pd
import statistics as stats

df = pd.read_csv('20211014_15:10:21_all_exp_results_clean.csv')

for key, grp in df.groupby(['exp_command', 'order_type']):
    print(key)
    m = grp['result'].values
    x = stats.mean(m)
    print(x)
    print()
