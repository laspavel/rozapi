# RozAPI – Python Client for Rozetka API

RozAPI is a lightweight Python library designed to simplify interactions with the Rozetka e-commerce platform's API.

## 📌 Features

* Straightforward authentication using Rozetka credentials
* Simplified API request handling
* Support for GET and POST methods
* Customizable request parameters

## ⚙️ Requirements

* Python 3.6 or higher
* Valid Rozetka account credentials

## 🚀 Installation

Since RozAPI is a single-file module, you can install it by downloading the rozapi.py file directly:

* Download the rozapi.py file from the repository.
* Place it in your project directory.
* Import it into your Python script:

```python
import rozapi
```

## 🧪 Usage Example
```python
import rozapi

# Initialize the Rozetka API client with your credentials
rapi = rozapi.RozetkaAPI('YourRozetkaLogin', 'YourRozetkaPassword')

# Fetch a list of orders
orders = rapi.api_request(
    api_type='get',
    api_method='orders/search',
    params={'page': '1', 'sort': 'id'}
)

# Process the retrieved orders
for order in orders.get('data', []):
    print(f"Order ID: {order['id']}, Status: {order['status']}")
```

## 🛡️ License

MIT License.

## 🤝 Contributions

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact

Author: [laspavel](https://github.com/laspavel)

Feel free to reach out with questions or ideas.

---
