CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT ExISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
)

"""

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

SELECT_TASKS = "SELECT id,  task, completed FROM tasks"

SELECT_TASKS_COMPLETED = "SELECT id, task, completed FROM tasks WHERE completed = 1"

SELECT_TASKS_UNCOMPLETED = "SELECT id, task, completed FROM tasks WHERE completed = 0"

UPDATE_TASKS = "UPDATE tasks SET task = 7 WHERE id = ?"

DELETE_TASK = "DELETE  FROM tasks WHERE id = ?"