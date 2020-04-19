import os
import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(description='View the dataset')
    parser.add_argument(
        '--type', help='type of news, namely political or gossip', default='political')
    parser.add_argument('--fake_real', help='fake or real', default='fake')
    parser.add_argument(
        '--num', help='number of news to load', default=1)
    parser.add_argument(
        '--folder_path', help='the path of FakeNewsDetect', default='D:/FakeNewsDetect/')

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    if args.type == 'political':
        path = args.folder_path+'dataset/politifact/'+args.fake_real+'/'
        file_list = os.listdir(path)
        for _file in file_list:
            _file_list = os.listdir(path+_file)
            for j in _file_list:
                with open(path+_file+'/'+j, "r") as current_news:
                    news_content = json.load(current_news)
                    for i in news_content:
                        print(i)
    elif args.type == 'gossip':
        pass
    else:
        raise("Wrong type")


if __name__ == '__main__':
    main()
