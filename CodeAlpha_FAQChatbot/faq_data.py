"""
FAQ knowledge base for the chatbot.
Topic: E-commerce store support (Shopinza-style).
Each entry has a question (and optional alternate phrasings) + its answer.
"""

FAQS = [
    {
        "question": "How do I create an account?",
        "alt": ["how to sign up", "how can i register", "create new account"],
        "answer": "Tap on 'Sign Up' on the login screen, enter your name, email, and password, then verify your email to activate your account."
    },
    {
        "question": "How can I track my order?",
        "alt": ["where is my order", "order status", "track my package", "track shipment"],
        "answer": "Go to 'My Orders' in your profile, select the order, and you'll see real-time tracking status from processing to delivery."
    },
    {
        "question": "What payment methods do you accept?",
        "alt": ["how can i pay", "payment options", "do you accept jazzcash", "do you accept easypaisa"],
        "answer": "We accept JazzCash, Easypaisa, major debit/credit cards, and Cash on Delivery (COD) for eligible areas."
    },
    {
        "question": "How do I return or exchange a product?",
        "alt": ["return policy", "how to exchange item", "refund process"],
        "answer": "You can request a return within 7 days of delivery from 'My Orders'. Once approved, our courier will pick up the item and your refund or exchange will be processed within 3-5 business days."
    },
    {
        "question": "How long does delivery take?",
        "alt": ["delivery time", "shipping time", "how many days for delivery"],
        "answer": "Standard delivery takes 2-5 business days depending on your city. Major cities like Islamabad, Lahore, and Karachi usually receive orders within 2-3 days."
    },
    {
        "question": "Is Cash on Delivery available?",
        "alt": ["cod available", "pay on delivery"],
        "answer": "Yes, Cash on Delivery is available in most major cities across Pakistan. You can select COD as your payment method at checkout."
    },
    {
        "question": "How do I apply a promo code?",
        "alt": ["discount code", "coupon code", "apply voucher"],
        "answer": "At checkout, enter your promo code in the 'Apply Promo Code' field before placing your order, and the discount will be applied automatically."
    },
    {
        "question": "How can I contact customer support?",
        "alt": ["customer service", "contact support", "need help"],
        "answer": "You can reach our support team via the 'Help & Support' section in the app, or email us directly — we usually respond within 24 hours."
    },
    {
        "question": "Can I cancel my order after placing it?",
        "alt": ["cancel order", "how to cancel"],
        "answer": "Yes, you can cancel an order from 'My Orders' as long as it hasn't been shipped yet. Once shipped, cancellation is no longer possible."
    },
    {
        "question": "How do I add items to my wishlist?",
        "alt": ["save item for later", "wishlist", "favorite items"],
        "answer": "Tap the heart icon on any product to add it to your wishlist. You can view all saved items anytime from the Wishlist tab."
    },
    {
        "question": "Are the products original/authentic?",
        "alt": ["are products fake", "genuine products"],
        "answer": "Yes, all products listed are 100% genuine and sourced directly from verified sellers and brands."
    },
    {
        "question": "How do I change my delivery address?",
        "alt": ["update address", "change shipping address"],
        "answer": "Go to your Profile > Addresses, and you can add, edit, or set a default delivery address before placing an order."
    },
]
