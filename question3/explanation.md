# Question 3

## Objective

Create a Unix shell script that accepts a CSV URL, downloads the data, extracts the company name, location, and founding year, and sorts the results by founding year.

## Tools Used

- bash
- curl
- awk
- sort

## Approach

1. Accept the URL as a command-line argument.
2. Download the CSV using `curl`.
3. Skip the header row.
4. Extract the required columns using `awk`.
5. Sort the records by founding year using `sort`.
6. Display the formatted output.