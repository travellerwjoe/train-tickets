# coding: utf-8

"""火车票查询CLI

Usage:
    train-tickets [-gdtkz] <from> <to> [<date>]

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    train-tickets 北京 上海 2016-10-10
    train-tickets -dg 成都 南京 2016-10-10
"""

from docopt import docopt
from stations import stations
import requests
from trainsCollection import TrainsCollection
from datetime import datetime

def cli():
    ''' command-line interface'''
    arguments = docopt(__doc__)
    date = arguments.get('<date>') or datetime.now().strftime('%Y-%m-%d')
    from_station = stations.get(arguments.get('<from>'))
    to_station = stations.get(arguments.get('<to>'))
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    res = requests.get(url, verify = False)
    trains = res.json()['data']['result']
    options = ''.join([
        k for k,v in arguments.items() if v == True
    ])
    TrainsCollection(trains, options).pretty_print()

if __name__ == '__main__':
    cli()
