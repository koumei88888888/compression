import pandas as pd

df = pd.read_csv("corolla_fielder_10min_xor_dump.csv", sep=' ', names=('ID', 'Payload'))
df = df['ID']
df.to_csv("huffman_id.csv", index=False)