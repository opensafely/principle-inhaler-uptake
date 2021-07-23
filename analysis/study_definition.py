from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv
from codelists import *
from datetime import date, timedelta

'''
Guidance issued 2021-04-12, with inclusion criteria of symptom onset within 14 days, therefore index date of 2021-03-29
'''

#todo: 

ix_dt = "2021-03-29"

def indexoffset(ndays):
    return (date.fromisoformat(ix_dt) + timedelta(days = ndays)).strftime('%Y-%m-%d')

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    index_date = ix_dt,

    population=patients.satisfying(
        
        # AND had_covid_symtoms

        """
            NOT has_died
            AND
            registered
            AND
            (age_band = "65_plus" OR (age_band = "55_65" AND (primis_shield OR primis_nonshield))) 
            AND
            (sex = "M" OR sex = "F")
            AND 
            (first_positive_test_type = "PCR_Only" OR first_positive_test_type = "LFT_WithPCR" OR first_positive_test_type ="")
           
            AND
            NOT has_previous_steroid_prescription
        """,

        has_died=patients.died_from_any_cause(
            on_or_before = "index_date",
            returning = "binary_flag",
        ),

        has_previous_steroid_prescription = patients.with_these_medications(
            inhaled_or_systemic_corticosteroids,
            on_or_before = "index_date - 3 months",
            returning = "binary_flag",
            return_expectations = {"incidence": 0.5}
        ),
        
        registered = patients.registered_as_of("index_date"),
    ),
    
   

# would be nice to use "all tests" as this may exlude pts with initial +ve LFT followed by PCR
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
                    "LFT_Only":0, 
                    "PCR_Only":0.1, 
                    "LFT_WithPCR":0.05,
                    "":0.85
                }
            }
        },
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
    age_band = patients.categorised_as(
        {
            "65_plus": "age >= 65",
            "55_65": "age >=55 AND age <65",
            "lt_55": "DEFAULT"
        },
        age = patients.age_as_of("first_positive_test_date - 3 months"),
        return_expectations={
            "category":{
                "ratios": {
                    "lt_55":0.85,
                    "55_65":0.05,
                    "65_plus":0.1,
                    }
                }
        }
    ),
    region = patients.registered_practice_as_of(
        ix_dt,
        returning='nuts1_region_name',
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        },
    ),
    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        return_expectations={
            "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
            "incidence": 0.75,
        }
    ),
    ethnicity_16=patients.with_these_clinical_events(
        ethnicity_codes_16,
        returning="category",
        find_last_match_in_period=True,
        return_expectations={
            "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
            "incidence": 0.75,
        }
    ),

    budesonide_prescription = patients.with_these_medications(
            budeonside_inhalers,
            between = ["first_positive_test_date","first_positive_test_date + 14 days"],
            returning = "number_of_matches_in_period",
            return_expectations = {"int" : {"distribution": "normal", "mean": 1, "stddev": 1}, "incidence" : 0.5}
    ),

    with_consultation = patients.with_gp_consultations(
        between=["first_positive_test_date - 7 days","first_positive_test_date + 7 days"],
        returning='binary_flag',
        return_expectations = {"incidence": 0.5}
    ),

    post_budesonide_hospitalisation = patients.satisfying(
        """
        budesonide_prescription>0 AND (
            covid_admission_date > budesonide_prescription_date OR 
            covid_emergency_admission_date > budesonide_prescription_date)
        """,
        budesonide_prescription_date = patients.with_these_medications(
            budeonside_inhalers,
            between = ["first_positive_test_date","first_positive_test_date + 14 days"],
            returning = "date"
        ),

        covid_admission_date=patients.admitted_to_hospital(
            returning= "date_admitted",
            with_these_diagnoses=covid_codelist,
            on_or_after="first_positive_test_date",
            find_first_match_in_period=True,
            date_format="YYYY-MM-DD"
        ),

        covid_emergency_admission_date=patients.attended_emergency_care(
            returning= "date_arrived",
            with_these_diagnoses=covid_codelist,
            on_or_after="first_positive_test_date",
            find_first_match_in_period=True,
            date_format="YYYY-MM-DD",
        ),
    ),
    
    covid_admission=patients.admitted_to_hospital(
        returning= "binary_flag",
        with_these_diagnoses=covid_codelist,
        on_or_after="first_positive_test_date",
        return_expectations = {"incidence": 0.05}),

    covid_emergency_admission=patients.attended_emergency_care(
        returning= "binary_flag",
        with_these_diagnoses=covid_codelist,
        on_or_after="first_positive_test_date",
        return_expectations = {"incidence": 0.05}),
    
    primis_shield = patients.with_these_clinical_events(
        primis_shield,
        returning='binary_flag',
        on_or_after='index_date - 1 year',
        return_expectations = {"incidence": 0.1}
    ),

    primis_nonshield = patients.with_these_clinical_events(
        primis_nonshield,
        returning='binary_flag',
        on_or_after='index_date - 1 year',
        return_expectations = {"incidence": 0.1}
    )
)
