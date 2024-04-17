import sqlite3
import hashlib
import os

try:
    # Connect to the existing database
    conn = sqlite3.connect('User_Data.db')

    # Create a cursor
    cursor = conn.cursor()

    # Begin transaction
    cursor.execute("BEGIN TRANSACTION;")

    # Insert 100 workers with hashed passwords
    for n in range(1000, 1100):
        password_data = str(n)
        
        # Generate value of salt
        salt = os.urandom(16)
        
        # generate a hash sha-256
        password_hash = hashlib.pbkdf2_hmac('sha256', password_data.encode('UTF-8'), salt, 100000)
        
        # convert password and salt to hexdecimal
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()
        
        # Combine Hashed password with salt
        password_set = f'{salt_hex}:{password_hash_hex}'
        
        # Generate a random cargo_id excluding 1
        cargo_id = n % 2 + 2
        
        # Insert worker into the funcionarios table
        cursor.execute("INSERT INTO funcionarios (nome, password, idade, morada, cargo_id) VALUES (?, ?, ?, ?, ?)",
                       (f"Worker {n}", password_set, n % 40 + 20, n, cargo_id))

    # Save with the commit
    conn.commit()

    # Close the connection
    conn.close()

    print('Saved Successfully!')

except sqlite3.Error as e:
    print('SQLite error:', e)
