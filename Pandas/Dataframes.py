import pandas as pd
Data={
    'Std1':
    {'Name':'Jyo',
    'Branch':'Bioinformatics',
    'ID':15236,
    'Skills':['python','sql']
    },
    'Std2':
    {'Name':'Varun',
        'Branch':'Bioinformatics',
        'ID':15237,
        'Skills':['python','sql','java']
    }
}
Data=pd.DataFrame(Data)
print(Data)