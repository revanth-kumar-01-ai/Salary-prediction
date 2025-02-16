import mappings
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class FeatureMapping:
    @staticmethod
    def drop_without_pay(df):
        df = df.copy()
        df = df[df['workclass'].str.strip() != 'Without-pay']
        return df
    
    @staticmethod
    def feature_values_replace(df):
        df = df.copy()
        df['workclass'] = df['workclass'].str.strip().replace(mappings.target_mapping)
        df['education'] = df['education'].str.strip().replace(mappings.education_mapping)
        df['maritalstatus'] = df['maritalstatus'].str.strip().replace(mappings.marital_mapping)
        df['occupation'] = df['occupation'].str.strip().replace(mappings.occupation_mapping)
        df['relationship'] = df['relationship'].str.strip().replace(mappings.relationship_mapping)
        df['sex'] = df['sex'].str.strip().replace(mappings.sex_mapping)
        df['Salary'] = df['Salary'].str.strip().replace(mappings.salary_mapping)
        return df
    
    @staticmethod
    def drop_columns(df):
        df = df.copy()
        df = df.drop(columns=['native', 'race']) 
        return df
    
