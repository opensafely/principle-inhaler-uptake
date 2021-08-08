import pandas as pd

## low count suppression function
def suppress(df_to_suppress,columns,n=10):
    for c in columns:
        if not c in df_to_suppress.columns:
            raise ValueError(f'column {c} not in dataframe')

    df = df_to_suppress
    for c in df.columns[df.columns.isin(columns)]:
        df[[c]] = df[[c]].astype(str)
        df[[c]] = df[c].apply(lambda x: '<10' if (int(x)>0 and int(x)<n ) else x)
    return df


df = pd.read_csv('../output/input.csv')

#exclude LFT tests, include unknowns
df.first_positive_test_type= df.first_positive_test_type.fillna('Unknown')
df = df[df.first_positive_test_type!="LFT"]

#add cohort label [over 65s, over 50s with sheilding flag, over 50s with non-sheilding flag]
df['cohort'] = df.apply(lambda x: x.age_band if x.age_band == '65_plus' else str(x.age_band) + ('H' if x.primis_shield==1 else 'L'),axis=1)


df_test_counts = df.groupby('first_positive_test_type').count()['patient_id'].reset_index().rename(columns={'patient_id':'Patient count',"first_positive_test_type":"Type of first recorded positive test"})
supressed_test_type_counts = suppress(df_test_counts,['Patient count'])

supressed_test_type_counts.style.hide_index()