from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv
from codelists import covid_codelist,flu_comorb,corticosteroid_contraindications
from datetime import date, timedelta

'''
Guidance issued 2021-04-12, with inclusion criteria of symptom onset within 14 days, therefore index date of 2021-03-29
'''

#past 3 months for current prescription

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
        # AND NOT corticosteroid_ADR

        """
            NOT has_died
            AND
            registered
            AND
            (age >= 65 OR ((age >=55 AND age <65) AND has_comorbidities)) 
            AND
            (sex = "M" OR sex = "F")
            AND 
            (first_positive_test_type = "PCR_Only" OR first_positive_test_type = "LFT_WithPCR")
            AND
            NOT corticosteroid_contraindicated
        """,

        has_died=patients.died_from_any_cause(
            on_or_before = "index_date",
            returning = "binary_flag",
        ),

        corticosteroid_contraindicated = patients.with_these_clinical_events(
            corticosteroid_contraindications, 
            returning='binary_flag', 
            # return_expectations={
            #         "incidence": 0.01
            #     }
        ),

        registered = patients.satisfying(
        "registered_at_start",
        registered_at_start = patients.registered_as_of("index_date"),
        ),
        
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
                    "PCR_Only":0.8, 
                    "LFT_WithPCR":0.2
                }
            }
        },
    ),

    

    has_comorbidities = patients.with_these_clinical_events(
        flu_comorb, 
        on_or_after=indexoffset(730), 
        returning='binary_flag', 
        return_expectations={
                "incidence": 0.05
            }
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
        "first_positive_test_date - 3 months",
        return_expectations = {
        "rate": "universal",
        "int": {"distribution": "population_ages"},
        "incidence" : 0.001
        },
    ),
  
    covid_admission_date=patients.admitted_to_hospital(
        returning= "date_admitted",
        with_these_diagnoses=covid_codelist,
        on_or_after=ix_dt,
        find_first_match_in_period=True,
        date_format="YYYY-MM-DD",
        return_expectations={"date": {"earliest": ix_dt}}),

    covid_emergency_admission_date=patients.attended_emergency_care(
        returning= "date_arrived",
        with_these_diagnoses=covid_codelist,
        on_or_after=ix_dt,
        find_first_match_in_period=True,
        date_format="YYYY-MM-DD",
        return_expectations={"date": {"earliest": ix_dt}}),

    
)
