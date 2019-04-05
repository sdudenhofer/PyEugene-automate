import sqlite3
import pandas as pd

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()
print(c)
query = '''select t01.artist, t02.content, t03.genre, t04.label, t05.score, t06.year
from artists t01 left outer join content t02 on t01.reviewid = t02.reviewid
left OUTER JOIN genres t03 on t02.reviewid = t03.reviewid
LEFT OUTER JOIN labels t04 on t03.reviewid = t04.reviewid
left OUTER join reviews t05 on t04.reviewid = t05.reviewid
left outer JOIN years t06 on t05.reviewid = t06.reviewid
order by t06.year ASC;'''

cursor = conn.execute(query)
array = []

for row in cursor:
    array.append(row)

df = pd.DataFrame(array)
save_file = input("Where should we save this file?")
df.to_excel(save_file, index=False