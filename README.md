# Advanced Inventory System with CSV Persistence

A Python-based command-line application designed to manage product inventory using CRUD operations and file persistence. This system allows users to store, retrieve, and analyze inventory data across sessions using CSV files.

## Features

* **Product Management**: Add, update, search, and delete products with validation.
* **Inventory Display**: View all registered products in a clear format.
* **Statistics Calculation**:

  * Total units in inventory
  * Total inventory value
  * Most expensive product
  * Product with highest stock
* **CSV Persistence**:

  * Save inventory data to CSV files
  * Load inventory from CSV files
  * Option to overwrite or merge existing data
* **Error Handling**:

  * Prevents crashes due to invalid input or file issues
  * Handles missing files, invalid formats, and corrupted data

## Project Structure

The project is modularized into several Python files:

* `app.py`: The main entry point containing the menu and user interaction logic.
* `servicios.py`: Contains all business logic including CRUD operations and statistics.
* `archivos.py`: Handles file operations such as saving and loading CSV data.
* `data.csv`: Stores persistent inventory data.
* `README.md`: Project documentation.

## Requirements

* Python 

## How to Run

1. Clone or download the project files into the same directory.
2. Open your terminal or command prompt.
3. Run the application using the following command:

```bash
python app.py
```

## Data Structure

The inventory is stored as a list of dictionaries:

```python
{"nombre": str, "precio": float, "cantidad": int}
```

## Functionality Overview

The system includes the following operations:

1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. View statistics
7. Save inventory to CSV
8. Load inventory from CSV
9. Exit

## CSV Format

The system uses the following structure for CSV files:

```
nombre,precio,cantidad
```

## Acceptance Criteria

* The system successfully saves and loads inventory data using CSV files.
* Users can choose to overwrite or merge data when loading files.
* Invalid rows in CSV files are ignored and reported.
* The application handles errors without crashing.
* The inventory is managed using a list of dictionaries.
* The code is modular, readable, and well-structured.
* All features are accessible through a functional menu system.

## Author

* Software Development Student
