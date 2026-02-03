# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import *  # noqa: F403, F401
import pandas as pd

# Define a subclass of QueryBase
# called Employee


class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution

    def names(self):

        # Query 3
        # Write an SQL query
        # that selects two columns
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        query = """
        SELECT first_name || ' ' || last_name AS full_name,
               employee_id
        FROM employee
        """
        return self.query(query)

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution

    def username(self, id):

        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        query = f"""
        SELECT first_name || ' ' || last_name AS full_name
        FROM employee
        WHERE employee_id = {id}
        """
        return self.query(query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    # YOUR CODE HERE

    def model_data(self, id):
        query = f"""
        SELECT
            COALESCE(SUM(positive_events), 0) as positive_events,
            COALESCE(SUM(negative_events), 0) as negative_events
        FROM employee_events
        WHERE employee_id = {id}
        """
        result = self.query(query)

        # Convert to DataFrame
        if result:
            return pd.DataFrame(
                result,
                columns=[
                    'positive_events',
                    'negative_events'])
        else:
            # Return empty DataFrame with correct columns if no results
            return pd.DataFrame(columns=['positive_events', 'negative_events'])
