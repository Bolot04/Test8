# CREATE_BUY = """
#     CREATE TABLE IF NOT EXISTS lists (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         list TEXT NOT NULL,
#         completed INTEGER DAFAULT 0
# )
# """
CREATE_BUY = """
    CREATE TABLE IF NOT EXISTS lists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        list  TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
"""

INSERT_LISTS = "INSERT INTO lists (list) VALUES (?)"

SELECT_LISTS = 'SELECT id, list, completed FROM lists'

SELECT_LISTS_COMPLETED = 'SELECT id, list, completed FROM lists WHERE completed == 1'

SELECT_LISTS_UNCOMPLETED = 'SELECT id, list, completed FROM lists WHERE completed == 0'

UPDATE_LISTS = 'UPDATE lists SET list = ? WHERE id = ?'

DELETED_LISTS = "DELETED FROM lists WHERE id = ?"