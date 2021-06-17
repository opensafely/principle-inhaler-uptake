from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv
from codelists import *

'''
Guidance issued 2021-04-12, with inclusion criteria of symptom onset within 14 days, therefore index date of 2021-03-29
'''

#past 3 months for current prescription

ix_dt = "2021-03-29"
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    index_date = ix_dt,

    population=patients.satisfying(
       #'''age>=65''' 
        # '''(age >= 65 OR ((age >=55 AND age <65)) AND has_comorbidities)) 
        # AND has_covid_pcr_positive
        # AND had_covid_symtoms
        # AND NOT corticosteroid_ADR
        # AND NOT has_covid_admission
        # AND NOT has_covid_emergency_admission'''

        """
            NOT has_died
            AND
            registered
            AND
            age >=55
            AND
            (sex = "M" OR sex = "F")
        """,

        has_died=patients.died_from_any_cause(
            on_or_before = "index_date",
            returning = "binary_flag",
        ),

        registered = patients.satisfying(
        "registered_at_start",
        registered_at_start = patients.registered_as_of("index_date"),
        ),
    ),
    
    sex = patients.sex(
        return_expectations = {
        "rate": "universal",
        "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
    
    imd = patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 """,
        },
        index_of_multiple_deprivation = patients.address_as_of(
            "index_date",
            returning = "index_of_multiple_deprivation",
            round_to_nearest = 100,
            ),
        return_expectations = {
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.01,
                    "1": 0.20,
                    "2": 0.20,
                    "3": 0.20,
                    "4": 0.20,
                    "5": 0.19
                }
            },
        },
    ),
  
    age = patients.age_as_of(
        "index_date",
        return_expectations = {
        "rate": "universal",
        "int": {"distribution": "population_ages"},
        "incidence" : 0.001
        },
    ),
  
    first_positive_test_date=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        on_or_after=ix_dt,
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD",
        return_expectations={
            "date": {"earliest" : ix_dt},
            "rate" : "exponential_increase"
        },
    ),
    
    first_positive_test_type=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        on_or_after=ix_dt,
        find_first_match_in_period=True,
        returning="case_category",
        return_expectations={
            "rate":"universal",
            "category": {
                "ratios": {
                    "LFT_Only":0.3, 
                    "PCR_Only":0.4, 
                    "LFT_WithPCR":0.3
                }
            }
        },
    ),

    # #stub
    # has_comorbidities = 1,
    # has_covid_pcr_positive = 1,
    # had_covid_symptoms = 1,

    # covid_admission_date=patients.admitted_to_hospital(
    # returning= "date_admitted",
    # with_these_diagnoses=covid_codelist,
    # on_or_after=ix_dt,
    # find_first_match_in_period=True,
    # date_format="YYYY-MM-DD",
    # return_expectations={"date": {"earliest": ix_dt}},

    # covid_emergency_admission_date=patients.attended_emergency_care(
    # returning= "date_admitted",
    # with_these_diagnoses=covid_codelist,
    # on_or_after=ix_dt,
    # find_first_match_in_period=True,
    # date_format="YYYY-MM-DD",
    # return_expectations={"date": {"earliest": ix_dt}},

    # # has_positive_covid_pcr = patients.with_test_result_in_sgss(

    # # )


    # first_positive_test_date=patients.with_test_result_in_sgss(
    # pathogen="SARS-CoV-2",
    # test_result="positive",
    # on_or_after=ix_dt,
    # find_first_match_in_period=True,
    # returning="date",
    # date_format="YYYY-MM-DD",
    # return_expectations={
    #     "date": {"earliest" : ix_dt},
    #     "rate" : "exponential_increase"
    # },
    #),
)
