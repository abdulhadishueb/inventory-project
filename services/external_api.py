import requests


def get_product_from_api(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == 1:
            product = data["product"]
            return {
                "name": product.get("product_name", "No name"),
                "brand": product.get("brands", "No brand"),
                "ingredients": product.get("ingredients_text", "No ingredients")
            }
        else:
            return {"error": "Product not found"}

    except:
        return {"error": "Could not connect to API"}