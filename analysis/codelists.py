from os import system
from cohortextractor import codelist, codelist_from_csv

covid_codelist = codelist_from_csv(
    "codelists/opensafely-covid-identification-2020-06-03.csv",
    system="icd10",
    column="icd10_code",
)

flu_comorb = codelist_from_csv(
    "codelists/jon_massey-shielding-patient-list-spl-flu-risk-based-codes-7f5612ce.csv",
    system="snomed",
    column='code'
)

corticosteroid_contraindications = codelist_from_csv(
    "codelists/jon_massey-inhaled-corticosteroid-contraindications-05ea5490.csv",
    system="snomed",
    column='code'
)

inhaled_or_systemic_corticosteroids = codelist_from_csv(
    "codelists/jon_massey-inhaled-or-systemic-corticosteroids-1ef9c7c5-dmd.csv",
    system="snomed",
    column='dmd_id'
)

ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity-2020-04-27.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)
ethnicity_codes_16 = codelist_from_csv(
    "codelists/opensafely-ethnicity-2020-04-27.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_16",
)