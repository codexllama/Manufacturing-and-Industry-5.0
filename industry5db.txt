
-- ============================================================
-- AUTOPLANT-OS / INDUSTRY 5.0 DATABASE
-- 50 MEMBERS
-- 40 WORKERS + 7 MANAGERS + 3 ADMINS
-- PostgreSQL 18
-- ============================================================


-- ============================================================
-- REMOVE OLD TABLES
-- ============================================================

DROP TABLE IF EXISTS
    alerts,
    sensor_data,
    production,
    maintenance_requests,
    tasks,
    attendance,
    machines,
    users,
    departments
CASCADE;


-- ============================================================
-- 1. DEPARTMENTS
-- ============================================================

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO departments (department_name)
VALUES
    ('Production'),
    ('Assembly'),
    ('Quality'),
    ('Maintenance'),
    ('Warehouse'),
    ('Logistics'),
    ('Safety'),
    ('Administration');


-- ============================================================
-- 2. USERS
-- 40 WORKERS + 7 MANAGERS + 3 ADMINS = 50
-- ============================================================

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,

    employee_id VARCHAR(15) UNIQUE NOT NULL,

    full_name VARCHAR(100) NOT NULL,

    password VARCHAR(100) NOT NULL,

    role VARCHAR(20)
        CHECK (role IN ('Worker', 'Manager', 'Admin')),

    department_id INT
        REFERENCES departments(department_id),

    status VARCHAR(20) DEFAULT 'Active'
);


-- ============================================================
-- 40 WORKERS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES

-- Workers 1-10
('EMP-1001', 'Arjun Kumar', 'worker123', 'Worker', 1),
('EMP-1002', 'Ravi Sharma', 'worker123', 'Worker', 1),
('EMP-1003', 'Karthik Reddy', 'worker123', 'Worker', 2),
('EMP-1004', 'Suresh Naik', 'worker123', 'Worker', 2),
('EMP-1005', 'Mahesh Patel', 'worker123', 'Worker', 3),
('EMP-1006', 'Vikram Singh', 'worker123', 'Worker', 3),
('EMP-1007', 'Ramesh Rao', 'worker123', 'Worker', 4),
('EMP-1008', 'Ajay Verma', 'worker123', 'Worker', 4),
('EMP-1009', 'Ganesh Kumar', 'worker123', 'Worker', 5),
('EMP-1010', 'Sunil Reddy', 'worker123', 'Worker', 6),

-- Workers 11-20
('EMP-1011', 'Rahul Mehta', 'worker123', 'Worker', 1),
('EMP-1012', 'Manoj Kumar', 'worker123', 'Worker', 1),
('EMP-1013', 'Naveen Rao', 'worker123', 'Worker', 2),
('EMP-1014', 'Prakash Singh', 'worker123', 'Worker', 2),
('EMP-1015', 'Deepak Sharma', 'worker123', 'Worker', 3),
('EMP-1016', 'Rohit Patel', 'worker123', 'Worker', 3),
('EMP-1017', 'Sanjay Kumar', 'worker123', 'Worker', 4),
('EMP-1018', 'Vivek Reddy', 'worker123', 'Worker', 4),
('EMP-1019', 'Harish Naik', 'worker123', 'Worker', 5),
('EMP-1020', 'Tarun Verma', 'worker123', 'Worker', 6),

-- Workers 21-30
('EMP-1021', 'Abhishek Rao', 'worker123', 'Worker', 1),
('EMP-1022', 'Varun Sharma', 'worker123', 'Worker', 1),
('EMP-1023', 'Akash Kumar', 'worker123', 'Worker', 2),
('EMP-1024', 'Mohan Reddy', 'worker123', 'Worker', 2),
('EMP-1025', 'Rakesh Patel', 'worker123', 'Worker', 3),
('EMP-1026', 'Dinesh Singh', 'worker123', 'Worker', 3),
('EMP-1027', 'Yash Verma', 'worker123', 'Worker', 4),
('EMP-1028', 'Nikhil Rao', 'worker123', 'Worker', 4),
('EMP-1029', 'Lokesh Kumar', 'worker123', 'Worker', 5),
('EMP-1030', 'Chandan Reddy', 'worker123', 'Worker', 6),

