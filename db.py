import sqlite3

#Connection sqllite3
conn = sqlite3.connect('ma.sqlite3')

#Cursor = execute sqlite3
c = conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS ma_list(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    service_name TEXT,
                    year TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    partner TEXT,
                    contact TEXT)""")

def insert_ma_list(service_name,year,start_date,end_date,partner,contact):
    with conn:
        command = 'INSERT INTO ma_list VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(None,service_name,year,start_date,end_date,partner,contact))
    conn.commit()

# data = [
#     [1, "Fortigate 100E", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [2, "Kaspersky Endpoint security for Business - Select", "1 Year", "2024-06-01", "2025-05-31", "Tech Titen Distrivution CO., LTD.", "supportdept-th@tech-titan.com"],
#     [3, "Microsoft 365 Family", "1 Year", "2024-07-01", "2025-06-31", "Microsoft Store", "https://www.microsoft.com/"],
#     [4, "Kaspersky Standard 5 Devices", "2 Year", "2024-04-18", "2026-04-17", "Kasoshopping", "www.kasoshopping.com"],
#     [5, "Kaspersky Standard 1 Device", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [6, "PowerEdge T150 Tower Server", "1 Year", "2024-06-01", "2025-05-31", "Kasoshopping", "www.kasoshopping.com"],
#     [7, "Microsoft Office 365 Family", "1 Year", "2024-07-01", "2025-06-31", "Microsoft Store", "https://www.microsoft.com/"],
#     [8, "Internet Lease line", "1 Year", "2024-04-18", "2025-04-17", "United Information Highway", "cc_support@uih.co.th"],
#     [9, "FortiAnalyzer Cloud Service", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [10, "APC Smart-UPS 2200VA LCD RM 2U 230V", "1 Year", "2024-06-01", "2025-05-31", "EKKARAJ CO., LTD.", "ONLINESALES@EKKARAJ.CO.TH"],
#     [11, "Fortigate 100E", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [12, "Kaspersky Endpoint security for Business - Select", "1 Year", "2024-06-01", "2025-05-31", "Tech Titen Distrivution CO., LTD.", "supportdept-th@tech-titan.com"],
#     [13, "Microsoft 365 Family", "1 Year", "2024-07-01", "2025-06-31", "Microsoft Store", "https://www.microsoft.com/"],
#     [14, "Kaspersky Standard 5 Devices", "2 Year", "2024-04-18", "2026-04-17", "Kasoshopping", "www.kasoshopping.com"],
#     [15, "Kaspersky Standard 1 Device", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [16, "PowerEdge T150 Tower Server", "1 Year", "2024-06-01", "2025-05-31", "Kasoshopping", "www.kasoshopping.com"],
#     [17, "Microsoft Office 365 Family", "1 Year", "2024-07-01", "2025-06-31", "Microsoft Store", "https://www.microsoft.com/"],
#     [18, "Internet Lease line", "1 Year", "2024-04-18", "2025-04-17", "United Information Highway", "cc_support@uih.co.th"],
#     [19, "FortiAnalyzer Cloud Service", "1 Year", "2024-04-01", "2025-03-31", "iPartner Co., Ltd", "ipartner@ipartner.co.th"],
#     [20, "APC Smart-UPS 2200VA LCD RM 2U 230V", "1 Year", "2024-06-01", "2025-05-31", "EKKARAJ CO., LTD.", "ONLINESALES@EKKARAJ.CO.TH"]
# ]
    
# for i in data:
#     insert_ma_list(f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}',f'{i[6]}')

def search_ma_list(s_name):
    with conn:
        command = f"SELECT * FROM ma_list Where service_name like '{s_name}%'"
        c.execute(command)
        result = c.fetchall()
        # print(result)
    return result

# result = search_ma_list("kas")
# print(result)

def view_ma_list():
    with conn:
        command = 'SELECT * FROM ma_list'
        c.execute(command)
        result = c.fetchall()
        # print(result)
    return result

# result = view_ma_list()
# print(result)

def update_ma_list(id,field,newvalue):
    with conn:
        command = 'UPDATE ma_list SET {} = (?) WHERE id=(?)'.format(field)
        c.execute(command,(newvalue,id))
    conn.commit()

# update_ma_list(1,'service_name','APC UPS2200')
    
def delete_ma_list(id):
    with conn:
        command = 'DELETE FROM ma_list WHERE id=(?)'
        c.execute(command,([id]))
    conn.commit()

# delete_ma_list(1)