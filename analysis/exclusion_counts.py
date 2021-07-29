import pandas as pd
import os
df = pd.read_csv('output/input_exclusioncounts.csv')

out_dict = {}

out_dict['totalrows'] = len(df.index)

df.covid_admission = df.covid_admission.fillna(0)
for r in df.groupby('covid_admission')['patient_id'].count().reset_index().iterrows():
    out_dict[f'initial_covid_emergency_admission__{r[1].covid_admission}'] = r[1].patient_id

df.primary_covid_hospital_admission = df.primary_covid_hospital_admission.fillna(
    0)
for r in df.groupby('primary_covid_hospital_admission')['patient_id'].count().reset_index().iterrows():
    out_dict[f'initial_primary_covid_hospital_admission__{r[1].primary_covid_hospital_admission}'] = r[1].patient_id

df.covid_emergency_admission = df.covid_emergency_admission.fillna(0)
for r in df.groupby('covid_emergency_admission')['patient_id'].count().reset_index().iterrows():
    out_dict[f'initial_covid_emergency_admission__{r[1].covid_emergency_admission}'] = r[1].patient_id

df.has_previous_steroid_prescription = df.has_previous_steroid_prescription.fillna(
    0)
out_dict['initial_NOT_has_previous_steroid_prescription'] = len(
    df[df.has_previous_steroid_prescription == 0].index)

df = df[df.has_died == 0]
out_dict['has_not_died'] = len(df.index)

df = df[df.registered == 1]
out_dict['registered'] = len(df.index)

out_dict['over_65'] = len(df[df.age >= 65].index)
out_dict['over_55_low_covid_risk'] = len(df[((df.age < 65) & (df.age >= 55)) & (
    df.primis_shield == 0) & (df.primis_nonshield == 1)].index)
out_dict['over_55_high_covid_risk'] = len(
    df[((df.age < 65) & (df.age >= 55)) & (df.primis_shield == 1)].index)

df.drop((df[((df.age < 65) & (df.age >= 55)) & (df.primis_shield == 1)].index))
df.drop(df[df.age < 55].index)

df = df[(df.sex == 'M') | (df.sex == 'F')]
out_dict['sex_M_or_F'] = len(df.index)


df = df[df.first_positive_test_date.notna()]
out_dict['first_positive_test_date_notna'] = len(df.index)

df.first_positive_test_type = df.first_positive_test_type.fillna('NA')
for r in df.groupby('first_positive_test_type')['patient_id'].count().reset_index().iterrows():
    out_dict[f'first_positive_test_type__{r[1].first_positive_test_type}'] = r[1].patient_id

df = df[df.first_positive_test_type != "LFT_Only"]

out_dict['PCR_+ve_over_65'] = len(df[df.age >= 65].index)
out_dict['PCR_+ve_over_55_low_covid_risk'] = len(df[((df.age < 65) & (
    df.age >= 55)) & (df.primis_shield == 0) & (df.primis_nonshield == 1)].index)
out_dict['PCR_+ve_over_55_high_covid_risk'] = len(
    df[((df.age < 65) & (df.age >= 55)) & (df.primis_shield == 1)].index)

df.has_previous_steroid_prescription = df.has_previous_steroid_prescription.fillna(
    0)
df = df[df.has_previous_steroid_prescription == 0]
out_dict['NOT_has_previous_steroid_prescription'] = len(df.index)

df.covid_admission = df.covid_admission.fillna(0)
df.covid_emergency_admission = df.covid_emergency_admission.fillna(0)

df[(df.covid_admission == 0) & (df.primary_covid_hospital_admission == 0)
    & (df.covid_emergency_admission == 0)]
out_dict['NOT_hospitalised'] = len(df.index)

out_dict['with_consultation'] = len(df[df.with_consultation == 1].index)

for r in df.groupby('budesonide_prescription')['patient_id'].count().reset_index().iterrows():
    out_dict[f'has_budesonide_prescription__{r[1].budesonide_prescription}'] = r[1].patient_id

with open('output/exclusioncounts.txt', 'w+') as wf:
    wf.writelines(
        [f'{k}:{v if v>10 else "<10"}\n' for k, v in out_dict.items()])
