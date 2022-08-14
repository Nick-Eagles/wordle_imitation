import pandas as pd

out_path = 'cleaned_word_list.csv'

#   Manually determined cutoff, below which I have trouble recognizing many
#   words
FREQ_CUTOFF = 200

WORD_LEN = 5

#   Read in first list
a = pd.read_csv('lemmas_60k.txt', skiprows = 7, sep = '\t')
a['lemma'] = a['lemma'].astype(str)

#   Grab valid words of the correct length
good_indices = pd.Series(
    ['-' not in x and len(x) == WORD_LEN for x in a['lemma']]
)
a = a[good_indices]

#   Read in second list
b = pd.read_excel('wordFrequency.xlsx', sheet_name = 1)
b['lemma'] = b['lemma'].astype(str)

#   Grab valid words of the correct length
good_indices = pd.Series(
    ['-' not in x and len(x) == WORD_LEN for x in b['lemma']]
)
b = b[good_indices]

#   Now combine the lists but make sure words are unique
a = a[~ a['lemma'].isin(b['lemma'])]
assert a.shape[0] > 0, a.shape
word_df = pd.concat((a, b))

#   Filter out uncommon words and write to CSV (ordered by decreasing
#   frequency)
word_df = word_df[word_df['freq'] > FREQ_CUTOFF]
word_df.sort_values('freq', ascending = False, inplace = True)
word_df.to_csv(out_path, index = False, columns = ('lemma', 'freq'))
