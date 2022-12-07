from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def fetch_data(cust_id="", update_data="", trans_id="", add_data=""):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pr@navi11",
        database='super_mart'
    )
    cursor = mydb.cursor()

    # get all the employee details
    if len(trans_id) > 1:
        query = """
                SELECT Cus.*, O.*
                FROM super_mart.customers Cus
                Join super_mart.locations L
                on Cus.cust_id = L.cust_id and L.trans_id={id}
                Join super_mart.Orders O
                on L.trans_id = O.trans_id and L.trans_id={id}
                """
        main_query = query.format(id=int(trans_id))
        cursor.execute(main_query)
        sequence = cursor.column_names
        main_data = []
        for result in cursor:
            main_data.append(result)
        return (sequence, tuple(main_data))

    # get the employee data who deals with the project greater than the income given
    if len(add_data) > 1:
        query = """INSERT INTO customers (cust_id,  cust_name, contact_no, payment_method) 
        VALUES (%s, %s, %s, %s)
        """
        record = (int(add_data[0]), add_data[1], int(add_data[2]), add_data[3])
        cursor.execute(query, record)
        mydb.commit()
        query = """
        select * from customers
        """
        cursor.execute(query)
        sequence = cursor.column_names
        main_data = []
        for result in cursor:
            main_data.append(result)
        return (sequence, tuple(main_data))

    if len(cust_id) > 1:
        query = """
        DELETE FROM Customers WHERE cust_id='{id}';
        """
        main_query = query.format(id=int(cust_id))
        cursor.execute(main_query)
        mydb.commit()
        query = """
        select * from customers
        """
        cursor.execute(query)
        sequence = cursor.column_names
        main_data = []
        for result in cursor:
            main_data.append(result)
        return (sequence, tuple(main_data))

    if len(update_data) > 1:
        query = """ UPDATE customers
        SET contact_no = %s 
        Where cust_id = %s
        """

        record = (int(update_data[1]), int(update_data[0]))

        cursor.execute(query, record)

        mydb.commit()

        query = """
        select * from customers
        """
        cursor.execute(query)
        sequence = cursor.column_names
        main_data = []
        for result in cursor:
            main_data.append(result)
        return (sequence, tuple(main_data))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cust_id = request.form['cust_id']
        update_data = list(request.form['update_data'].split(","))
        trans_id = request.form['trans_id']
        add_data = list(request.form['add'].split(","))
        headings, data = fetch_data(cust_id, update_data, trans_id, add_data)
        return render_template("index.html", headings=headings, data=data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)