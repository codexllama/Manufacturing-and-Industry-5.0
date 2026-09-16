from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = FastAPI(title="AutoPlant-OS API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


# ============================================================
# TEST DATABASE CONNECTION
# ============================================================

@app.get("/api/test")
def test_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return {
            "status": "success",
            "message": "PostgreSQL connection successful!",
            "database": version
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ============================================================
# LOGIN
# ============================================================

@app.post("/api/login")
def login(employee_id: str, password: str):

    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(
            """
            SELECT
                u.user_id,
                u.employee_id,
                u.full_name,
                u.role,
                u.department_id,
                u.status,
                d.department_name
            FROM users u
            LEFT JOIN departments d
                ON u.department_id = d.department_id
            WHERE u.employee_id = %s
            AND u.password = %s
            """,
            (employee_id, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid employee ID or password"
            )

        return {
            "status": "success",
            "user": user
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# USERS
# ============================================================

@app.get("/api/users")
def get_users(role: str = None):

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    if role:
        cursor.execute(
            """
            SELECT
                u.user_id,
                u.employee_id,
                u.full_name,
                u.role,
                u.department_id,
                u.status,
                d.department_name
            FROM users u
            LEFT JOIN departments d
                ON u.department_id = d.department_id
            WHERE u.role = %s
            ORDER BY u.user_id
            """,
            (role,)
        )
    else:
        cursor.execute(
            """
            SELECT
                u.user_id,
                u.employee_id,
                u.full_name,
                u.role,
                u.department_id,
                u.status,
                d.department_name
            FROM users u
            LEFT JOIN departments d
                ON u.department_id = d.department_id
            ORDER BY u.user_id
            """
        )

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


@app.get("/api/users/{user_id}")
def get_user(user_id: int):

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            u.user_id,
            u.employee_id,
            u.full_name,
            u.role,
            u.department_id,
            u.status,
            d.department_name
        FROM users u
        LEFT JOIN departments d
            ON u.department_id = d.department_id
        WHERE u.user_id = %s
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ============================================================
# MACHINES
# ============================================================

@app.get("/api/machines")
def get_machines():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            m.machine_id,
            m.machine_name,
            m.department_id,
            m.status,
            d.department_name
        FROM machines m
        LEFT JOIN departments d
            ON m.department_id = d.department_id
        ORDER BY m.machine_id
        """
    )

    machines = cursor.fetchall()

    cursor.close()
    conn.close()

    return machines


# ============================================================
# DEPARTMENTS
# ============================================================

@app.get("/api/departments")
def get_departments():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT *
        FROM departments
        ORDER BY department_id
        """
    )

    departments = cursor.fetchall()

    cursor.close()
    conn.close()

    return departments


# ============================================================
# ATTENDANCE
# ============================================================

@app.get("/api/attendance")
def get_attendance():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            a.*,
            u.full_name,
            u.employee_id
        FROM attendance a
        LEFT JOIN users u
            ON a.user_id = u.user_id
        ORDER BY a.attendance_id
        """
    )

    attendance = cursor.fetchall()

    cursor.close()
    conn.close()

    return attendance


# ============================================================
# TASKS
# ============================================================

@app.get("/api/tasks")
def get_tasks():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            t.*,
            u.full_name
        FROM tasks t
        LEFT JOIN users u
            ON t.assigned_to = u.user_id
        ORDER BY t.task_id
        """
    )

    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return tasks


# ============================================================
# MAINTENANCE
# ============================================================

@app.get("/api/maintenance")
def get_maintenance():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            mr.*,
            m.machine_name
        FROM maintenance_requests mr
        LEFT JOIN machines m
            ON mr.machine_id = m.machine_id
        ORDER BY mr.request_id
        """
    )

    maintenance = cursor.fetchall()

    cursor.close()
    conn.close()

    return maintenance


# ============================================================
# PRODUCTION
# ============================================================

@app.get("/api/production")
def get_production():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            p.*,
            m.machine_name
        FROM production p
        LEFT JOIN machines m
            ON p.machine_id = m.machine_id
        ORDER BY p.production_id
        """
    )

    production = cursor.fetchall()

    cursor.close()
    conn.close()

    return production


# ============================================================
# SENSOR DATA
# ============================================================

@app.get("/api/sensors")
def get_sensors():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            s.*,
            m.machine_name
        FROM sensor_data s
        LEFT JOIN machines m
            ON s.machine_id = m.machine_id
        ORDER BY s.sensor_id
        """
    )

    sensors = cursor.fetchall()

    cursor.close()
    conn.close()

    return sensors


# ============================================================
# ALERTS
# ============================================================

@app.get("/api/alerts")
def get_alerts():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            a.*,
            m.machine_name
        FROM alerts a
        LEFT JOIN machines m
            ON a.machine_id = m.machine_id
        ORDER BY a.alert_id
        """
    )

    alerts = cursor.fetchall()

    cursor.close()
    conn.close()

    return alerts


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/")
def home():
    return FileResponse(
        "../autoplant-os-light-theme.html"
    )