import json

import pandas as pd
import Configuration.Config


class DataSetHandler:

    def readInputFile(self):
        d = pd.read_excel(Configuration.Config.INPUT_PATH, header=None)
        return d

    def cleanDataset(self, d):
        data = pd.DataFrame(d)
        row = len(data.axes[0])
        col = len(data.axes[1])
        for i in range(col):
            for j in range(row):

                if 'layer 1' == str(data[i][j]):
                    data[i][j + 1] += ' layer 1'
                    temp = list(data.iloc[j + 1])
                    if 'AC' in temp:
                        data[i][j + 2] += ' layer 1'
                        data[i][j + 3] += ' layer 1'
                        data[i][j + 4] += ' layer 1'
                        data[i][j + 5] += ' layer 1'
                        data[i][j + 6] += ' layer 1'
                    else:
                        data[i][j + 2] += ' layer 1'
                        data[i][j + 3] += ' layer 1'
                        data[i][j + 4] += ' layer 1'

                if 'layer 2' == str(data[i][j]):
                    data[i][j + 1] += ' layer 2'
                    temp = list(data.iloc[j + 1])
                    if 'AC' in temp:
                        data[i][j + 2] += ' layer 2'
                        data[i][j + 3] += ' layer 2'
                        data[i][j + 4] += ' layer 2'
                        data[i][j + 5] += ' layer 2'
                        data[i][j + 6] += ' layer 2'
                    else:
                        data[i][j + 2] += ' layer 2'
                        data[i][j + 3] += ' layer 2'
                        data[i][j + 4] += ' layer 2'

                if 'layer 3' == str(data[i][j]):
                    data[i][j + 1] += ' layer 3'
                    temp = list(data.iloc[j + 1])
                    if 'AC' in temp:
                        data[i][j + 2] += ' layer 3'
                        data[i][j + 3] += ' layer 3'
                        data[i][j + 4] += ' layer 3'
                        data[i][j + 5] += ' layer 3'
                        data[i][j + 6] += ' layer 3'
                    else:
                        data[i][j + 2] += ' layer 3'
                        data[i][j + 3] += ' layer 3'
                        data[i][j + 4] += ' layer 3'

                if 'layer 4' == str(data[i][j]):
                    data[i][j + 1] += ' layer 4'
                    temp = list(data.iloc[j + 1])
                    if 'AC' in temp:
                        data[i][j + 2] += ' layer 4'
                        data[i][j + 3] += ' layer 4'
                        data[i][j + 4] += ' layer 4'
                        data[i][j + 5] += ' layer 4'
                        data[i][j + 6] += ' layer 4'
                    else:
                        data[i][j + 2] += ' layer 4'
                        data[i][j + 3] += ' layer 4'
                        data[i][j + 4] += ' layer 4'

                if 'layer 5' == str(data[i][j]):
                    data[i][j + 1] += ' layer 5'
                    data[i][j + 2] += ' layer 5'
                    data[i][j + 3] += ' layer 5'
                    # data[i][j + 4] += ' layer 5'

                if 'position top' in str(data[i][j]):
                    data[i][j + 1] += ' top'
                    data[i][j + 2] += ' top'
                    data[i][j + 3] += ' top'
                    temp = list(data.iloc[j + 1])
                    if 'vertical strain' in temp or 'horizontal strain' in temp:
                        data[i][j + 5] += ' top'
                        if data[i][j + 6] == 'k1' and data[i][j + 7] == 'k2':
                            data[i][j + 6] += ' top'
                            data[i][j + 7] += ' top'

                if 'position middle' in str(data[i][j]):
                    data[i][j + 1] += ' middle'
                    data[i][j + 2] += ' middle'
                    data[i][j + 3] += ' middle'
                    temp = list(data.iloc[j + 1])
                    if 'vertical strain' in temp or 'horizontal strain' in temp:
                        data[i][j + 5] += ' middle'
                        if data[i][j + 6] == 'k1' and data[i][j + 7] == 'k2':
                            data[i][j + 6] += ' middle'
                            data[i][j + 7] += ' middle'

                if 'position bottom' in str(data[i][j]):
                    data[i][j + 1] += ' bottom'
                    data[i][j + 2] += ' bottom'
                    data[i][j + 3] += ' bottom'
                    temp = list(data.iloc[j+1])
                    if 'vertical strain' in temp or 'horizontal strain' in temp:
                        data[i][j + 5] += ' bottom'
                        if data[i][j + 6] == 'k1' and data[i][j + 7] == 'k2':
                            data[i][j + 6] += ' bottom'
                            data[i][j + 7] += ' bottom'

        # print(data)

        result = pd.DataFrame(data.transpose())
        result = result.dropna(thresh=len(result) - 2, axis=1)
        result.drop(result.index[0], inplace=True)
        del result[1]
        new_header = result.iloc[0]  # grab the first row for the header
        result = result[1:]  # take the data less the header row
        self.header = list(new_header)
        result.columns = self.header
        result.reset_index(drop=True, inplace=True)  # resetting the index

        # self.header = list(json.dumps(header))
        return result
