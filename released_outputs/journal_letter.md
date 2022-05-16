# Measuring implementation of a national COVID-19 therapeutic alert following PRINCIPLE trial using OpenSAFELY

The OpenSAFELY Collaborative: Jon Massey<sup>1</sup>, Brian MacKenna<sup>1</sup>, Richard Croker<sup>1</sup>, Alex J Walker<sup>1</sup>, Peter Inglesby<sup>1</sup>, Christopher T Rentsch<sup>2</sup>, Helen J Curtis<sup>1</sup>, Caroline E Morton<sup>1</sup>, Jessica Morley<sup>1</sup>, Amir Mehrkar<sup>1</sup>, Sebastian CJ Bacon<sup>1</sup>, George Hickman<sup>1</sup>, Christopher Bates<sup>3</sup>, David Evans<sup>1</sup>, Tom Ward<sup>1</sup> , Louis Fisher<sup>1 </sup>, Amelia CA Green<sup>1</sup>, Rebecca M Smith<sup>1</sup>, Jonathan Cockburn<sup>3</sup>, Colm Andrews<sup>1</sup> , Viyaasan Mahalingasivam<sup>2</sup>, Simon Davy<sup>1</sup>, Krishnan Bhaskaran<sup>2</sup>, Anna Schultze<sup>2</sup>, Ian J Douglas<sup>2</sup>, Stephen JW Evans<sup>2</sup>, Elizabeth J Williamson<sup>2</sup>, William J Hulme<sup>1</sup>, Helen I McDonald<sup>2</sup>, Laurie Tomlinson<sup>2</sup>, Rohini Mathur<sup>2</sup>, Rosalind M Eggo<sup>2</sup>, Kevin Wing<sup>2</sup>, Angel YS Wong<sup>2</sup>, John Tazare<sup>2</sup>,  John Parry<sup>3</sup>, Frank Hester<sup>3</sup>, Sam Harper<sup>3</sup>, Liam Smeeth<sup>2</sup>, Ben Goldacre<sup>1*</sup>

<sup>1</sup> The DataLab, Nuffield Department of Primary Care Health Sciences, University of Oxford, OX2 6GG


<sup>2</sup> London School of Hygiene and Tropical Medicine, Keppel Street, London WC1E 7HT


<sup>3</sup> TPP, TPP House, 129 Low Lane, Horsforth, Leeds, LS18 5PX

*Corresponding

A national NHS COVID-19 therapeutic alert was issued in April 2021 regarding use of inhaled budesonide for patients with COVID-19 and high risk of complications<sup><a href="https://www.zotero.org/google-docs/?8x3Zua">1</a></sup> following prepublication of results<sup><a href="https://www.zotero.org/google-docs/?t3UB2R">2</a></sup> from the PRINCIPLE trial. 

[guidance updated/revoked on …]

During COVID-19 our team has built OpenSAFELY, a secure open source platform executing code across NHS patients’ full electronic health records in situ in near-real-time. Using this platform, we find that implementation of the PRINCIPLE trial findings has been minimal. 

With NHS England approval, we analysed 24 million people’s electronic health records managed by TPP, a GP software provider, linked to death data provided by the Office of National Statistics, SARS-CoV-2 test data from Public Health England, and Admitted Patient Care and Emergency Care Data Set provided by NHS Digital. We identified eligible patients based on their age, positive SARS-CoV-2 PCR test, lack of COVID-19-related hospital admission, COVID-19 complication risk<sup><a href="https://www.zotero.org/google-docs/?sR9vvf">3</a></sup>, and lack of recent corticosteroid prescription. We then identified budesonide prescriptions within two weeks of positive SARS-CoV-2 test from the NHS alert until December 31st 2021. All code for the platform and analysis is shared under open licenses<sup><a href="https://www.zotero.org/google-docs/?9qy59H">4</a></sup>.

Of 134,062 eligible patients, only 498 (0.37%) received inhaled budesonide prescriptions issued by 2,516 practices (Table 1). There were striking geographic differences, with the South West region having 85% of prescriptions, and 82% of prescribing practices, but only 11% of the eligible population.

We also recognise some limitations. Our data, although large, may not be fully representative and does not include all data from settings such as “out of hours” clinics or COVID-19 treatment centres where different software may be used. However we have assessed open NHS dispensing data and there does not appear to be any substantial increase in budesonide prescription in these settings<sup><a href="https://www.zotero.org/google-docs/?d2ijW0">4</a></sup>.

Following final publication of PRINCIPLE<sup><a href="https://www.zotero.org/google-docs/?4iZtXt">5</a></sup>, we will now further monitor changes. More broadly, OpenSAFELY can now execute code securely across 58 million patients’ full electronic health records, and opens the possibility of monitoring implementation of critical new guidance and evidence in near-real-time using fine-grained data covering almost the entire population while preserving patients’ privacy. 

Table 1: _Counts of inhaled budesonide prescriptions issued to eligible patients within two weeks of positive PCR test for COVID-19_


<table>
  <tr>
   <td><strong>Cohort</strong>
   </td>
   <td><strong>Number of budesonide prescriptions in 2 weeks following positive test </strong>
   </td>
   <td><strong>Count of Patients </strong>
