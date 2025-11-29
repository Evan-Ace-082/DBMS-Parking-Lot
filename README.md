# Smart Parking System (Portable)

This is a portable version of the Smart Parking System, designed to run on Windows, macOS, and Linux.

## Prerequisites

- **Python 3.8+**: Ensure Python is installed and added to your system's PATH.

## Installation

1.  **Download and Extract**: Download this folder and extract it to a location on your computer.
2.  **Open Terminal/Command Prompt**: Navigate to this folder.
3.  **Create a Virtual Environment** (Recommended):
    -   *Windows*: `python -m venv venv`
    -   *Mac/Linux*: `python3 -m venv venv`
4.  **Activate the Virtual Environment**:
    -   *Windows*: `venv\Scripts\activate`
    -   *Mac/Linux*: `source venv/bin/activate`
5.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Copy the `.env.example` file and rename it to `.env`.
    -   *Windows*: `copy .env.example .env`
    -   *Mac/Linux*: `cp .env.example .env`
2.  **Database**: By default, the system uses **SQLite**, which requires no setup. A file named `parking_lot_db.sqlite` will be created automatically.
    -   If you prefer MySQL, edit the `.env` file and update `DATABASE_URL`.

## Running the Application

You need to run the **Backend** and **Frontend** in two separate terminal windows.

### 1. Start the Backend (API)

Open a terminal, activate the venv, and run:

```bash
# From the root directory
uvicorn backend.main:app --reload
```
*The API will start at http://127.0.0.1:8000*

### 2. Start the Frontend (Web Interface)

Open a **second** terminal, activate the venv, and run:

```bash
# From the root directory
python frontend_flask/app.py
```
*The website will be available at http://127.0.0.1:5001*

## Usage

1.  Open your browser and go to `http://127.0.0.1:5001`.
2.  **Register** a new account.
3.  **Login** with `root` / `1234` for the Super Admin account, or use your newly registered user.
