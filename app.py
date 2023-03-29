from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'data'


# Define a function to execute MySQL queries
def run_query(query):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/air_quality', methods=['GET', 'POST'])
def air_quality():
    # Define the available areas
    areas = ['2023-03-07','2023-03-08','2023-03-22']

    # If a POST request is made, get the selected area
    if request.method == 'POST':
        selected_area = request.form['area']
    else:
        selected_area = areas[0]

    # Define the query to get the data for the selected area
    query = f"SELECT * FROM `{selected_area}`"

    # Execute the query and get the data
    data = run_query(query)

    # Render the template with the selected area and the data
    return render_template('air_quality.html', areas=areas, selected_area=selected_area, data=data)


if __name__ == '__main__':
    app.run(debug=True)
