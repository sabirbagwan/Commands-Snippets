import pandas as pd

pd.options.plotting.backend = "hvplot"
pd.options.plotting.backend = "matplotlib"
pd.set_option('display.min_rows', 20)
pd.set_option('display.min_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.0f}')
pd.set_option('display.float_format',  f'${:,.2f}')
pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
pd.set_option('display.float_format', lambda x: f'{x:.3f}')
pd.set_option('display.precision', 2)
pd.reset_option('display.max_rows')
pd.reset_option('all')
