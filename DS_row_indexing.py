df.loc[df['column_name'] == some_value]
df.loc[df['column_name'].isin(some_values)]
df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
df['column_name'] >= A & df['column_name'] <= B
df['column_name'] >= (A & df['column_name']) <= B
df.loc[df['column_name'] != some_value]
df.loc[~df['column_name'].isin(some_values)]
df.loc[df['B'].isin(['one','three'])]
df.loc[df.index.isin(['one','two'])]

df.query('foo == 222 | bar == 444')

exclude = ('red', 'orange')
df.query('color not in @exclude')

df.query('`Sender email`.str.endswith("@shop.com")')
domain = 'shop.com'
df.query('`Sender email`.str.endswith(@domain)')

df.loc[df['column_name'] == some_value, [col_name1, col_name2]]
f.query('column_name == some_value')[[col_name1, col_name2]]
