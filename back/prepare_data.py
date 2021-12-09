import os 
import pandas as pd
pd.options.mode.chained_assignment = None  

def prepare(file,path_data,path_clean,cols):
    """
    file : csv file containing the dataset 
    path_data : path of the dataset 
    path_clean : path for the clean dataset
    cols : names of the columns 
    Returns : the clean dataset 
    """
    # Read dataframe 
    df = pd.read_csv(os.path.join(path_data,file),names= cols)
    df_clean = df.copy()
    # Change labels 
    df_clean.sentiment[df_clean.sentiment == 'Positive'] = 1 
    df_clean.sentiment[df_clean.sentiment == 'Negative'] = -1 
    df_clean.sentiment[df_clean.sentiment == 'Neutral'] = 0
    # Drop useless label & duplicates rows 
    df_clean1 = df_clean[df_clean.sentiment != 'Irrelevant']
    df_clean2 = df_clean1.drop_duplicates(subset = ["ID"])
    # Equivalent distribution 9000 rows 
    df0_train = df_clean2[df_clean2.sentiment == 0].iloc[:1500][:]
    df0_test = df_clean2[df_clean2.sentiment == 0].iloc[1500:3001][:]
    dfpos_train = df_clean2[df_clean2.sentiment == 1].iloc[:1500][:]
    dfpos_test = df_clean2[df_clean2.sentiment == 1].iloc[1500:3001][:]
    dfneg_train = df_clean2[df_clean2.sentiment == -1].iloc[:1500][:]
    dfneg_test = df_clean2[df_clean2.sentiment == -1].iloc[1500:3001][:]
    # Merge df 
    merged_df_train = pd.concat([df0_train, dfpos_train,dfneg_train])
    merged_df_test = pd.concat([df0_test, dfpos_test,dfneg_test])

    merged_df_train.to_csv(os.path.join(path_clean,'twitter_train_cleaned.csv'), index=False)
    merged_df_test.to_csv(os.path.join(path_clean,'twitter_test_cleaned.csv'), index=False)
    return merged_df_train,merged_df_test

if __name__ =='__main__':
    root_data = '../data/raw/'
    PROCESSED_PATH = '../data/process'
    cols = ['ID','origin','sentiment','tweet']
    file = 'twitter_training.csv'
    df_train, df_test = prepare(file,root_data,PROCESSED_PATH,cols)