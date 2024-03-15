"""
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The result format is in the following example.


"""


import pandas as pd

def remove_duplicate(Person):
    data = pd.DataFrame(Person, columns=['id','email'])
    rm_duplicate= data.drop_duplicates(subset=['email'], keep='first')
    return rm_duplicate

if __name__ == "__main__":
    print(remove_duplicate_email([
    [1, 'john@example.com'],
    [2, 'bob@example.com'],
    [3, 'john@example.com']
]))