-- Workers 31-40
('EMP-1031', 'Pavan Kumar', 'worker123', 'Worker', 1),
('EMP-1032', 'Sai Kiran', 'worker123', 'Worker', 1),
('EMP-1033', 'Surya Prakash', 'worker123', 'Worker', 2),
('EMP-1034', 'Madhav Rao', 'worker123', 'Worker', 2),
('EMP-1035', 'Teja Reddy', 'worker123', 'Worker', 3),
('EMP-1036', 'Raghu Sharma', 'worker123', 'Worker', 3),
('EMP-1037', 'Srinivas Naik', 'worker123', 'Worker', 4),
('EMP-1038', 'Vamsi Krishna', 'worker123', 'Worker', 4),
('EMP-1039', 'Naveen Kumar', 'worker123', 'Worker', 5),
('EMP-1040', 'Aditya Verma', 'worker123', 'Worker', 6);


-- ============================================================
-- 7 MANAGERS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES
('MGR-2001', 'Anil Kumar', 'manager123', 'Manager', 1),
('MGR-2002', 'Sneha Verma', 'manager123', 'Manager', 2),
('MGR-2003', 'Kiran Rao', 'manager123', 'Manager', 3),
('MGR-2004', 'Priyanka Sharma', 'manager123', 'Manager', 4),
('MGR-2005', 'Ramesh Patel', 'manager123', 'Manager', 5),
('MGR-2006', 'Swathi Reddy', 'manager123', 'Manager', 6),
('MGR-2007', 'Vijay Singh', 'manager123', 'Manager', 7);


-- ============================================================
-- 3 ADMINS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES
('ADM-3001', 'Rahul Sharma', 'admin123', 'Admin', 8),
('ADM-3002', 'Priya Reddy', 'admin123', 'Admin', 8),
('ADM-3003', 'Sandeep Kumar', 'admin123', 'Admin', 8);


-- ============================================================
-- 3. MACHINES
-- ============================================================

CREATE TABLE machines (
    machine_id SERIAL PRIMARY KEY,

    machine_name VARCHAR(100) NOT NULL,

    department_id INT
        REFERENCES departments(department_id),

    status VARCHAR(20)
);


INSERT INTO machines
    (machine_name, department_id, status)
VALUES
('Torque Bot', 1, 'Stopped'),
('Stamp Press', 2, 'Maintenance'),
('Spot Welder', 2, 'Running'),
('Auto Guided Vehicle', 5, 'Running'),
('Engine Assembly Robot', 1, 'Running'),
('Paint Robot', 2, 'Running'),
('CNC Machine', 1, 'Running'),
('Quality Inspection Bot', 3, 'Running'),
('Hydraulic Press', 1, 'Running'),
('Welding Robot', 2, 'Running'),
('Conveyor System', 5, 'Running'),
('Laser Cutting Machine', 1, 'Running'),
('Drilling Machine', 2, 'Maintenance'),
('Packaging Robot', 5, 'Running'),
('Material Handling AGV', 6, 'Running');


-- ============================================================
-- 4. ATTENDANCE
-- ============================================================

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,

    user_id INT
        REFERENCES users(user_id),

    attendance_date DATE,

    status VARCHAR(20)
);


INSERT INTO attendance
    (user_id, attendance_date, status)
SELECT
    user_id,
    CURRENT_DATE,
    CASE
        WHEN user_id % 10 = 0 THEN 'Absent'
        ELSE 'Present'
    END
FROM users;


