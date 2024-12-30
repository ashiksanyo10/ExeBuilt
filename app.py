from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'gti_database'
}

# Check duplicate endpoint
@app.route('/check_duplicate', methods=['POST'])
def check_duplicate():
    data = request.json
    gti = data.get('gti')
    task_id = data.get('task_id')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Check for duplicate
        cursor.execute("SELECT * FROM content_table WHERE gti = %s", (gti,))
        result = cursor.fetchone()

        if result:
            # Log duplicate in `duplicate_log`
            cursor.execute(
                "INSERT INTO duplicate_log (duplicate_gti, old_task_id, new_task_id) VALUES (%s, %s, %s)",
                (gti, result['task_id'], task_id)
            )
            conn.commit()
            return jsonify({"status": "duplicate", "message": "Duplicate GTI logged"}), 200
        else:
            # Insert new GTI and Task ID
            cursor.execute(
                "INSERT INTO content_table (gti, task_id) VALUES (%s, %s)",
                (gti, task_id)
            )
            conn.commit()
            return jsonify({"status": "success", "message": "New GTI added"}), 200
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
