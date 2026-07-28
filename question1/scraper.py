import requests
from bs4 import BeautifulSoup
import json

def get_search_term():
    # Accepts a search term from the user.
    return input("Enter product to search: ").strip()

def build_search_url(search_term):
    # Creates the search URL for MDComputers.
    base_url = "https://mdcomputers.in/"
    return f"{base_url}?route=product/search&search={search_term}"

def fetch_page(url):
    """
    Fetches the search results page from MDComputers.
    """

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
    """
    Extracts product information from the HTML.
    """

    soup = BeautifulSoup(html, "html.parser")
    products = []

    product_cards = soup.find_all("div", class_="product-wrapper")

    for product in product_cards:

        title_tag = product.find("h3", class_="product-entities-title")
        price_tag = product.find("span", class_="price")

        if title_tag and title_tag.a:

            product_name = title_tag.a.text.strip()

            product_link = title_tag.a["href"]

            price = (
                price_tag.get_text(" ", strip=True)
                if price_tag
                else "Not Available"
            )

            products.append(
                {
                    "Product Name": product_name,
                    "Price": price,
                    "Product Link": product_link,
                }
            )

    return products
def save_to_json(products):
    """
    Saves products to a JSON file.
    """

    with open("question1/products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)

    print(f"\nSaved {len(products)} products to products.json")
def main():

    search_term = get_search_term()

    url = build_search_url(search_term)

    html = fetch_page(url)

    if html:

        products = extract_products(html)

        if products:

            save_to_json(products)

            print("\nProducts Found:\n")

            for product in products:
                print(product)

        else:
            print("No products found.")


if __name__ == "__main__":
    main()