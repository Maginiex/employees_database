import sqlite3

connect = sqlite3.connect('employees.db')
cursor = connect.cursor()

connect.commit()

def search():
    cursor.execute("SELECT * FROM employees")
    all_results = cursor.fetchall()
    print(all_results)

def search2():
    cursor.execute("SELECT employee FROM employees WHERE employee LIKE 'David'")
    all_results2 = cursor.fetchall()
    print(all_results2)

def search3():
    cursor.execute("SELECT employee, job_id FROM employees WHERE job_id LIKE 'IT_PROG'")
    all_results3 = cursor.fetchall()
    print(all_results3)

def search4():
    cursor.execute("SELECT employee,department_id , salary FROM employees WHERE department_id = 50 AND salary > 4000")
    all_results4 = cursor.fetchall()
    print(all_results4)


def search5():
    cursor.execute("SELECT employee FROM employees WHERE employee LIKE '%a'")
    all_results5 = cursor.fetchall()
    print(all_results5)


def search6():
    cursor.execute("SELECT employee FROM employees WHERE employee LIKE '%n%n%'")
    all_results6 = cursor.fetchall()
    print(all_results6)


def search7():
    cursor.execute("SELECT max(salary), min(salary), max(date_job), min(date_job) FROM employees GROUP BY department_id ORDER BY count (*) desc")
    all_results7 = cursor.fetchall()
    print(all_results7)


def search8():
    cursor.execute("SELECT manager_id FROM employees GROUP BY manager_id HAVING COUNT (*) > 5 AND SUM(salary) > 50000")
    all_results8 = cursor.fetchall()
    print(all_results8)



search()
search2()
search3()
search4()
search5()
search6()
search7()
search8()