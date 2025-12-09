<p align="center">
  <h1> PYTHON + SQL LOW LEVEL DESIGN</h1>

This repository contains multiple Python projects related to banking, movie management, university systems, and more. Each subdirectory represents a separate application with its own structure and components.

## Projects

### Banking System
- **Location:** `banking/`
- **Description:** A banking application with customer, account, and transaction management.
- **Key Files:**
  - `banking/main.py` - Entry point
  - `banking/service/` - Business logic for customers, accounts, and transactions
  - `banking/model/` - Data models for the application
  - `banking/db/` - Database connection and operations

### LLD (Low-Level Design) Examples
- **Location:** `lld/`
- **Description:** Various low-level design implementations for different domains (hotel, gym, university, etc.).
- **Key Files:**
  - `lld/db_test.py` - Database testing example
  - `lld/employee.py`, `lld/gym.py`, etc. - Domain-specific design implementations

### Movie Management System
- **Location:** `movie/`
- **Description:** A movie database application with casting, director, and movie management.
- **Key Files:**
  - `movie/main.py` - Entry point
  - `movie/service/` - Business logic for movie-related operations
  - `movie/models/` - Data models for movies, directors, and casting

### University System
- **Location:** `university_system/`
- **Description:** A university management system with student, course, and grade tracking.
- **Key Files:**
  - `university_system/main.py` - Entry point
  - `university_system/services/` - Business logic for students, courses, and grades
  - `university_system/models/` - Data models for the university system

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VSD10/py_sql_lld.git
   cd py_sql_lld
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run applications:**
   - Navigate to the project directory (e.g., `banking/`)
   - Execute the main file (e.g., `python main.py`)

## Contributing

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make your changes and test them
4. Commit your changes
5. Push to your fork
6. Create a pull request

</p>

