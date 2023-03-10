import pandas as pd
class file_parser:
    def __init__(self, patient_name = "", pid = 0000, date = 1/1/2022, test = "NVI"):
        self.patient_name = patient_name
        self.pid = pid
        self.date = date
        self.test_type = test
    def list_creator(self):
        data_list = self.csv_list.values.tolist()
        #print(data_list)
        return data_list
    
    def raw_data_creator(self, filedata):
        #print("_______------------__________",filedata)    
        sd = pd.DataFrame(filedata)
        sd.to_csv(self.patient_name + "_" +self.date + "_rawdata.csv", encoding='utf-8', index=False, header=False)
        return("done")

    def output_file(self, data):
        print("---------------------------------------------",data)
        data_list = [self.patient_name, self.pid, self.date, "" ,""]   # replace with date
        print(data_list)
        data_list += data                                   
        df = pd.read_csv('Outputfile.csv')
        df.columns = ['identifiers','data','']
        data_dataframe = pd.DataFrame(data_list, columns=['data'])
        #print(df)
        df['data'] = data_dataframe['data']
        #print(df)
        file_name = self.pid + "_" + self.date + ".csv"
        df.to_csv(file_name,index=False, encoding='utf-8')

    def output_worksheet(self, data):
        wk = pd.read_csv('Outputfile_large_system_worksheet.csv')#= pd.DataFrame(data)
        #wk.columns=['vessels','data']
        print(wk)
        data_dataframe = pd.DataFrame(data)
        print(data_dataframe)
        wk['data'] = data_dataframe[0]
        wk.to_csv(self.pid + "_" + self.date +"_system_summary.csv", index=False, encoding='utf-8')
        
if __name__ == "__main__":
    testfile = [["Left_Proximal_Radial",[0, 1, 2, 3]], ["Left_Proximal_Ulnar",[None, None, None, None]],\
                ["Left_Distal_Radial", [None, None, None, None]], ["Left_Distal_Ulnar", [None, None, None, None]], \
                ["Left_Proximal_Pero",[None, None, None, None]], ["Left_Inter_Pero", [None, None, None, None]], \
                ["Left_Proximal_tib", [None, None, None, None]], ["Left_inter_tib", [None, None, None, None]],\
                ["Left_low_tib", [None, None, None, None]], ["Left_Low_Pero", [None, None, None, None]],\
                ["Post_Left_Proximal_Radial",[3, 2, 1, 0]], ["Post_Left_Proximal_Ulnar",[None, None, None, None]],\
                ["Post_Left_Distal_Radial", [None, None, None, None]], ["Post_Left_Distal_Ulnar", [None, None, None, None]], \
                ["Post_Left_Proximal_Pero",[None, None, None, None]], ["Post_Left_Inter_Pero", [None, None, None, None]], \
                ["Post_Left_Proximal_tib", [None, None, None, None]], ["Post_Left_inter_tib", [None, None, None, None]],\
                ["Post_Left_low_tib", [None, None, None, None]], ["Post_Left_Low_Pero", [None, None, None, None]],
                ]
    test = file_parser("Nicole", 99999, "3/8/2023", "Food")
    test.raw_data_creator(testfile)