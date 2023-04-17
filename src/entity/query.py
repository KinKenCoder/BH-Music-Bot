class Query:
    """
        Entity to query the database in a transaction
    """
    def __init__(self, sql: str, *params):
        self.sql = sql
        self.params = params
        self.success = False
        self.response = None
