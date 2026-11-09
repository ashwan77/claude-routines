# Pressure Risk Calculator

`PressureRiskCalculator.html` is a single offline HTML file for scoring a **Waterlow** or **Braden** pressure injury risk assessment.

## Using it
1. Copy `PressureRiskCalculator.html` anywhere (eg OneDrive) and double click it. It opens in Safari, Chrome or Edge with no internet needed.
2. Enter the client name or initials and the assessment date.
3. Choose Waterlow or Braden and tick through each section. Hover over or tap any **?** for an explanation.
4. The total, risk level and recommended actions update live at the bottom.
5. Press **Download PDF** to save a one page summary named like `Waterlow 09.11.2026 SI.pdf`.

Nothing is stored or sent anywhere. Closing the tab clears the answers.

## What is scored
* **Waterlow** (2005 revision) with the built in Malnutrition Screening Tool, an optional BMI calculator, and special risks. Bands: under 10 not at risk, 10 to 14 at risk, 15 to 19 high risk, 20 and over very high risk.
  * **Age based BMI cut off.** Age 70 and over scores Below average (3) for a BMI under 22 instead of under 20, using the international [GLIM criteria for malnutrition (Cederholm et al 2019)](https://pubmed.ncbi.nlm.nih.gov/30181091/). Other bands follow the Waterlow card. Enter age in years to tick the age band automatically (needed for 65 to 74, since 70 falls inside that band). The PDF notes when the 70 and over cut off was used.
* **Braden** (adult). Bands: 19 to 23 no risk, 15 to 18 mild, 13 to 14 moderate, 10 to 12 high, 9 or less very high.

## Rebuilding
The page is edited in `build/template.html`. The PDF library (jsPDF 4.2.1, MIT licence, see `build/vendor/jspdf.LICENSE`) is inlined by:

```bash
python3 build/build.py
```
