## Music App Data Collection Tables (FastAPI + PostgreSQL)

This repository provides a set of data collection tables for a music app implemented using FastAPI with PostgreSQL as the database backend. It was started for my [music-web-project](https://github.com/Klhall7/music-web-project) and was coded with Python 3.12

### Disclaimer Note

Please note that this collects data for the purpose of enhancing user experience and improving app functionality. If it is included on a deployed app users should be informed about the data collection practices and how their data is used.
Ensure compliance with relevant privacy regulations with a disclaimer prominently displayed within the app.

### Usage

1. **Database Setup**:
   - I used Postico 2 to view the created tables, align the models accordingly, and execute queries as necessary.
   - Ensure that the PostgreSQL server is running and has the required database created.

2. **API Documentation**:
   - FastAPI comes with Swagger documentation by default.
   - All CRUD routes are testable via: [http://localhost:8000/docs](http://localhost:8000/docs).

3. **Virtual Environment**:
   - The virtual environment located in `env/` is hidden from the GitHub version for cleanliness.
   - Install required dependencies using `requirements.txt`.
   - Activate the initialized virtual environment before running the application and deactivate it as needed.

### Notes
- All ID **sequences** in the database should start at 1 for consistency.

-By adding the **to_dict method** to each model class, you can easily convert instances of these classes to dictionaries, which can be useful for various operations, including serialization and logging.
