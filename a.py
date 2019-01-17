import pandas as pd
df = pd.read_csv("yuki_1230s_field.csv", sep=',', names=('id', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'))
id = df['id']
id.to_csv("yuki_1230s_id.csv", index=False)