import numpy as np
import pandas as pd

# for i in range(0, 100, 10):
#     print(i)

print(np.round((0+90)/10 + 1))

page_info = []

# 创建xlxs
data = {'one':[1, 2, 3, 4, 5],
        'two':[2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
print(df)
df = df.set_index('one')
print(df)
df.to_excel(r'C:\Users\Administrator\Desktop\outpu.xlsx')

# 写

# 读