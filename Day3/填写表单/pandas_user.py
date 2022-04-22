import pandas as pd
excel_path = r'E:\Auto_Pro\填写表单\用户表.xlsx'
users = pd.read_excel(excel_path)
print(users.shape)
