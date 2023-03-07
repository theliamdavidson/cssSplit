import pandas as pd
class file_parser:
    def __init__(self):
        self.patient_name = ""
        self.pid = ""
        self.date = ""
    def list_creator(self):
        data_list = self.csv_list.values.tolist()
        #print(data_list)
        return data_list
    
    def raw_data_creator(self, filedata):
        #print("_______------------__________",filedata)    
        sd = pd.DataFrame(filedata)
        sd.to_csv(self.pid + "_" +self.date + "_rawdata.csv", encoding='utf-8', index=False, header=False)
        return("done")

    def output_file(self, data, patient_name, pid, date):
        try:
            self.patient_name = patient_name
            self.pid = pid
            self.date = date[6:]
        except:
            self.patient_name = "test"
            self.pid = "987654321"
            self.date = "1_9_23"
            print()
        print("---------------------------------------------",data)
        data_list = [patient_name, pid, self.date, "" ,""]   # replace with date
        print(data_list)
        data_list += data                                   
        df = pd.read_csv('Outputfile.csv')
        df.columns = ['identifiers','data','']
        data_dataframe = pd.DataFrame(data_list, columns=['data'])
        #print(df)
        df['data'] = data_dataframe['data']
        #print(df)
        file_name = pid + "_" + date + ".csv"
        df.to_csv(file_name,index=False, encoding='utf-8')

    def output_worksheet(self, data):
        wk = pd.read_csv('Outputfile_large_system_worksheet.csv')#= pd.DataFrame(data)
        #wk.columns=['vessels','data']
        print(wk)
        data_dataframe = pd.DataFrame(data)
        print(data_dataframe)
        wk['data'] = data_dataframe[0]
        wk.to_csv(self.pid + "_" + self.date +"_system_summary.csv", index=False, encoding='utf-8')
        
