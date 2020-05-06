import os
import argparse
import json
import pandas as pd
import random
from tqdm import  tqdm
import re

def generate_list(path, name_list, flag):
    """
    :param path: root path of data
    :param name_list: list of file names
    :param flag: 0/1 0-real 1-fake
    :return: a list of title, cleaned text, author, label(0-real 1-fake)
            [[title1, cleaned_text1, author1, label1],...,[titleN, cleaned_textN, authorN, labelN]]
    """
    generated_list=[]

    for name in tqdm(name_list):

        # check if the data file exists
        if os.path.exists(path+name+'/news content.json'):
            # load json format annotations
            with open(path+name+'/news content.json', 'r') as current_json:
                loaded_json=json.load(current_json)

                text=loaded_json['text']
                # if the news do not have content, then pass to the next
                if text=='':
                    continue

                # clean the text, remove the symbol which is not A-Z, a-z, nor 0-9,
                # then it can be easier to do the word vectorize step
                clean_text = re.sub("[^A-Za-z0–9']", ' ', text)

                # add text, title, author, flag to the generated list, which will be returned
                title=loaded_json['title']
                author = loaded_json['authors']
                temp_list=[]
                temp_list.append(title)
                temp_list.append(clean_text)
                temp_list.append(author)
                temp_list.append(flag)
                generated_list.append(temp_list)

    return generated_list


def main():
    # define data path
    gossip_root='D:/FakeNewsDetect/dataset/gossipcop/'
    gossip_real = gossip_root+'real/'
    gossip_fake = gossip_root+'fake/'

    # generate filename list
    real_list = os.listdir(gossip_real)
    fake_list = os.listdir(gossip_fake)

    # call generate_list() function to get a list of title, clean text, and fake/real label
    real_content = generate_list(gossip_real, real_list, 0)
    fake_content = generate_list(gossip_fake, fake_list, 1)

    # merge fake/real content into one list, and then randomly shuffle it
    real_content.extend(fake_content)
    total_content=real_content
    random.shuffle(total_content)

    # genarate csv format data_file
    data = pd.DataFrame(total_content,columns=['title','text','author','label'])
    data.to_csv('data.csv',index=False)
if __name__ == '__main__':
    main()
