# Advanced Inventory with CSV Persistence

##  Description

This project consists of an inventory management system developed in Python that allows users to manage products through CRUD operations (Create, Read, Update, Delete), as well as save and load data from CSV files.

The system is designed to preserve data between sessions, facilitate analysis, and allow easy sharing of information.

---

##  User Story 

* Save and load the inventory using CSV files to maintain data between sessions.
* Enable business statistics analysis.
* Apply lists, dictionaries, and tuples along with Python modules and functions.
* Build a modular system with data persistence and error handling.

---

##  Technologies Used

* Python
* `csv` module
* File handling
* Modular programming

---

##  Project Structure

```
  inventario/
│── app.py
│── servicios.py
│── archivos.py
│── data.csv
│── README.md
```

---

## ⚙️ Features

*  Add products
*  Display inventory
*  Search products
*  Update products
*  Delete products
*  Calculate statistics
*  Save inventory to CSV
*  Load inventory from CSV
*  Merge or overwrite data

---

##  Task Description

###  TASK 1: Flowchart

* Design the complete system flow (CRUD + persistence).
* Represent the main menu and subprocesses for saving and loading.
* Export the diagram in PNG or PDF format.

---

###  TASK 2: Data Structure and Modularization

* Use a list of dictionaries to represent the inventory:

```
{"nombre": str, "precio": float, "cantidad": int}
```

* Split the code into modules:

  * `app.py` (main controller)
  * `servicios.py` (business logic)

* Implement CRUD and statistics functions.

* Use docstrings and comments.

---

###  TASK 3: Inventory Statistics

* Calculate:

  * Total units
  * Total value
  * Most expensive product
  * Product with highest stock

* Display results clearly.

* Optional use of lambda functions for calculations.

---

###  TASK 4: Save CSV

* Create the function `guardar_csv()`.
* Validate that the inventory is not empty.
* Write to file with header:

```
nombre,precio,cantidad
```

* Handle errors using `try/except`.

---

###  TASK 5: Load CSV

* Implement the function `cargar_csv()`.

* Validate:

  * Correct header
  * Number of columns
  * Data types

* Handle errors:

  * File not found
  * Encoding issues
  * Invalid data

* Options:

  * Overwrite inventory
  * Merge existing data

---

###  TASK 6: Final Menu

* Implement an interactive menu with options:

  1. Add
  2. Show
  3. Search
  4. Update
  5. Delete
  6. Statistics
  7. Save CSV
  8. Load CSV
  9. Exit

* Validations:

  * Correct numeric input
  * Non-negative values

* Use a `while` loop to keep the program running.

---

##  Concepts Applied

* Variables
* Lists
* Dictionaries
* Tuples
* Functions
* Modules
* CSV file handling
* Data validation
* Error handling (`try/except`)
* Structured programming

---

##  How to Run the Project

1. Clone the repository:

```
git clone URL_DEL_REPOSITORY
```

2. Navigate to the folder:

```
cd inventario
```

3. Run the program:

```
python app.py
```

---

##  Example Usage

```
--- INVENTORY MENU ---
1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit
```

---

##  Acceptance Criteria

*  The inventory can be saved and loaded using CSV files.
*  The system allows overwriting or merging data.
*  Proper error handling without crashing the program.
*  Use of a list of dictionaries as the main data structure.
*  Modular code (app.py, servicios.py, archivos.py).
*  Correct calculation of statistics.
*  Functional and validated menu.
*  Clean, readable, and well-documented code.
*  Delivery of the complete system flowchart (PNG/PDF).

---

##  Author

* Software Development Student
