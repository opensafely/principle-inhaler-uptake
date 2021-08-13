# Measuring implementation of a national COVID-19 therapeutic alert following PRINCIPLE trial using OpenSAFELY

This is the code and configuration for measurement of the implementation of a [a national COVID-19 therapeutic alert](https://www.cas.mhra.gov.uk/ViewandAcknowledgment/ViewAlert.aspx?AlertID=103154) about the prescribing of inhaled budesonide for patients with COVID-19 in people at high risk of complications following pre-publication results2 from the [PRINCIPLE trial](https://doi.org/10.1016/S0140-6736(21)01744-X)

* The paper is [here]()
* Raw model outputs, including charts, crosstabs, etc, are in `released_outputs/`
* If you are interested in how we defined our variables, take a look at the [study definition](analysis/study_definition.py); this is written in `python`, but non-programmers should be able to understand what is going on there
* If you are interested in how we defined our code lists, look in the [codelists folder](./codelists/).
* Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)

# About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).
