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