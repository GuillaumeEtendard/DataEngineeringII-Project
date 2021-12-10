import os 
import pandas as pd
pd.options.mode.chained_assignment = None  

def prepare(file,path_data,path_clean):
    """
    file : csv file containing the dataset 
    path_data : path of the dataset 
    path_clean : path for the clean dataset
    cols : names of the columns 
    Returns : the clean dataset 
    """
    # Read Data
    df_tw = pd.read_csv(os.path.join(root_data,file),sep='\t')
    df_tw['sentiment'] = df_tw['Sentiment']
    df_tw['text'] = df_tw['Phrase']
    df_tw = df_tw.drop(columns=['Sentiment', 'Phrase', 'SentenceId', 'PhraseId'])
    # Change labels 
    df_tw = df_tw[(df_tw.sentiment != 3) & (df_tw.sentiment != 1)]
    df_tw.sentiment[df_tw.sentiment == 4] = 1 
    df_tw.sentiment[df_tw.sentiment == 0] = -1 
    df_tw.sentiment[df_tw.sentiment == 2] = 0
    df_tw['sentiment'] = df_tw['sentiment'].astype('int64')
    # Select a subset of data
    df0_train = df_tw[df_tw.sentiment == 0].iloc[:200][:]
    dfpos_train = df_tw[df_tw.sentiment == 1].iloc[:200][:]
    dfneg_train = df_tw[df_tw.sentiment == -1].iloc[:200][:]
    # Merge dataframe
    merged_df_train = pd.concat([df0_train, dfpos_train,dfneg_train])
    merged_df_train.to_csv(os.path.join(PROCESSED_PATH,'data_cleaned.csv'), index=False)
    return merged_df_train

if __name__ =='__main__':
    root_data = '../data/raw/'
    PROCESSED_PATH = '../data/process'
    file = 'train.tsv'
    df_train = prepare(file,root_data,PROCESSED_PATH)