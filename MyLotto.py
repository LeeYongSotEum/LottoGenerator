# import numpy as np
# import pandas as pd
from flask import render_template, Flask, request
app = Flask(__name__)


@app.route('/')
def student():
    return render_template('sample.html')


@app.route('/templates', methods=['POST', 'GET'])
def templete_test():
    if request.method == 'POST':
        result = request.form
        return render_template('index.html', result=result)


#     df_train = pd.read_csv('/input/lotto_data_train.csv', encoding='euc-kr')
#     df_train = df_train.drop(['Round'], axis=1)
#     df_num1 = df_train['Num1']
#     df_num2 = df_train['Num2']
#     df_num3 = df_train['Num3']
#     df_num4 = df_train['Num4']
#     df_num5 = df_train['Num5']
#     df_num6 = df_train['Num6']
#     df_bonus = df_train['Bonus']

#     df_train_list = [df_num1, df_num2, df_num3, df_num4, df_num5, df_num6]
#     choice_number = []

#     for train in df_train_list:
#         values = train.value_counts().sort_index().keys().tolist()
#         counts = train.value_counts([0]).sort_index().tolist()
#         idx = len(choice_number)
#         if idx == 0:
#             number = np.random.choice(values, p=counts)
#             choice_number.append(number)
#         else:
#             while (1):
#                 number = np.random.choice(values, p=counts)
#                 if choice_number[-1] >= number:
#                     continue
#                 elif choice_number[-1] < number:
#                     choice_number.append(number)
#                     break

#     values = df_bonus.value_counts().sort_index().keys().tolist()
#     counts = df_bonus.value_counts([0]).sort_index().tolist()

#     while (1):
#         number = np.random.choice(values, p=counts)
#         if number in choice_number:
#             continue
#         else:
#             choice_number.append(number)
#             break

#     return render_template('index.html', my_str='ABCD')


if __name__ == '__main__':
    app.run(debug=True)
