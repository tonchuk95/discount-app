import streamlit as st

# Заголовок сторінки
st.title("Магазин зі знижками 💰")

# Введення суми покупки
purchase_amount = st.number_input("Введіть суму покупки (грн):", min_value=0.0, step=0.1)

# Умови для визначення знижки
if purchase_amount > 10000:
    discount = 0.2
elif purchase_amount > 5000:
    discount = 0.15
elif purchase_amount > 1000:
    discount = 0.1
else:
    discount = 0

# Обчислення остаточної суми
new_price = purchase_amount - (purchase_amount * discount)

# Вивід результату
if discount > 0:
    st.success(f"✅ Ваша знижка: {int(discount * 100)}%")
    st.info(f"💵 Сума до сплати зі знижкою: {new_price:.2f} грн")
else:
    st.warning("⚠️ Знижка не надається.")