-- ============================================================
-- 5. TASKS
-- ============================================================

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,

    title VARCHAR(100),

    assigned_to INT
        REFERENCES users(user_id),

    assigned_by INT
        REFERENCES users(user_id),

    status VARCHAR(20)
);


INSERT INTO tasks
    (title, assigned_to, assigned_by, status)
VALUES
('Machine Inspection', 1, 41, 'Completed'),
('Assembly Line Check', 2, 42, 'In Progress'),
('Quality Inspection', 5, 43, 'Pending'),
('Maintenance Inspection', 7, 44, 'In Progress'),
('Inventory Verification', 9, 45, 'Pending'),
('Safety Equipment Check', 12, 47, 'Completed'),
('Production Report', 15, 41, 'Pending'),
('Sensor Calibration', 18, 44, 'In Progress');


-- ============================================================
-- 6. MAINTENANCE REQUESTS
-- ============================================================

CREATE TABLE maintenance_requests (
    request_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    reported_by INT
        REFERENCES users(user_id),

    issue_description TEXT,

    status VARCHAR(20)
);


INSERT INTO maintenance_requests
    (machine_id, reported_by, issue_description, status)
VALUES
(1, 7, 'Torque calibration required', 'Open'),
(2, 13, 'Scheduled preventive maintenance', 'In Progress'),
(7, 21, 'CNC vibration above normal level', 'Open'),
(13, 31, 'Drilling machine requires inspection', 'Pending');


-- ============================================================
-- 7. PRODUCTION
-- ============================================================

CREATE TABLE production (
    production_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    production_date DATE,

    units_produced INT
);


INSERT INTO production
    (machine_id, production_date, units_produced)
SELECT
    machine_id,
    CURRENT_DATE,
    100 + (machine_id * 25)
FROM machines;


-- ============================================================
-- 8. SENSOR DATA
-- ============================================================

