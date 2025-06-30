import pandas as pd
Data={
    'Std1':
    {'Name':'Jyo',
    'branch':'Bioniformatics',
    'ID':10001,
    'Skills':["Python",'DSA','SQL','C']
    },
    'Std2':
    {'Name':'Venky',
    'branch':'Bioniformatics',
    'ID':10002,
    'Skills':["Python",'DSA','SQL','C']
    }
}
Data=pd.DataFrame(Data)
print(Data)