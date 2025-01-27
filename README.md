Python Project - Department and Employee Matching
This script performs a department and employee matching algorithm. The goal is to match departments and employees based on their preferences, using a simplified version of the Gale-Shapley algorithm.

Overview
The script uses two lists of preferences:

Department Preference List: A list that holds the preferences of each department for the employees.
Employee Preference List: A list that holds the preferences of each employee for the departments.
The script then tries to match each employee to a department, and if a department is already matched with an employee, it checks if the new employee is preferred over the current match.

Features
Department Preference List: A list of departments and their preferences for employees.
Employee Preference List: A list of employees and their preferences for departments.
Stable Matching: The algorithm ensures that all matches are stable. This means no department or employee can be matched with someone they prefer more than their current match.
Input Format
The input is hardcoded as two lists of preferences:

Department Preference List (D): A list where each department ranks all the employees.
Employee Preference List (P): A list where each employee ranks all the departments.
Example of a department preference list:

python
Copy
Edit
D = [
    [2, 1, 4, 5, 3],
    [4, 2, 1, 3, 5],
    [2, 5, 3, 4, 1],
    [1, 4, 3, 2, 5],
    [2, 4, 1, 5, 3]
]
Example of an employee preference list:

python
Copy
Edit
P = [
    [5, 1, 2, 4, 3],
    [3, 2, 4, 1, 5],
    [2, 3, 4, 5, 1],
    [1, 5, 4, 3, 2],
    [4, 2, 5, 3, 1]
]
How to Run
Clone the repository or download the script.

Install Python 3.x on your system if it's not installed already.

Run the script using the command:

bash
Copy
Edit
python runSomething.py
The script will output the final matching between departments and employees, indicating which employee was assigned to which department.

Example Output
bash
Copy
Edit
Result is:-
HR : Adam
CRM : Diane
Admin : Emily
Research : Clare
Development : Bob
Code Explanation
Department and Employee Preference Lists:
Two lists (D and P) hold the preferences of the departments and employees.
Matching Process:
The script matches each employee to a department based on their preferences.
If a department is already matched with another employee, the department will choose the employee they prefer based on their own preference list.
Final Matches:
The final matched pairs are printed out, showing which employee has been matched with which department.
Contributing
If you want to contribute to this project, feel free to fork the repository and create a pull request. Any improvements or suggestions are welcome!

License
This project is open-source and available under the MIT License.
