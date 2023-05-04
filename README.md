# **Build ETL Pipeline**
This project provides a simple example of building an ETL (Extract, Transform, Load) pipeline using Python and SQL. The pipeline extracts data from a CSV file, applies some transformations to the data, and loads the transformed data into a SQLite database.

## Getting Started
To get started with this project, you'll need to do the following:

Clone the repository to your local machine
Install the required dependencies using pip (see requirements.txt)
Run the pipeline using the command python etl.py
Project Structure
The project is structured as follows:
```
data/: contains the input CSV file
db/: contains the output SQLite database
etl.py: the main ETL pipeline script
requirements.txt: list of Python dependencies required by the project
```
## Dependencies
This project has the following dependencies:
```
Python 3.x
pandas
SQLAlchemy
```

## Usage
To run the ETL pipeline, simply execute the following command:
```
python etl.py
```
This will extract data from the data/input.csv file, apply some transformations to it, and load the transformed data into the db/output.db SQLite database.

## License
This project is licensed under the MIT License - see the LICENSE file for details.






