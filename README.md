# Grocery Store Manager

A CLI application to manage a grocery store’s products, customers, sales, and sale items using Python, SQLAlchemy ORM, and Alembic.

## Setup

1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pipenv install`
3. Enter the environment: `pipenv shell`
4. Apply migrations: `alembic upgrade head`
5. Run the CLI: `python lib/cli.py`

## Usage

- **Products**: Add, delete, view, find by name, see sale items.
- **Customers**: Add, delete, view, find by name, see sales.
- **Sales**: Create, delete, view, see items.
- **Sale Items**: Add, delete, view, tie to sales and products.

## Files

- **lib/cli.py**: Main CLI script with menus and user interaction.
- **lib/models/**: Contains `product.py`, `customer.py`, `sale.py`, `sale_item.py` for database models.
- **lib/helpers.py**: Utility functions like `exit_program()`.
- **lib/migrations/**: Alembic migrations for database schema.
