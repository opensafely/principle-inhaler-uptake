import pandas as pd
import os

#     """
#         NOT has_died
#         AND
#         registered
#         AND
#         (age >= 65 OR ((age >=55 AND age <65) AND has_comorbidities))
#         AND
#         (sex = "M" OR sex = "F")
#         AND
#         (first_positive_test_type = "PCR_Only" OR first_positive_test_type = "LFT_WithPCR")

#         AND
#         NOT has_previous_steroid_prescription
#     """,

df = pd.read_csv('output/input_exclusioncounts.csv')

out_dict = {}

out_dict['totalrows'] = len(df.index)
df = df[df.has_died == 0]
out_dict['has_not_died'] = len(df.index)

df = df[df.registered == 1]
out_dict['registered'] = len(df.index)

out_dict['over_65'] = len(df[df.age >= 65].index)
# out_dict['over_55_comorbidities'] = len(
#     df[((df.age < 65) & (df.age >= 55)) & (df.has_comorbidities == 1)].index)
# df = df[(df.age >= 65) | (((df.age < 65) & (df.age >= 55))
#                           & (df.has_comorbidities == 1))]
out_dict['over_55_no_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55))   & (df.primis_shield == 0)& (df.primis_nonshield == 0)].index)
out_dict['over_55_low_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55))  & (df.primis_shield == 0)& (df.primis_nonshield == 1)].index)
out_dict['over_55_high_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55)) & (df.primis_shield == 1)].index)

df = df[(df.sex == 'M') | (df.sex == 'F')]
out_dict['sex_M_or_F'] = len(df.index)


df = df[df.first_positive_test_date.notna()]
out_dict['first_positive_test_date_notna'] = len(df.index)

df.first_positive_test_type=df.first_positive_test_type.fillna('NA')
for r in df.groupby('first_positive_test_type')['patient_id'].count().reset_index().iterrows():
    out_dict[f'first_positive_test_type__{r[1].first_positive_test_type}'] = r[1].patient_id

out_dict['+ve_over_65'] = len(df[df.age >= 65].index)
out_dict['+ve_over_55_no_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55))   & (df.primis_shield == 0)& (df.primis_nonshield == 0)].index)
out_dict['+ve_over_55_low_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55))  & (df.primis_shield == 0)& (df.primis_nonshield == 1)].index)
out_dict['+ve_over_55_high_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55)) & (df.primis_shield == 1)].index)

df = df[df.has_previous_steroid_prescription==0]
out_dict['NOT_has_previous_steroid_prescription'] = len(df.index)


df[(df.covid_admission == 0) & (df.covid_emergency_admission == 0)]
out_dict['NOT_hospitalised'] = len(df.index)

out_dict['with_consultation'] = len(df[df.with_consultation == 1].index)



for r in df.groupby('budesonide_prescription')['patient_id'].count().reset_index().iterrows():
    out_dict[f'has_budesonide_prescription__{r[1].budesonide_prescription}'] = r[1].patient_id

with open('output/exclusioncounts.txt', 'w+') as wf:
    wf.writelines([f'{k}:{v if v>10 else "<10"}\n' for k,v in out_dict.items()])
