# Interview Slot App

## Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

1. **Clone the Git repository**:
    ```bash
    git clone "https://github.com/FinuAjas/Interview-Slot-App.git"
    ```

2. **Set up a virtual environment**:
    ```bash

    cd Interview_Slot_App

    # Create a virtual environment
    virtualenv venv

    # Activate the virtual environment
    source venv/bin/activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Database**:
    ```
    You don't need to set up a database manually because `db.sqlite3` is already included in the project. The project is configured to use SQLite as the default database. If you wish to use a different database (e.g., PostgreSQL, MySQL), update the `DATABASES` configuration in the `settings.py` file.

    ```

5. **Run the server**:
    ```bash
    # Start the server
    python manage.py runserver
    ```
    Your server should now be running on  [http://localhost:8000/](http://localhost:8000/).

---

## Application URLs

- **User Registration [POST] method**: [http://localhost:8000/api/](http://localhost:8000/api/)

Sample data to create an entry.

{
    "email": "example@example.com",
    "phone_number": 9876543210,
    "role": "Interviewer", / "Candidate"
    "start_time": "00:00:00",
    "end_time": "23:00:00"
}   

- **Getslots [GET] method**: [http://localhost:8000/api/getslots/candidate ID/interviewer ID/](http://localhost:8000/api/getslots/candidate ID/interviewer ID/)

---

"For more information or queries, feel free to contact us at finuajas@gmail.com."