CREATE TABLE sensor_data (
    sensor_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    temperature NUMERIC(5,2),

    vibration NUMERIC(5,2),

    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO sensor_data
    (machine_id, temperature, vibration)
SELECT
    machine_id,
    35 + (machine_id * 0.5),
    1.0 + (machine_id * 0.1)
FROM machines;


-- ============================================================
-- 9. ALERTS
-- ============================================================

CREATE TABLE alerts (
    alert_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    alert_type VARCHAR(50),

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO alerts
    (machine_id, alert_type, message)
VALUES
(1, 'Machine Stopped', 'Torque Bot has stopped unexpectedly'),
(2, 'Maintenance', 'Stamp Press is under scheduled maintenance'),
(7, 'Vibration', 'CNC Machine vibration above normal level'),
(13, 'Maintenance', 'Drilling Machine requires inspection'),
(3, 'Production', 'Spot Welder operating normally');


-- ============================================================
-- VERIFICATION
-- ============================================================

-- Total users
SELECT COUNT(*) AS total_users
FROM users;


-- Users by role
SELECT
    role,
    COUNT(*) AS total
FROM users
GROUP BY role
ORDER BY
    CASE role
        WHEN 'Worker' THEN 1
        WHEN 'Manager' THEN 2
        WHEN 'Admin' THEN 3
    END;

-- All users
SELECT
    u.user_id,
    u.employee_id,
    u.full_name,
    u.role,
    d.department_name,
    u.status
FROM users u
JOIN departments d
    ON u.department_id = d.department_id
ORDER BY
    CASE u.role
        WHEN 'Worker' THEN 1
        WHEN 'Manager' THEN 2
        WHEN 'Admin' THEN 3
    END,
    u.user_id;

-- Total machines
SELECT COUNT(*) AS total_machines
FROM machines;


-- All machines
SELECT
    m.machine_id,
    m.machine_name,
    d.department_name,
    m.status
FROM machines m
JOIN departments d
    ON m.department_id = d.department_id
ORDER BY m.machine_id;






-- ============================================================
-- AUTOPLANT-OS / INDUSTRY 5.0 DATABASE
-- 50 MEMBERS
-- 40 WORKERS + 7 MANAGERS + 3 ADMINS
-- PostgreSQL 18
-- ============================================================


-- ============================================================
-- REMOVE OLD TABLES
-- ============================================================

DROP TABLE IF EXISTS
    alerts,
    sensor_data,
    production,
    maintenance_requests,
    tasks,
    attendance,
    machines,
    users,
    departments
CASCADE;


-- ============================================================
-- 1. DEPARTMENTS
-- ============================================================

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO departments (department_name)
VALUES
    ('Production'),
    ('Assembly'),
    ('Quality'),
    ('Maintenance'),
    ('Warehouse'),
    ('Logistics'),
    ('Safety'),
    ('Administration');


-- ============================================================
-- 2. USERS
-- 40 WORKERS + 7 MANAGERS + 3 ADMINS = 50
-- ============================================================

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,

    employee_id VARCHAR(15) UNIQUE NOT NULL,

    full_name VARCHAR(100) NOT NULL,

    password VARCHAR(100) NOT NULL,

    role VARCHAR(20)
        CHECK (role IN ('Worker', 'Manager', 'Admin')),

    department_id INT
        REFERENCES departments(department_id),

    status VARCHAR(20) DEFAULT 'Active'
);


-- ============================================================
-- 40 WORKERS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES

-- Workers 1-10
('EMP-1001', 'Arjun Kumar', 'worker123', 'Worker', 1),
('EMP-1002', 'Ravi Sharma', 'worker123', 'Worker', 1),
('EMP-1003', 'Karthik Reddy', 'worker123', 'Worker', 2),
('EMP-1004', 'Suresh Naik', 'worker123', 'Worker', 2),
('EMP-1005', 'Mahesh Patel', 'worker123', 'Worker', 3),
('EMP-1006', 'Vikram Singh', 'worker123', 'Worker', 3),
('EMP-1007', 'Ramesh Rao', 'worker123', 'Worker', 4),
('EMP-1008', 'Ajay Verma', 'worker123', 'Worker', 4),
('EMP-1009', 'Ganesh Kumar', 'worker123', 'Worker', 5),
('EMP-1010', 'Sunil Reddy', 'worker123', 'Worker', 6),

-- Workers 11-20
('EMP-1011', 'Rahul Mehta', 'worker123', 'Worker', 1),
('EMP-1012', 'Manoj Kumar', 'worker123', 'Worker', 1),
('EMP-1013', 'Naveen Rao', 'worker123', 'Worker', 2),
('EMP-1014', 'Prakash Singh', 'worker123', 'Worker', 2),
('EMP-1015', 'Deepak Sharma', 'worker123', 'Worker', 3),
('EMP-1016', 'Rohit Patel', 'worker123', 'Worker', 3),
('EMP-1017', 'Sanjay Kumar', 'worker123', 'Worker', 4),
('EMP-1018', 'Vivek Reddy', 'worker123', 'Worker', 4),
('EMP-1019', 'Harish Naik', 'worker123', 'Worker', 5),
('EMP-1020', 'Tarun Verma', 'worker123', 'Worker', 6),

-- Workers 21-30
('EMP-1021', 'Abhishek Rao', 'worker123', 'Worker', 1),
('EMP-1022', 'Varun Sharma', 'worker123', 'Worker', 1),
('EMP-1023', 'Akash Kumar', 'worker123', 'Worker', 2),
('EMP-1024', 'Mohan Reddy', 'worker123', 'Worker', 2),
('EMP-1025', 'Rakesh Patel', 'worker123', 'Worker', 3),
('EMP-1026', 'Dinesh Singh', 'worker123', 'Worker', 3),
('EMP-1027', 'Yash Verma', 'worker123', 'Worker', 4),
('EMP-1028', 'Nikhil Rao', 'worker123', 'Worker', 4),
('EMP-1029', 'Lokesh Kumar', 'worker123', 'Worker', 5),
('EMP-1030', 'Chandan Reddy', 'worker123', 'Worker', 6),

-- Workers 31-40
('EMP-1031', 'Pavan Kumar', 'worker123', 'Worker', 1),
('EMP-1032', 'Sai Kiran', 'worker123', 'Worker', 1),
('EMP-1033', 'Surya Prakash', 'worker123', 'Worker', 2),
('EMP-1034', 'Madhav Rao', 'worker123', 'Worker', 2),
('EMP-1035', 'Teja Reddy', 'worker123', 'Worker', 3),
('EMP-1036', 'Raghu Sharma', 'worker123', 'Worker', 3),
('EMP-1037', 'Srinivas Naik', 'worker123', 'Worker', 4),
('EMP-1038', 'Vamsi Krishna', 'worker123', 'Worker', 4),
('EMP-1039', 'Naveen Kumar', 'worker123', 'Worker', 5),
('EMP-1040', 'Aditya Verma', 'worker123', 'Worker', 6);


-- ============================================================
-- 7 MANAGERS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES
('MGR-2001', 'Anil Kumar', 'manager123', 'Manager', 1),
('MGR-2002', 'Sneha Verma', 'manager123', 'Manager', 2),
('MGR-2003', 'Kiran Rao', 'manager123', 'Manager', 3),
('MGR-2004', 'Priyanka Sharma', 'manager123', 'Manager', 4),
('MGR-2005', 'Ramesh Patel', 'manager123', 'Manager', 5),
('MGR-2006', 'Swathi Reddy', 'manager123', 'Manager', 6),
('MGR-2007', 'Vijay Singh', 'manager123', 'Manager', 7);


-- ============================================================
-- 3 ADMINS
-- ============================================================

INSERT INTO users
    (employee_id, full_name, password, role, department_id)
VALUES
('ADM-3001', 'Rahul Sharma', 'admin123', 'Admin', 8),
('ADM-3002', 'Priya Reddy', 'admin123', 'Admin', 8),
('ADM-3003', 'Sandeep Kumar', 'admin123', 'Admin', 8);


-- ============================================================
-- 3. MACHINES
-- ============================================================

CREATE TABLE machines (
    machine_id SERIAL PRIMARY KEY,

    machine_name VARCHAR(100) NOT NULL,

    department_id INT
        REFERENCES departments(department_id),

    status VARCHAR(20)
);


INSERT INTO machines
    (machine_name, department_id, status)
VALUES
('Torque Bot', 1, 'Stopped'),
('Stamp Press', 2, 'Maintenance'),
('Spot Welder', 2, 'Running'),
('Auto Guided Vehicle', 5, 'Running'),
('Engine Assembly Robot', 1, 'Running'),
('Paint Robot', 2, 'Running'),
('CNC Machine', 1, 'Running'),
('Quality Inspection Bot', 3, 'Running'),
('Hydraulic Press', 1, 'Running'),
('Welding Robot', 2, 'Running'),
('Conveyor System', 5, 'Running'),
('Laser Cutting Machine', 1, 'Running'),
('Drilling Machine', 2, 'Maintenance'),
('Packaging Robot', 5, 'Running'),
('Material Handling AGV', 6, 'Running');


-- ============================================================
-- 4. ATTENDANCE
-- ============================================================

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,

    user_id INT
        REFERENCES users(user_id),

    attendance_date DATE,

    status VARCHAR(20)
);


