from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv
from codelists import *
from datetime import date, timedelta

'''
Guidance issued 2021-04-12, with inclusion criteria of symptom onset within 14 days, therefore index date of 2021-03-29
'''

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    index_date="2021-03-29",

    population=patients.satisfying(
        """
            NOT has_died
            AND registered
            AND (
                age_band = "65_plus" 
                OR (
                    age_band = "50_65" 
                    AND (
                        primis_shield 
                        OR 
                        primis_nonshield
                        )
                    )
                ) 
            AND (
                sex = "M" 
                OR 
                sex = "F"
                )
            AND NOT covid_admission
            AND NOT covid_emergency_admission
            AND NOT has_previous_steroid_prescription
            AND NOT primary_covid_hospital_admission
            AND first_positive_test_type != "LFT_Only"
        """,

        has_died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
        ),

        has_previous_steroid_prescription=patients.with_these_medications(
            inhaled_or_systemic_corticosteroids,
            between=[
                "index_date - 90 days",
                "index_date",
            ],
            returning="binary_flag",
            return_expectations={"incidence": 0.5}
        ),

        registered=patients.registered_as_of("index_date"),
    ),

    first_positive_test_date=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        on_or_after="index_date",
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD",
        return_expectations={
            "date": {"earliest": "index_date"},
            "rate": "exponential_increase"
        },
    ),

    first_positive_test_type=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        on_or_after="index_date",
        find_first_match_in_period=True,
        returning="case_category",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "LFT_Only": 0,
                    "PCR_Only": 0.1,
                    "LFT_WithPCR": 0.05,
                    "": 0.85
                }
            }
        },
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    age_band=patients.categorised_as(
        {
            "65_plus": "age >= 65",
            "50_65": "age >=50 AND age <65",
            "lt_50": "DEFAULT"
        },
        age=patients.age_as_of("first_positive_test_date - 90 days"),
        return_expectations={
            "category": {
                "ratios": {
                    "lt_50": 0.85,
                    "50_65": 0.05,
                    "65_plus": 0.1,
                }
            }
        }
    ),
    region=patients.registered_practice_as_of(
        "index_date",
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

    budesonide_prescription=patients.with_these_medications(
        budesonide_inhalers,
        between=["first_positive_test_date",
                 "first_positive_test_date + 14 days"],
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "normal", "mean": 1, "stddev": 1}, "incidence": 0.5}
    ),

    with_consultation=patients.with_gp_consultations(
        between=["first_positive_test_date - 7 days",
                 "first_positive_test_date + 7 days"],
        returning='binary_flag',
        return_expectations={"incidence": 0.5}
    ),
    primary_covid_hospital_admission=patients.admitted_to_hospital(
        returning="binary_flag",
        with_these_primary_diagnoses=covid_codelist,
        on_or_after="first_positive_test_date",
        find_last_match_in_period=True,
        return_expectations={
            "incidence": 0.3,
        },
    ),

    covid_admission=patients.admitted_to_hospital(
        returning="binary_flag",
        with_these_diagnoses=covid_codelist,
        on_or_after="first_positive_test_date",
        return_expectations={"incidence": 0.05}),

    covid_emergency_admission=patients.attended_emergency_care(
        returning="binary_flag",
        with_these_diagnoses=covid_codes_ae,
        on_or_after="first_positive_test_date",
        return_expectations={"incidence": 0.05}),

    primis_shield=patients.with_these_clinical_events(
        primis_shield,
        returning='binary_flag',
        on_or_after='index_date - 1 year',
        return_expectations={"incidence": 0.1}
    ),

    primis_nonshield=patients.with_these_clinical_events(
        primis_nonshield,
        returning='binary_flag',
        on_or_after='index_date - 1 year',
        return_expectations={"incidence": 0.1}
    )
)
