import pandas as pd

file = input("Enter File Name/Location:")

data = pd.read_csv(file)
output = input("Enter Excel Filename:")
data.to_excel(output, index=False)
