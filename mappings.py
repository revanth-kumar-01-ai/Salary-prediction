# work class 
target_mapping = {
    'State-gov': 'Government',
    'Self-emp-not-inc': 'Self-Employed',
    'Private': 'Private Sector',
    'Federal-gov': 'Government',
    'Local-gov': 'Government',
    'Self-emp-inc': 'Self-Employed',
}

# education 
education_mapping = {
    'Preschool': 'No Education',
    '1st-4th': 'Primary',
    '5th-6th': 'Primary',
    '7th-8th': 'Middle School',
    '9th': 'Middle School',
    '10th': 'High School',
    '11th': 'High School',
    '12th': 'High School',
    'HS-grad': 'High School Graduate',
    'Some-college': 'College',
    'Assoc-voc': 'Associate Degree',
    'Assoc-acdm': 'Associate Degree',
    'Bachelors': 'Bachelor’s Degree',
    'Masters': 'Master’s Degree',
    'Doctorate': 'Doctorate',
    'Prof-school': 'Professional Degree'
}

# marital 
marital_mapping = {
    'Married-civ-spouse': 'Married',
    'Married-AF-spouse': 'Married',
    'Married-spouse-absent': 'Married but Separated',
    'Never-married': 'Single',
    'Divorced': 'Divorced',
    'Separated': 'Separated', 
    'Widowed': 'Widowed'
}

# Occupation 
occupation_mapping = {
    'Adm-clerical': 'Clerical',
    'Exec-managerial': 'Management',
    'Handlers-cleaners': 'Labor',
    'Prof-specialty': 'Professional',
    'Other-service': 'Service',
    'Sales': 'Sales',
    'Transport-moving': 'Transportation',
    'Farming-fishing': 'Agriculture',
    'Machine-op-inspct': 'Manufacturing',
    'Tech-support': 'Technical',
    'Craft-repair': 'Skilled Trades',
    'Protective-serv': 'Security',
    'Armed-Forces': 'Military',
    'Priv-house-serv': 'Domestic Work'
}


# relationship 
relationship_mapping = {
    'Husband': 'Spouse',
    'Wife': 'Spouse',        
    'Own-child': 'Child',
    'Not-in-family': 'Independent',
    'Unmarried': 'Single',
    'Other-relative': 'Extended Family'
}

# sex mapping
sex_mapping = {
    'Male':'M', 
    'Female':'F'
}

# salary 
salary_mapping = {
    '<=50K':0, # less
    '>50K':1 # greater 
}
