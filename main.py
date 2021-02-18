import pandas as pd

url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm#ief781ab58e4f4fcaa872ddbd30da40e1_91"

# Now, let's create a pandas DataFrame object :-

df = pd.read_html(url)


print()

print(len(df))
