import os
from pathlib import Path

import pymysql

DIR = Path(os.path.dirname(os.path.dirname(__file__)))
print(DIR)
SAVE_DIR = DIR / 'process_data/'
INFER_DIR = DIR / 'inference_data/'
RESULT_DIR = DIR / 'prediction_result/'

TEST_USERS = r'data/test_dataset.csv'
USER_INFO = r'data/静态.xlsx'
RECORD_INFO = r'data/交易.xlsx'

USER_ID_COL = 'zhdh'
TARGET_COL = 'black_flag'
RECORD_CAT_COLS = ['jyqd', 'zydh', 'dfhh', 'dfzh']
UNAVAILABLE_COLS = [TARGET_COL, USER_ID_COL, 'khrq', 'khjgdh', 'jyts_Min', 'jyts_Max']

EPS = 1e-5
SEED = 2023
N_SPLITS = 2

try:
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="yupeihao05ab",
        database="locallog",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "SELECT version,a,b,c,d,e,f,g,h,i FROM localparameter"
    cursor.execute(sql, ())
    results = cursor.fetchall()
    print(results[0])
    conn.commit()
except Exception as e:
    print("删除失败：", e)
finally:
    cursor.close()
    conn.close()

a = results[0][1]
b = results[0][2]
c = results[0][3]
d = results[0][4]
e = results[0][5]
f = results[0][6]
g = results[0][7]
h = results[0][8]
i = results[0][9]
print(results)
XGB_PARAMS = {
    'n_estimators': a,
    'max_depth': b,
    'learning_rate': c,
    'booster': 'gbtree',
    'subsample': d,
    'colsample_bytree': e,
    'gamma': f,
    'reg_alpha': g,
    'reg_lambda': h,
    'max_leaves': i
}