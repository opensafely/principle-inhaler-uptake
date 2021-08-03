from os import system
from cohortextractor import codelist, codelist_from_csv

covid_codelist = codelist_from_csv(
    "codelists/opensafely-covid-identification.csv",
    system="icd10",
    column="icd10_code",
)
budesonide_inhalers = codelist_from_csv(
    "codelists/opensafely-budesonide-inhalers-used-in-principle-trial-cemcmo2021011.csv",
    system="snomed",
    column='dmd_id'
)

inhaled_or_systemic_corticosteroids = codelist_from_csv(
    "codelists/opensafely-inhaled-or-systemic-corticosteroids.csv",
    system="snomed",
    column='dmd_id'
)
primis_shield = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-shield.csv",
    system="snomed",
    column="code"
)
primis_nonshield = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-nonshield.csv",
    system="snomed",
    column="code"
)
#from https://github.com/opensafely/vaccine-effectiveness-hospital-admissions-validation/
covid_codes_ae = codelist_from_csv(
    "analysis/covid_codes_ae.csv",
    system="snomed",
    column="snomed_id",
)