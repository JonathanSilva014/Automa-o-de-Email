import sqlite3

try:
    # Connect to a database
    conn = sqlite3.connect('User_Data.db')

    # Create a cursor
    cursor = conn.cursor()

    # Command SQL for creating tables
    create_tables = '''
        CREATE TABLE IF NOT EXISTS cargo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cargo_nome VARCHAR(30) NOT NULL
        );
        
        -- Insert initial cargo values
        INSERT INTO cargo (cargo_nome) VALUES ('SuperUser');
        INSERT INTO cargo (cargo_nome) VALUES ('Admin');
        INSERT INTO cargo (cargo_nome) VALUES ('Gerente');

        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            password TEXT NOT NULL,
            idade INTEGER,
            morada VARCHAR(100),
            cargo_id INTEGER NOT NULL,
            FOREIGN KEY (cargo_id) REFERENCES cargo(id)
        );

        CREATE TABLE IF NOT EXISTS picagem_entrada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER NOT NULL,
            picagem_data DATE NOT NULL,
            hora_registro TIME NOT NULL,
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
        );

        CREATE TABLE IF NOT EXISTS picagem_saida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER NOT NULL,
            picagem_data DATE NOT NULL,
            hora_registro TIME NOT NULL,
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
        );

        CREATE TABLE IF NOT EXISTS picagem_entrada_pausa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER NOT NULL,
            picagem_data DATE NOT NULL,
            hora_registro TIME NOT NULL,
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
        );

        CREATE TABLE IF NOT EXISTS picagem_saida_pausa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER NOT NULL,
            picagem_data DATE NOT NULL,
            hora_registro TIME NOT NULL,
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
        );
    '''

    # Execute the SQL command with cursor
    cursor.executescript(create_tables)

    # Save with the commit
    conn.commit()

    # Close the connection
    conn.close()

    # Confirmation that the code has been successful at saving the data
    print('Saved Successfully!')

except sqlite3.Error as e:
    print('SQLite error:', e)