INSERT INTO attendance
    (user_id, attendance_date, status)
SELECT
    user_id,
    CURRENT_DATE,
    CASE
        WHEN user_id % 10 = 0 THEN 'Absent'
        ELSE 'Present'
    END
FROM users;


-- ============================================================
-- 5. TASKS
-- ============================================================

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,

    title VARCHAR(100),

    assigned_to INT
        REFERENCES users(user_id),

    assigned_by INT
        REFERENCES users(user_id),

    status VARCHAR(20)
);


INSERT INTO tasks
    (title, assigned_to, assigned_by, status)
VALUES
('Machine Inspection', 1, 41, 'Completed'),
('Assembly Line Check', 2, 42, 'In Progress'),
('Quality Inspection', 5, 43, 'Pending'),
('Maintenance Inspection', 7, 44, 'In Progress'),
('Inventory Verification', 9, 45, 'Pending'),
('Safety Equipment Check', 12, 47, 'Completed'),
('Production Report', 15, 41, 'Pending'),
('Sensor Calibration', 18, 44, 'In Progress');


-- ============================================================
-- 6. MAINTENANCE REQUESTS
-- ============================================================

CREATE TABLE maintenance_requests (
    request_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    reported_by INT
        REFERENCES users(user_id),

    issue_description TEXT,

    status VARCHAR(20)
);


