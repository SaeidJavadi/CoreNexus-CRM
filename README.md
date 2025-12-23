# CoreNexus CRM 🚀
**A Comprehensive Subscription, User Management, and Notification System.**

CoreNexus CRM is a powerful, production-ready CRM system designed to manage subscriptions, user interactions, and organizational communications. It features a robust web-based administration panel for operators and a full-featured REST API that seamlessly connects to Android and iOS mobile applications.

---

## 🌟 Overview
This project serves as the central hub for organizations to manage their members. Users can purchase or renew subscriptions via mobile apps, participate in lotteries, and stay updated with organizational news. Meanwhile, administrators and staff use the web panel to oversee operations, verify payments, and manage community engagement.

## ✨ Key Features

### 👥 Advanced Subscription Management
* **Categorized Memberships:** Automated handling of different subscription tiers based on age and conditions (Common60, Common61, Common70).
* **Deceased Services Management:** Dedicated modules for managing religious services and legal requirements for deceased members (`CommonDead`, `JudiciaryDead`, `DoingDead`).
* **Public Assistance:** Integrated tools for tracking charitable donations and help names.

### 🎰 Lottery & Reward System
* **Lottery Management:** Organize specialized lotteries (e.g., Quran memorization or religious pilgrimages).
* **Dynamic Gift Tables:** A complex system (`TableType`, `TableGift`) to manage installments, discounts, and annual numbers.
* **Chance Calculation:** Automated calculation of lottery chances based on user payment status and history via `TableGiftUser`.

### 📢 Integrated Communication & Social Hub
* **Smart Notifications:** Send global or targeted notifications with "Force" options and "Seen" tracking via JSON fields.
* **Internal Social Media:** A built-in social feed supporting Posts and Stories with Like, View, and Comment functionality to boost user engagement.
* **News Feed:** A dedicated section for official announcements and news updates using `NewsText`.

### 💳 Financial & Payment Tracking
* **Payment Verification:** Track subscription payments and gift table installments through `TablePayment`.
* **Status Control:** Administrative toggle to activate or deactivate user services based on financial status.

---

## 🛠 Tech Stack
* **Backend Framework:** [Django](https://www.djangoproject.com/) (Python)
* **API Engine:** [Django Rest Framework (DRF)](https://www.django-rest-framework.org/)
* **Database:** PostgreSQL (Recommended) / SQLite
* **Authentication:** Custom User Model with JWT/Token support for Mobile.
* **Internationalization:** Full support for multi-language translations (i18n) using `gettext_lazy`.

---

## 🏗 Database Architecture (Core Models)
The system logic is built around several specialized models:
- `Common60/61/70`: Handles user registration and age-based subscriptions.
- `TableGiftUser`: Manages the relationship between users and specific reward/gift plans.
- `SocialMedia`: Supports multimedia content (Post/Story) for the mobile feed.
- `Notification`: A many-to-many system for high-priority user alerts.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 5.x

### Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com:SaeidJavadi/CoreNexus-CRM.git
   cd CoreNexus-CRM
   ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Start the server:**
    ```bash
    python manage.py runserver
    ```
## 📱 Mobile Integration

The project is API-First. All functionalities, from purchasing subscriptions to interacting with social posts, are exposed via REST endpoints, making it ready for React Native, Flutter, or Native mobile development.

## 🔗 Project Demo

You can view the live demo of the project here: 👉 Live Demo: [CoreNexus CRM](https://nexcrm.sjpy.ir/)
* **Demo Access:**
    * **Username:** `admin`
    * **Password:** `admin`

## 🔗 API Documentation & Demo
You can explore the live API endpoints and interact with the system through the Swagger UI:

* **Swagger Documentation:** [https://nexcrm.sjpy.ir/swagger/](https://nexcrm.sjpy.ir/swagger/)

> [!TIP]
> To test protected endpoints in Swagger, first obtain a token from `/api/rest-auth/login/`, then use the **Authorize** button and enter `Token <your_token_string>`.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📜 License

This project is licensed under the MIT License.