# TaxCalculator
A simplified version of ATO Tax Calculator

# Requirements 
- [Python](https://www.python.org/) 3.8+
- [PIP](https://pip.pypa.io/en/stable/)
- [GIT](https://git-scm.com/)

## Installation

1. Clone repository to your local filesystem
```bash
git clone https://github.com/Harman-92/TaxCalculator.git
```
2. (Optional) Create a virtual environment using venv
```bash
python -m venv env
```

3. Install dependencies using pip
```bash
pip install -r requirements.txt
```

## Usage

```bash
python tax_calculator.py
```
## Example

![](https://img001.prntscr.com/file/img001/5cWoap3lRrW7gl6oz5_93A.png)

## Tax Rates
The Tax Rates are taken from the taxratesinfo website and are in the following format. <br/>
![](https://img001.prntscr.com/file/img001/gWXcGzEnRImY3HDvu2-CcA.png)
<br/>
<br/>
[tax_rates.xlsx](https://github.com/Harman-92/TaxCalculator/blob/main/tax_rates.xlsx) allows us to write and update tax rates with individual sheet for a particular year
![](https://img001.prntscr.com/file/img001/duTTEL1xTQiO_7LwfNe1-g.png)
## Assumptions
- Tax payer is an Australian Resident
- Medicare Levy is not included