<p>
<em>(numbers &lt;10 suppressed)</em>
   </td>
  </tr>
  <tr>
   <td rowspan="5" >All
   </td>
   <td>0
   </td>
   <td>134,062
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>468
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>30
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td rowspan="5" >Aged 50-64 with COVID-19 Complication Risk
   </td>
   <td>0
   </td>
   <td>22,449
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>160
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td rowspan="5" >Aged 65+
   </td>
   <td>0
   </td>
   <td>111,613
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>308
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>19
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>0
   </td>
  </tr>
</table>



## References
[1	CMO Messaging. COVID-19 Therapeutic Alert - Inhaled Budesonide for Adults (50 Years and Over) with COVID-19. MHRA Cent. Alerting Syst. 2021; published online April 12. https://www.cas.mhra.gov.uk/ViewandAcknowledgment/ViewAlert.aspx?AlertID=103154 (accessed Aug 8, 2021).](https://www.zotero.org/google-docs/?9svTx4)

[2	PRINCIPLE Collaborative Group, Yu L-M, Bafadhel M, et al. Inhaled budesonide for COVID-19 in people at higher risk of adverse outcomes in the community: interim analyses from the PRINCIPLE trial. Primary Care Research, 2021 DOI:10.1101/2021.04.10.21254672.](https://www.zotero.org/google-docs/?9svTx4)

[3	PRIMIS. Covid-19. Univ. Nottm. https://www.nottingham.ac.uk/primis/covid-19/covid-19.aspx (accessed Aug 8, 2021).](https://www.zotero.org/google-docs/?9svTx4)

[4	opensafely/principle-inhaler-uptake. https://github.com/opensafely/principle-inhaler-uptake (accessed Aug 13, 2021).](https://www.zotero.org/google-docs/?9svTx4)

[5	Yu L-M, Bafadhel M, Dorward J, et al. Inhaled budesonide for COVID-19 in people at high risk of complications in the community in the UK (PRINCIPLE): a randomised, controlled, open-label, adaptive platform trial. The Lancet 2021; : S014067362101744X.](https://www.zotero.org/google-docs/?9svTx4)


## Conflicts of Interest

All authors have completed the ICMJE uniform disclosure form at www.icmje.org/coi_disclosure.pdf and declare the following: over the past five years BG has received research funding from the Laura and John Arnold Foundation, the NHS National Institute for Health Research (NIHR), the NIHR School of Primary Care Research, the NIHR Oxford Biomedical Research Centre, the Mohn-Westlake Foundation, NIHR Applied Research Collaboration Oxford and Thames Valley, the Wellcome Trust, the Good Thinking Foundation, Health Data Research UK (HDRUK), the Health Foundation, and the World Health Organisation; he also receives personal income from speaking and writing for lay audiences on the misuse of science. KB holds a Wellcome Senior Research Fellowship (220283/Z/20/Z). HIM is funded by the NIHR Health Protection Research Unit in Immunisation, a partnership between Public Health England and London School of Hygiene & Tropical Medicine. AYSW holds a fellowship from the British Heart Foundation. EJW holds grants from MRC. RG holds grants from NIHR and MRC. RM holds a Sir Henry Wellcome Fellowship funded by the Wellcome Trust (201375/Z/16/Z). HF holds a UKRI fellowship. IJD has received unrestricted research grants and holds shares in GlaxoSmithKline (GSK). 


## Funding

This work was jointly funded by UKRI, NIHR and Asthma UK-BLF [COV0076; MR/V015737/] and the Longitudinal Health and Wellbeing strand of the National Core Studies programme. The OpenSAFELY data science platform is funded by the Wellcome Trust.

BG’s work on better use of data in healthcare more broadly is currently funded in part by: the Wellcome Trust, NIHR Oxford Biomedical Research Centre, NIHR Applied Research Collaboration Oxford and Thames Valley, the Mohn-Westlake Foundation; all DataLab staff are supported by BG’s grants on this work. LS reports grants from Wellcome, MRC, NIHR, UKRI, British Council, GSK, British Heart Foundation, and Diabetes UK outside this work. JPB is funded by a studentship from GSK. AS is employed by LSHTM on a fellowship sponsored by GSK. KB holds a Wellcome Senior Research Fellowship (220283/Z/20/Z). HIM is funded by the National Institute for Health Research (NIHR) Health Protection Research Unit in Immunisation, a partnership between Public Health England and LSHTM. AYSW holds a fellowship from BHF. BMK is also employed by NHS England working on medicines policy and clinical lead for primary care medicines data. RM holds a Sir Henry Wellcome fellowship. EW holds grants from MRC.ID holds grants from NIHR and GSK. RM holds a Sir Henry Wellcome Fellowship funded by the Wellcome Trust. HF holds a UKRI fellowship. RME is funded by HDR-UK and the MRC

The views expressed are those of the authors and not necessarily those of the NIHR, NHS England, Public Health England or the Department of Health and Social Care. 

Funders had no role in the study design, collection, analysis, and interpretation of data; in the writing of the report; and in the decision to submit the article for publication. 
