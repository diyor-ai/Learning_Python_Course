company = {
    "IT": {
        "Ali": {
            "salary": 1200,
            "projects": {
                "AI": 90,
                "Web": 80
            }
        },
        "Sami": {
            "salary": 1500,
            "projects": {
                "AI": 95,
                "ML": 85
            }
        }
    },
    "Marketing": {
        "Vali": {
            "salary": 1000,
            "projects": {
                "SEO": 70,
                "Ads": 75
            }
        }
    }
}

"""
IT
Employees: 2
Total salary: 2700
Average salary: 1350
----------------

Marketing
Employees: 1
Total salary: 1000
Average salary: 1000
----------------
"""
company_info = {}

for company_part, company_data in company.items():
    company_info[company_part] = {
        "employees": 0,
        "total_salary": 0,
        "average_salary": 0
    }
    for employee in company_data.values():
        company_info[company_part]["employees"] += 1
        company_info[company_part]["total_salary"] += employee['salary']
    company_info[company_part]["average_salary"] = company_info[company_part]["total_salary"] / \
                                                   company_info[company_part]["employees"]

for company_part, company_datas in company_info.items():
    print(company_part)
    print(f"Employees: {company_datas['employees']}")
    print(f"Total salary: {company_datas['total_salary']}")
    print(f"Average salary: {company_datas['average_salary']}")
    print("__" * 8)

"""
Top performer: Sami (90.0)
"""

top_performe = []

for company in company.values():
    for employee_name, employee_data in company.items():
        avarage = sum(employee_data['projects'].values()) / len(employee_data['projects'])
        top_performe.append([employee_name, avarage])

top_performer = top_performe[0]

for employee in top_performe:
    if employee[1] > top_performer[1]:
        top_performer = employee
print(f"Top performer: {top_performer[0]} ({top_performer[1]})")


