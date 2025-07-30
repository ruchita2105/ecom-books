# streamlit_app.py

import streamlit as st

# Sample product list
products = [
    {"name": "Book 1", "price": 250, "image": "store/static/store/images/images.jpeg"},
    {"name": "Book 2", "price": 350, "image": "store/static/store/images/images.jpeg"},
]

# Cart session
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("📚 Welcome to Ecom Bookstore")

st.sidebar.header("🛒 Cart")
total = 0
for item in st.session_state.cart:
    st.sidebar.write(f"{item['name']} - ₹{item['price']}")
    total += item['price']
st.sidebar.write(f"---\n**Total: ₹{total}**")

# Display products
for product in products:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(product["image"], width=100)
    with col2:
        st.subheader(product["name"])
        st.write(f"Price: ₹{product['price']}")
        if st.button(f"Add {product['name']} to Cart", key=product["name"]):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")

