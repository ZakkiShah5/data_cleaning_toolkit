
# Data Cleaning Toolkit

A reusable Python data cleaning toolkit project that cleans the different types of data built as practice for real-world Pandas workflows.

## What It Does

Given raw data, the program:
- Cleans inconsistent name casing and handles missing values
- Cleans and converts date data to pandas datetime,
- Cleans email data and converts to lowercase.
- Cleans currency Series, removing the currency signs and converts to numeric value.

## Functions

### `clean_text(series)`
Strips whitespace, converts to title case, fills missing values with "Unknown".

### `clean_email(series)`
Lowercases and strips email addresses, fills missing values with "unknown".

### `clean_date(series)`
Parses mixed-format date strings into datetime, handling multiple formats gracefully. Unparseable entries become NaT.

### `clean_currency(series)`
Converts currency strings (e.g. "$1,200.50") into floats. Invalid entries become NaN.

## Example Output

customer_id        name          email signup_date  purchase_amount
0            1   Ana Silva  ana@email.com  2024-01-15          1200.50
1            2   Bob Jones  bob@email.com  2024-02-20            45.00
2            3  Cid Santos  cid@email.com  2024-03-15              NaN
3            4     Unknown  dan@email.com  2024-04-10           300.75
4            5   Dan   Lee        Unknown  2024-05-05            89.99
5            6   Eve Brown  eve@email.com         NaT           150.00

*Note*: `NaT`/`NaN` values in the output are intentional — they mark genuinely invalid entries (e.g., "invalid" as a date or currency value) that the toolkit correctly identified and flagged rather than silently mishandling.

## How to Run

This project is a python reusable file which can be imported into any jupyter notebook or even python file. To run it:

```bash
pip install pandas numpy jupyter
jupyter notebook demo.ipynb
```

Then run all cells from top to bottom.

## Skills Practiced

- Building reusable, importable Python modules
- Regex-based text cleaning
- Vectorized string operations (`.str` accessor)
- Robust date parsing across multiple formats (with fallback handling)
- Safe numeric conversion with error coercion
- Writing pure functions (no side effects on input data)


## Possible Improvements

- Load data from real CSV files instead of hardcoded DataFrames
- Add support for additional data types (phone numbers, addresses, etc.)
- Add unit tests to formally verify edge-case handling