INSERT INTO maintenance_requests
    (machine_id, reported_by, issue_description, status)
VALUES
(1, 7, 'Torque calibration required', 'Open'),
(2, 13, 'Scheduled preventive maintenance', 'In Progress'),
(7, 21, 'CNC vibration above normal level', 'Open'),
(13, 31, 'Drilling machine requires inspection', 'Pending');


-- ============================================================
-- 7. PRODUCTION
-- ============================================================

CREATE TABLE production (
    production_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    production_date DATE,

    units_produced INT
);


INSERT INTO production
    (machine_id, production_date, units_produced)
SELECT
    machine_id,
    CURRENT_DATE,
    100 + (machine_id * 25)
FROM machines;


-- ============================================================
-- 8. SENSOR DATA
-- ============================================================

CREATE TABLE sensor_data (
    sensor_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    temperature NUMERIC(5,2),

    vibration NUMERIC(5,2),

    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO sensor_data
    (machine_id, temperature, vibration)
SELECT
    machine_id,
    35 + (machine_id * 0.5),
    1.0 + (machine_id * 0.1)
FROM machines;


-- ============================================================
-- 9. ALERTS
-- ============================================================

CREATE TABLE alerts (
    alert_id SERIAL PRIMARY KEY,

    machine_id INT
        REFERENCES machines(machine_id),

    alert_type VARCHAR(50),

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO alerts
    (machine_id, alert_type, message)
VALUES
(1, 'Machine Stopped', 'Torque Bot has stopped unexpectedly'),
(2, 'Maintenance', 'Stamp Press is under scheduled maintenance'),
(7, 'Vibration', 'CNC Machine vibration above normal level'),
(13, 'Maintenance', 'Drilling Machine requires inspection'),
(3, 'Production', 'Spot Welder operating normally');


-- ============================================================
-- VERIFICATION
-- ============================================================

-- Total users
SELECT COUNT(*) AS total_users
FROM users;


-- Users by role
SELECT
    role,
    COUNT(*) AS total
FROM users
GROUP BY role
ORDER BY
    CASE role
        WHEN 'Worker' THEN 1
        WHEN 'Manager' THEN 2
        WHEN 'Admin' THEN 3
    END;

-- All users
SELECT
    u.user_id,
    u.employee_id,
    u.full_name,
    u.role,
    d.department_name,
    u.status
FROM users u
JOIN departments d
    ON u.department_id = d.department_id
ORDER BY
    CASE u.role
        WHEN 'Worker' THEN 1
        WHEN 'Manager' THEN 2
        WHEN 'Admin' THEN 3
    END,
    u.user_id;

-- Total machines
SELECT COUNT(*) AS total_machines
FROM machines;


-- All machines
SELECT
    m.machine_id,
    m.machine_name,
    d.department_name,
    m.status
FROM machines m
JOIN departments d
    ON m.department_id = d.department_id
ORDER BY m.machine_id;





