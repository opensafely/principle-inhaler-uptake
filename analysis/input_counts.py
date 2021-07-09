import pandas as pd
import os

#do breakdown counts of exclusions.

df = pd.read_csv('output/input.csv')

out_dict= {}

out_dict['totalrows'] = len(df.index)
out_dict['first_positive_test_date_notna'] = len(df.first_positive_test_date.notna())
out_dict['with_consultation'] = len(df[df.with_consultation==1].index)
out_dict['hospitalised'] = len(df[(df.covid_admission==0)&(df.covid_emergency_admission==0)].index)

for r in df.groupby('budesonide_prescription')['patient_id'].count().reset_index().iterrows():
    out_dict[f'has_budesonide_prescription__{r[1].budesonide_prescription}'] = r[1].patient_id

with open('output/inputcounts.txt','w+') as wf:
    wf.writelines([f'{k}:{v}\n' for k,v in out_dict.items()])