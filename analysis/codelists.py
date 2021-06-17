from cohortextractor import codelist, codelist_from_csv

covid_codelist = codelist_from_csv(
    "codelists/opensafely-covid-identification-2020-06-03.csv",
    system="icd10",
    column="icd10_code",
)