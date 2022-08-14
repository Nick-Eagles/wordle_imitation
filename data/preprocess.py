import pandas as pd

out_path = 'cleaned_word_list.csv'

#   Read in first list and filter out words with special characters
a = pd.read_csv('lemmas_60k.txt', skiprows = 7, sep = '\t')
a['lemma'] = a['lemma'].astype(str)
a = a[pd.Series(['-' not in x and "'" not in x for x in a['lemma']])]

#   Read in second list and filter out words with special characters
b = pd.read_excel('wordFrequency.xlsx', sheet_name = 1)
b['lemma'] = b['lemma'].astype(str)
b = b[pd.Series(['-' not in x and "'" not in x for x in b['lemma']])]

#   Now combine the lists but make sure words are unique
a = a[~ a['lemma'].isin(b['lemma'])]
assert a.shape[0] > 0, a.shape
word_df = pd.concat((a, b))

#   Write to CSV (ordered by decreasing frequency)
print(f'{word_df.shape[0]} words written to cleaned list.')
word_df.sort_values('freq', ascending = False, inplace = True)
word_df.to_csv(out_path, index = False, columns = ('lemma', 'freq'))
