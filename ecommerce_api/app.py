from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_PATH = 'ecommerce.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/customers', methods=['GET'])
def get_customers():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users LIMIT ? OFFSET ?', (limit, offset)).fetchall()
    conn.close()

    result = [dict(user) for user in users]
    return jsonify(result)

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (customer_id,)).fetchone()
    
    if user is None:
        return jsonify({'error': 'Customer not found'}), 404

    order_count = conn.execute('SELECT COUNT(*) FROM orders WHERE user_id = ?', (customer_id,)).fetchone()[0]
    conn.close()

    user_data = dict(user)
    user_data['order_count'] = order_count

    return jsonify(user_data)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
# Get all orders for a specific customer
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_orders_by_customer(customer_id):
    conn = get_db_connection()
    # Check if customer exists
    user = conn.execute('SELECT id FROM users WHERE id = ?', (customer_id,)).fetchone()
    if not user:
        conn.close()
        return jsonify({'error': 'Customer not found'}), 404

    orders = conn.execute('SELECT * FROM orders WHERE user_id = ?', (customer_id,)).fetchall()
    conn.close()

    orders_list = [dict(order) for order in orders]
    return jsonify(orders_list)


# Get specific order details
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    conn = get_db_connection()
    order = conn.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,)).fetchone()
    conn.close()

    if order is None:
        return jsonify({'error': 'Order not found'}), 404

    return jsonify(dict(order))


