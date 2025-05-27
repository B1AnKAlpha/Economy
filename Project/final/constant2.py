import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.dirname(__file__)))
print(DIR)
SAVE_DIR = DIR / 'process_data/'
INFER_DIR = DIR / 'inference_data/'
RESULT_DIR = DIR / 'prediction_result/'

TEST_USERS = r'D:\睿抗\模型\test_dataset.csv'
USER_INFO = r'D:\睿抗\模型\交易.xlsx'
RECORD_INFO = r'D:\睿抗\模型\静态.xlsx'

USER_ID_COL = 'zhdh'
TARGET_COL = 'black_flag'
RECORD_CAT_COLS = ['jyqd', 'zydh', 'dfhh', 'dfzh']
UNAVAILABLE_COLS = [TARGET_COL, USER_ID_COL, 'khrq', 'khjgdh', 'jyts_Min', 'jyts_Max']

EPS = 1e-5
SEED = 2023
N_SPLITS = 2

LGB_PARAMS = {
    'objective': 'binary',
    'n_estimators': 225,
    'learning_rate': 0.14695,
    'max_depth': 12,
    'num_leaves': 57,
    'min_child_samples': 20,
    'subsample': 0.9535,
    'colsample_bytree': 0.8874,
    'reg_alpha': 0.9488,
    'reg_lambda': 0.1515
}

XGB_PARAMS = {
    'n_estimators': 83,
    'max_depth': 8,
    'learning_rate': 0.15728,
    'booster': 'gbtree',
    'subsample': 0.60797,
    'colsample_bytree': 0.6248,
    'gamma': 0.1208,
    'reg_alpha': 0.2586,
    'reg_lambda': 0.1858,
    'max_leaves': 63
}

CGB_PARAMS = {
    'verbose': False,
    'iterations': 375,
    'learning_rate': 0.26668,
    'depth': 4,
    'l2_leaf_reg': 0.5274,
    'random_strength': 0.7282,
    'rsm': 0.7,
    'border_count': 32,
    'feature_border_type': 'Median'
}

RF_PARAMS = {
    'n_estimators': 280,
    'max_depth': 19,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'max_features': 'log2',
    'bootstrap': False,
    'random_state':42
}

SVM_PARAMS = {
    'C': 7.8057,
    'kernel': 'poly',
    'gamma': 'scale',
    'degree': 4,
    'probability': True
}

KNN_PARAMS = {
    'n_neighbors': 13,
    'weights': 'distance',
    'p': 3,
    'algorithm': 'auto',
    'leaf_size': 30
}

NB_PARAMS = {
    'var_smoothing': 2.2914e-11,
    'priors': None
}

HGBT_PARAMS = {
    'max_iter': 88,
    'learning_rate': 0.2899,
    'max_depth': 5,
    'min_samples_leaf': 18,
    'l2_regularization': 0.1452,
    'max_leaf_nodes': 15
}

GBDT_PARAMS = {
    'n_estimators': 383,
    'learning_rate': 0.2938,
    'max_depth': 9,
    'min_samples_split': 6,
    'min_samples_leaf': 10,
    'subsample': 0.6813,
    'random_state':42
}