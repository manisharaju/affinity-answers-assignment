import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def get_search_term():
    # Accepts a search term from the user.
    return input("Enter search term: ").strip()


def build_search_url(search_term):
    # Creates the search URL for MDComputers.
    base_url = "https://mdcomputers.in/"
    encoded_term = quote_plus(search_term)

    return f"{base_url}?route=product/search&search={encoded_term}"


def fetch_page(url):
    # Fetches the search results page.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None


def extract_products(html):
    # Extracts product information from the HTML.
    soup = BeautifulSoup(html, "html.parser")
    products = []

    product_cards = soup.find_all("div", class_="product-wrapper")

    for product in product_cards:

        title_tag = product.find("h3",class_="product-entities-title")

        price_tag = product.find("span",class_="price")

        if title_tag and title_tag.a:

            product_name = title_tag.a.get_text(strip=True)

            if price_tag:
                prices = price_tag.get_text(" ",strip=True).split()

                if len(prices) >= 2:
                    price = prices[-1]
                else:
                    price = prices[0]
            else:
                price = "Not Available"

            products.append({ "Product Name": product_name,"Selling Price": price})

    return products

def display_products(products):
    # Displays the extracted products in a readable format.
    print("\nProducts Found:\n")

    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['Product Name']}")
        print(f"   Selling Price: {product['Selling Price']}")
        print()


def main():

    search_term = get_search_term()

    url = build_search_url(search_term)

    html = fetch_page(url)

    if html:

        products = extract_products(html)

        if products:
            display_products(products)
        else:
            print("No products found.")


if __name__ == "__main__":
    main()