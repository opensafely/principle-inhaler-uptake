from os import system
from cohortextractor import codelist, codelist_from_csv

covid_codelist = codelist_from_csv(
    "codelists/opensafely-covid-identification.csv",
    system="icd10",
    column="icd10_code",
)

flu_comorb = codelist_from_csv(
    "codelists/user-jon_massey-shielding-patient-list-spl-flu-risk-based-codes.csv",
    system="snomed",
    column='code'
)
budeonside_inhalers = codelist_from_csv(
    "codelists/opensafely-budesonide-inhalers-used-in-principle-trial-cemcmo2021011.csv",
    system="snomed",
    column='dmd_id'
)

inhaled_or_systemic_corticosteroids = codelist_from_csv(
    "codelists/opensafely-inhaled-or-systemic-corticosteroids.csv",
    system="snomed",
    column='dmd_id'
)

ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)
ethnicity_codes_16 = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_16",
)