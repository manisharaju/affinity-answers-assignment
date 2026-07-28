# Question 1 - Design Choices

## Objective
Develop a Python program that accepts a search term, retrieves products from MDComputers, and saves the product information in JSON format.

## Libraries Used

- requests
- BeautifulSoup (bs4)
- json

## Design Choices

### requests
Used to send HTTP requests and fetch the HTML page efficiently.

### BeautifulSoup
Used to parse HTML and extract product details such as product name, price, and product link.

### JSON Output
JSON was selected because it is:
- Easy to read
- Structured
- Portable
- Easy to process by other applications

## Modular Design

The program is divided into the following functions:

- get_search_term()
- build_search_url()
- fetch_page()
- extract_products()
- save_to_json()
- main()

This makes the program easier to maintain and understand.

## Error Handling

The program uses try-except blocks to handle network errors gracefully.
