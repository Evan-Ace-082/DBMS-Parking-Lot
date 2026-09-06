# 🚗 Smart Parking Management System (EasyPark)

> 🌐 **Live Demo Website (Direct Online Access):**  
> 👉 **[https://evan-ace-082.github.io/DBMS-Parking-Lot/](https://evan-ace-082.github.io/DBMS-Parking-Lot/)**

A modern Smart Parking Management System with real-time slot monitoring, dynamic vehicle check-in/check-out, digital ticketing, reservations, user management, feedback, and database analytics.

---

## 🌟 Key Features

1. **🔐 Authentication & User Roles:**
   - Real registration for drivers/customers with custom username and password.
   - Separate **User Dashboard** and **Admin Dashboard**.
   - Default Administrator access: `root` / `1234`.

2. **🅿️ Real-time Area & Slot Monitoring:**
   - Multi-area parking network across Dhaka (Gulshan, Banani, Dhanmondi, Uttara, Motijheel, Mirpur).
   - Live color-coded slot statuses: Available (Green), Occupied (Red), Reserved (Yellow).

3. **🚗 Park Now (Check-In):**
   - Vehicle registration with instant slot assignment.
   - Automated Digital Parking Pass / QR Ticket generation.

4. **💳 Check-Out & Billing:**
   - Vehicle plate / Ticket ID search.
   - Auto-calculated elapsed time and total fee based on hourly rates.
   - Payment options: bKash, Nagad, Cash, Card.

5. **📅 Spot Reservations:**
   - Advance parking spot booking with confirmation tracking.

6. **📈 Reports & DBMS Analytics:**
   - Peak parking hours bar chart.
   - Vehicle type share analysis.
   - Popular parking spots and top active users.

---

## 💻 Local Setup & Execution (Portable)

### Prerequisites
- **Python 3.8+**: Ensure Python is installed.

### Installation
1. **Clone or Download** this repository.
2. **Create a Virtual Environment:**
   - Windows: `python -m venv venv`
   - Mac/Linux: `python3 -m venv venv`
3. **Activate Environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
```bash
# Option A: Quick Runner
python main.py start

# Option B: Run Services Manually
# Terminal 1 (Backend API):
uvicorn backend.main:app --reload --port 8000

# Terminal 2 (Frontend Web):
python frontend_flask/app.py
```

- **Frontend:** [http://127.0.0.1:5001](http://127.0.0.1:5001)
- **Backend Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
