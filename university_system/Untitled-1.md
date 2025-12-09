
# ⭐⭐ **LEVEL 4 — UNIVERSITY COURSE REGISTRATION SYSTEM (FULL SPEC)**

*(Copy everything below from here to the end — this is your full reference.)*

---

# 🎓 **UNIVERSITY COURSE REGISTRATION SYSTEM — FULL REQUIREMENTS (LEVEL 4)**

## 📌 SYSTEM FEATURES

This system manages:

* Students
* Courses
* Enrollments
* Assignment Marks
* Grade Calculation
* GPA Calculation
* Course Capacity Limits
* Duplicate Enrollment Prevention

---

# 🗄 DATABASE NAME

```
university_db
```

---

# 🧱 **TABLE 1: students**

```
student_id     INT PRIMARY KEY AUTO_INCREMENT
name           VARCHAR(50)
email          VARCHAR(50)
year           INT        -- 1 to 4
major          VARCHAR(50)
```

---
                                                    s.name,
    c.course_name,
    c.department,
    e.status,
    e.enroll_date
# 🧱 **TABLE 2: courses**

```
course_id      INT PRIMARY KEY AUTO_INCREMENT
course_name    VARCHAR(100)
department     VARCHAR(50)
credits        INT     -- 1 to 4
capacity       INT     -- max allowed students
```

---

# 🧱 **TABLE 3: enrollments**

```
enroll_id      INT PRIMARY KEY AUTO_INCREMENT
student_id     INT
course_id      INT
enroll_date    DATE
status         VARCHAR(20)    -- Active / Completed / Dropped
```

---

# 🧱 **TABLE 4: grades**

```
grade_id        INT PRIMARY KEY AUTO_INCREMENT
enroll_id       INT
assignment_name VARCHAR(100)
marks           INT       -- 0 to 100
grade           VARCHAR(2)   -- A / B / C / D / F
```

---

# ⭐ **MAIN MENU (PYTHON)**

```
1. Add Student
2. Add Course
3. Enroll Student in Course
4. Add Assignment Marks
5. Calculate GPA for a Student
6. View Student Enrollments (JOIN)
7. View Course Roster
8. Drop a Course
9. Exit
```

---

# ⭐ DETAILED LOGIC

---

## 1️⃣ Add Student

Inputs:

* name
* email
* year
* major

Insert into `students`.

---

## 2️⃣ Add Course

Inputs:

* course_name
* department
* credits
* capacity

Insert into `courses`.

---

## 3️⃣ ENROLL STUDENT (ADVANCED LOGIC)

### MUST CHECK:

* Student exists
* Course exists
* Course capacity limit not exceeded
* Student not already enrolled in the same course

### Capacity check:

```sql
SELECT COUNT(*) 
FROM enrollments 
WHERE course_id=? AND status='Active';
```

If count >= capacity → reject.

### Insert:

```sql
INSERT INTO enrollments(student_id, course_id, enroll_date, status)
VALUES (?, ?, CURDATE(), 'Active');
```

---

## 4️⃣ ADD ASSIGNMENT MARKS

### MUST CHECK:

* enrollment exists
* marks 0–100
* grade must be auto-calculated

### Grade rules:

```
90–100 → A
80–89  → B
70–79  → C
60–69  → D
<60    → F
```

### Insert:

```sql
INSERT INTO grades(enroll_id, assignment_name, marks, grade)
VALUES (?, ?, ?, ?);
```

---

## 5️⃣ GPA CALCULATION (HARD FEATURE)

### Steps:

1. Get all enrollments for student.
2. Get all grades for each enrollment.
3. Convert grade to points:

```
A = 4
B = 3
C = 2
D = 1
F = 0
```

4. Weighted GPA calculation:

```
GPA = SUM(grade_points × course_credits)  / SUM(course_credits)
```

Round to 2 decimals.

---

## 6️⃣ VIEW STUDENT ENROLLMENTS (JOIN)

```sql
SELECT 
    s.name,
    c.course_name,
    c.department,
    e.status,
    e.enroll_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE s.student_id = ?;
```

---

## 7️⃣ VIEW COURSE ROSTER (STUDENTS IN A COURSE)

```sql
SELECT 
    s.student_id,
    s.name,
    s.year,
    s.major
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
WHERE e.course_id = ? AND e.status='Active';
```

---

## 8️⃣ DROP A COURSE

Must only drop if enrollment is Active.

```sql
UPDATE enrollments 
SET status='Dropped'
WHERE enroll_id=? AND status='Active';
```

If status = Completed → do NOT allow dropping.

---

# 🧪 TEST CASES (COMPANY-LEVEL)

| No | Test Case                          | Expected               |
| -- | ---------------------------------- | ---------------------- |
| 1  | Enroll student in a course         | Success                |
| 2  | Enroll same student again          | Reject                 |
| 3  | Enroll more students than capacity | Reject extra           |
| 4  | Add assignment marks               | Success                |
| 5  | Add marks >100 or <0               | Reject                 |
| 6  | Calculate GPA for a student        | Correct result         |
| 7  | Drop a course                      | Status becomes Dropped |
| 8  | Drop completed course              | Reject                 |
| 9  | View student enrollments           | Shows JOIN results     |
| 10 | View course roster                 | Shows active students  |

---


