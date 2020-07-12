from Libs.http_requests import *
json1 = {
  "Status": 'true',
  "Info": "",
  "Data": [
    {
      "Id": 1102,
      "PId": 0,
      "Name": "三码",
      "Child": [
        {
          "N": "前三",
          "C": [
            {
              "Id": 1440,
              "PId": 1102,
              "Name": "前三直选复式",
              "TP": 1440,
              "Child": [
                {
                  "Id": 21044,
                  "Name": "前三直选复式",
                  "SId": 21044,
                  "FId": 21044
                }
              ]
            },
            {
              "Id": 1441,
              "PId": 1102,
              "Name": "前三直选单式",
              "TP": 1441,
              "Child": [
                {
                  "Id": 21045,
                  "Name": "前三直选单式",
                  "SId": 21045,
                  "FId": 21045
                }
              ]
            },
            {
              "Id": 1442,
              "PId": 1102,
              "Name": "前三组选复式",
              "TP": 1442,
              "Child": [
                {
                  "Id": 21046,
                  "Name": "前三组选复式",
                  "SId": 21046,
                  "FId": 21046
                }
              ]
            },
            {
              "Id": 1443,
              "PId": 1102,
              "Name": "前三组选单式",
              "TP": 1443,
              "Child": [
                {
                  "Id": 21047,
                  "Name": "前三组选单式",
                  "SId": 21047,
                  "FId": 21047
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "Code": 0
}
Data={"PeriodId":"177573687","OrderList":"[{\"a\":2.0,\"c\":\"01\",\"i\":21053,\"k\":\"0\",\"m\":1,\"n\":1,\"t\":1,\"ts\":1593190940}]","GameId":"320"}
# PeriodId 期数ID
# GameId  游戏ID
# i      玩法项ID
# c     投注内容
# n    总注数
# t    倍数
# k   当前退水
# m   	单位（元对于1，角对应2，分对应3，厘对应4）
# a    	总金额
# ts    秒级别的时间戳

temp = {
    "Status": "true",
    "Info": "",
    "Data": [
        {
            "Id": 1102,
            "PId": 0,
            "Name": "三码",
            "Child": [
                {
                    "N": "前三",
                    "C": [
                        {
                            "Id": 1440,
                            "PId": 1102,
                            "Name": "前三直选复式",
                            "TP": 1440,
                            "Child": [
                                {
                                    "Id": 21044,
                                    "Name": "前三直选复式",
                                    "SId": 21044,
                                    "FId": 21044
                                }
                            ]
                        },
                        {
                            "Id": 1441,
                            "PId": 1102,
                            "Name": "前三直选单式",
                            "TP": 1441,
                            "Child": [
                                {
                                    "Id": 21045,
                                    "Name": "前三直选单式",
                                    "SId": 21045,
                                    "FId": 21045
                                }
                            ]
                        },
                        {
                            "Id": 1442,
                            "PId": 1102,
                            "Name": "前三组选复式",
                            "TP": 1442,
                            "Child": [
                                {
                                    "Id": 21046,
                                    "Name": "前三组选复式",
                                    "SId": 21046,
                                    "FId": 21046
                                }
                            ]
                        },
                        {
                            "Id": 1443,
                            "PId": 1102,
                            "Name": "前三组选单式",
                            "TP": 1443,
                            "Child": [
                                {
                                    "Id": 21047,
                                    "Name": "前三组选单式",
                                    "SId": 21047,
                                    "FId": 21047
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1106,
            "PId": 0,
            "Name": "二码",
            "Child": [
                {
                    "N": "前二",
                    "C": [
                        {
                            "Id": 1444,
                            "PId": 1106,
                            "Name": "前二直选复式",
                            "TP": 1444,
                            "Child": [
                                {
                                    "Id": 21048,
                                    "Name": "前二直选复式",
                                    "SId": 21048,
                                    "FId": 21048
                                }
                            ]
                        },
                        {
                            "Id": 1445,
                            "PId": 1106,
                            "Name": "前二直选单式",
                            "TP": 1445,
                            "Child": [
                                {
                                    "Id": 21049,
                                    "Name": "前二直选单式",
                                    "SId": 21049,
                                    "FId": 21049
                                }
                            ]
                        },
                        {
                            "Id": 1446,
                            "PId": 1106,
                            "Name": "前二组选复式",
                            "TP": 1446,
                            "Child": [
                                {
                                    "Id": 21050,
                                    "Name": "前二组选复式",
                                    "SId": 21050,
                                    "FId": 21050
                                }
                            ]
                        },
                        {
                            "Id": 1447,
                            "PId": 1106,
                            "Name": "前二组选单式",
                            "TP": 1447,
                            "Child": [
                                {
                                    "Id": 21051,
                                    "Name": "前二组选单式",
                                    "SId": 21051,
                                    "FId": 21051
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1110,
            "PId": 0,
            "Name": "不定胆",
            "Child": [
                {
                    "N": "不定胆",
                    "C": [
                        {
                            "Id": 1448,
                            "PId": 1110,
                            "Name": "不定胆",
                            "TP": 1448,
                            "Child": [
                                {
                                    "Id": 21052,
                                    "Name": "前三位",
                                    "SId": 21052,
                                    "FId": 21052
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1111,
            "PId": 0,
            "Name": "定位胆",
            "Child": [
                {
                    "N": "定位胆",
                    "C": [
                        {
                            "Id": 1449,
                            "PId": 1111,
                            "Name": "定位胆",
                            "TP": 1449,
                            "Child": [
                                {
                                    "Id": 21053,
                                    "Name": "第一位",
                                    "SId": 21053,
                                    "FId": 21053
                                },
                                {
                                    "Id": 21317,
                                    "Name": "第二位",
                                    "SId": 21317,
                                    "FId": 21317
                                },
                                {
                                    "Id": 21318,
                                    "Name": "第三位",
                                    "SId": 21318,
                                    "FId": 21318
                                },
                                {
                                    "Id": 21319,
                                    "Name": "第四位",
                                    "SId": 21319,
                                    "FId": 21319
                                },
                                {
                                    "Id": 21320,
                                    "Name": "第五位",
                                    "SId": 21320,
                                    "FId": 21320
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1112,
            "PId": 0,
            "Name": "趣味型",
            "Child": [
                {
                    "N": "趣味性",
                    "C": [
                        {
                            "Id": 1450,
                            "PId": 1112,
                            "Name": "定单双",
                            "TP": 1450,
                            "Child": [
                                {
                                    "Id": 21054,
                                    "Name": "5单0双",
                                    "SId": 21054,
                                    "FId": 21054
                                },
                                {
                                    "Id": 21321,
                                    "Name": "0单5双",
                                    "SId": 21321,
                                    "FId": 21321
                                },
                                {
                                    "Id": 21322,
                                    "Name": "1单4双",
                                    "SId": 21322,
                                    "FId": 21322
                                },
                                {
                                    "Id": 21323,
                                    "Name": "4单1双",
                                    "SId": 21323,
                                    "FId": 21323
                                },
                                {
                                    "Id": 21324,
                                    "Name": "2单3双",
                                    "SId": 21324,
                                    "FId": 21324
                                },
                                {
                                    "Id": 21325,
                                    "Name": "3单2双",
                                    "SId": 21325,
                                    "FId": 21325
                                }
                            ]
                        },
                        {
                            "Id": 1451,
                            "PId": 1112,
                            "Name": "猜中位",
                            "TP": 1451,
                            "Child": [
                                {
                                    "Id": 21055,
                                    "Name": "3,9",
                                    "SId": 21055,
                                    "FId": 21055
                                },
                                {
                                    "Id": 21326,
                                    "Name": "4,8",
                                    "SId": 21326,
                                    "FId": 21326
                                },
                                {
                                    "Id": 21327,
                                    "Name": "5,7",
                                    "SId": 21327,
                                    "FId": 21327
                                },
                                {
                                    "Id": 21328,
                                    "Name": "6",
                                    "SId": 21328,
                                    "FId": 21328
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1114,
            "PId": 0,
            "Name": "任选单式",
            "Child": [
                {
                    "N": "任选单式",
                    "C": [
                        {
                            "Id": 1452,
                            "PId": 1114,
                            "Name": "一中一",
                            "TP": 1452,
                            "Child": [
                                {
                                    "Id": 21056,
                                    "Name": "一中一",
                                    "SId": 21056,
                                    "FId": 21056
                                }
                            ]
                        },
                        {
                            "Id": 1453,
                            "PId": 1114,
                            "Name": "二中二",
                            "TP": 1453,
                            "Child": [
                                {
                                    "Id": 21057,
                                    "Name": "二中二",
                                    "SId": 21057,
                                    "FId": 21057
                                }
                            ]
                        },
                        {
                            "Id": 1454,
                            "PId": 1114,
                            "Name": "三中三",
                            "TP": 1454,
                            "Child": [
                                {
                                    "Id": 21058,
                                    "Name": "三中三",
                                    "SId": 21058,
                                    "FId": 21058
                                }
                            ]
                        },
                        {
                            "Id": 1455,
                            "PId": 1114,
                            "Name": "四中四",
                            "TP": 1455,
                            "Child": [
                                {
                                    "Id": 21059,
                                    "Name": "四中四",
                                    "SId": 21059,
                                    "FId": 21059
                                }
                            ]
                        },
                        {
                            "Id": 1456,
                            "PId": 1114,
                            "Name": "五中五",
                            "TP": 1456,
                            "Child": [
                                {
                                    "Id": 21060,
                                    "Name": "五中五",
                                    "SId": 21060,
                                    "FId": 21060
                                }
                            ]
                        },
                        {
                            "Id": 1457,
                            "PId": 1114,
                            "Name": "六中五",
                            "TP": 1457,
                            "Child": [
                                {
                                    "Id": 21061,
                                    "Name": "六中五",
                                    "SId": 21061,
                                    "FId": 21061
                                }
                            ]
                        },
                        {
                            "Id": 1458,
                            "PId": 1114,
                            "Name": "七中五",
                            "TP": 1458,
                            "Child": [
                                {
                                    "Id": 21062,
                                    "Name": "七中五",
                                    "SId": 21062,
                                    "FId": 21062
                                }
                            ]
                        },
                        {
                            "Id": 1459,
                            "PId": 1114,
                            "Name": "八中五",
                            "TP": 1459,
                            "Child": [
                                {
                                    "Id": 21063,
                                    "Name": "八中五",
                                    "SId": 21063,
                                    "FId": 21063
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 1115,
            "PId": 0,
            "Name": "任选复式",
            "Child": [
                {
                    "N": "任选复式",
                    "C": [
                        {
                            "Id": 1460,
                            "PId": 1115,
                            "Name": "一中一",
                            "TP": 1460,
                            "Child": [
                                {
                                    "Id": 21064,
                                    "Name": "一中一",
                                    "SId": 21064,
                                    "FId": 21064
                                }
                            ]
                        },
                        {
                            "Id": 1461,
                            "PId": 1115,
                            "Name": "二中二",
                            "TP": 1461,
                            "Child": [
                                {
                                    "Id": 21065,
                                    "Name": "二中二",
                                    "SId": 21065,
                                    "FId": 21065
                                }
                            ]
                        },
                        {
                            "Id": 1462,
                            "PId": 1115,
                            "Name": "三中三",
                            "TP": 1462,
                            "Child": [
                                {
                                    "Id": 21066,
                                    "Name": "三中三",
                                    "SId": 21066,
                                    "FId": 21066
                                }
                            ]
                        },
                        {
                            "Id": 1463,
                            "PId": 1115,
                            "Name": "四中四",
                            "TP": 1463,
                            "Child": [
                                {
                                    "Id": 21067,
                                    "Name": "四中四",
                                    "SId": 21067,
                                    "FId": 21067
                                }
                            ]
                        },
                        {
                            "Id": 1464,
                            "PId": 1115,
                            "Name": "五中五",
                            "TP": 1464,
                            "Child": [
                                {
                                    "Id": 21068,
                                    "Name": "五中五",
                                    "SId": 21068,
                                    "FId": 21068
                                }
                            ]
                        },
                        {
                            "Id": 1465,
                            "PId": 1115,
                            "Name": "六中五",
                            "TP": 1465,
                            "Child": [
                                {
                                    "Id": 21069,
                                    "Name": "六中五",
                                    "SId": 21069,
                                    "FId": 21069
                                }
                            ]
                        },
                        {
                            "Id": 1466,
                            "PId": 1115,
                            "Name": "七中五",
                            "TP": 1466,
                            "Child": [
                                {
                                    "Id": 21070,
                                    "Name": "七中五",
                                    "SId": 21070,
                                    "FId": 21070
                                }
                            ]
                        },
                        {
                            "Id": 1467,
                            "PId": 1115,
                            "Name": "八中五",
                            "TP": 1467,
                            "Child": [
                                {
                                    "Id": 21071,
                                    "Name": "八中五",
                                    "SId": 21071,
                                    "FId": 21071
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "Id": 4256,
            "PId": 0,
            "Name": "两面",
            "Child": [
                {
                    "N": "总和",
                    "C": [
                        {
                            "Id": 4257,
                            "PId": 4256,
                            "Name": "总和大小",
                            "TP": 4201,
                            "Child": [
                                {
                                    "Id": 27504,
                                    "Name": "总大",
                                    "SId": 27400,
                                    "FId": 27504
                                },
                                {
                                    "Id": 27505,
                                    "Name": "总小",
                                    "SId": 27401,
                                    "FId": 27505
                                }
                            ]
                        },
                        {
                            "Id": 4258,
                            "PId": 4256,
                            "Name": "总和单双",
                            "TP": 4202,
                            "Child": [
                                {
                                    "Id": 27506,
                                    "Name": "总单",
                                    "SId": 27402,
                                    "FId": 27506
                                },
                                {
                                    "Id": 27507,
                                    "Name": "总双",
                                    "SId": 27403,
                                    "FId": 27507
                                }
                            ]
                        },
                        {
                            "Id": 4259,
                            "PId": 4256,
                            "Name": "总和总尾大小",
                            "TP": 4203,
                            "Child": [
                                {
                                    "Id": 27508,
                                    "Name": "总尾大",
                                    "SId": 27404,
                                    "FId": 27508
                                },
                                {
                                    "Id": 27509,
                                    "Name": "总尾小",
                                    "SId": 27405,
                                    "FId": 27509
                                }
                            ]
                        }
                    ]
                },
                {
                    "N": "特码",
                    "C": [
                        {
                            "Id": 4260,
                            "PId": 4256,
                            "Name": "特码大小",
                            "TP": 4204,
                            "Child": [
                                {
                                    "Id": 27510,
                                    "Name": "特大",
                                    "SId": 27406,
                                    "FId": 27510
                                },
                                {
                                    "Id": 27511,
                                    "Name": "特小",
                                    "SId": 27407,
                                    "FId": 27511
                                }
                            ]
                        },
                        {
                            "Id": 4261,
                            "PId": 4256,
                            "Name": "特码单双",
                            "TP": 4205,
                            "Child": [
                                {
                                    "Id": 27512,
                                    "Name": "特单",
                                    "SId": 27408,
                                    "FId": 27512
                                },
                                {
                                    "Id": 27513,
                                    "Name": "特双",
                                    "SId": 27409,
                                    "FId": 27513
                                }
                            ]
                        }
                    ]
                },
                {
                    "N": "正码一",
                    "C": [
                        {
                            "Id": 4262,
                            "PId": 4256,
                            "Name": "正码一大小",
                            "TP": 4206,
                            "Child": [
                                {
                                    "Id": 27514,
                                    "Name": "大",
                                    "SId": 27410,
                                    "FId": 27514
                                },
                                {
                                    "Id": 27515,
                                    "Name": "小",
                                    "SId": 27411,
                                    "FId": 27515
                                }
                            ]
                        },
                        {
                            "Id": 4263,
                            "PId": 4256,
                            "Name": "正码一单双",
                            "TP": 4207,
                            "Child": [
                                {
                                    "Id": 27516,
                                    "Name": "单",
                                    "SId": 27412,
                                    "FId": 27516
                                },
                                {
                                    "Id": 27517,
                                    "Name": "双",
                                    "SId": 27413,
                                    "FId": 27517
                                }
                            ]
                        }
                    ]
                },
                {
                    "N": "正码二",
                    "C": [
                        {
                            "Id": 4264,
                            "PId": 4256,
                            "Name": "正码二大小",
                            "TP": 4208,
                            "Child": [
                                {
                                    "Id": 27518,
                                    "Name": "大",
                                    "SId": 27414,
                                    "FId": 27518
                                },
                                {
                                    "Id": 27519,
                                    "Name": "小",
                                    "SId": 27415,
                                    "FId": 27519
                                }
                            ]
                        },
                        {
                            "Id": 4265,
                            "PId": 4256,
                            "Name": "正码二单双",
                            "TP": 4209,
                            "Child": [
                                {
                                    "Id": 27520,
                                    "Name": "单",
                                    "SId": 27416,
                                    "FId": 27520
                                },
                                {
                                    "Id": 27521,
                                    "Name": "双",
                                    "SId": 27417,
                                    "FId": 27521
                                }
                            ]
                        }
                    ]
                },
                {
                    "N": "正码三",
                    "C": [
                        {
                            "Id": 4266,
                            "PId": 4256,
                            "Name": "正码三大小",
                            "TP": 4210,
                            "Child": [
                                {
                                    "Id": 27522,
                                    "Name": "大",
                                    "SId": 27418,
                                    "FId": 27522
                                },
                                {
                                    "Id": 27523,
                                    "Name": "小",
                                    "SId": 27419,
                                    "FId": 27523
                                }
                            ]
                        },
                        {
                            "Id": 4267,
                            "PId": 4256,
                            "Name": "正码三单双",
                            "TP": 4211,
                            "Child": [
                                {
                                    "Id": 27524,
                                    "Name": "单",
                                    "SId": 27420,
                                    "FId": 27524
                                },
                                {
                                    "Id": 27525,
                                    "Name": "双",
                                    "SId": 27421,
                                    "FId": 27525
                                }
                            ]
                        }
                    ]
                },
                {
                    "N": "正码四",
                    "C": [
                        {
                            "Id": 4268,
                            "PId": 4256,
                            "Name": "正码四大小",
                            "TP": 4212,
                            "Child": [
                                {
                                    "Id": 27526,
                                    "Name": "大",
                                    "SId": 27422,
                                    "FId": 27526
                                },
                                {
                                    "Id": 27527,
                                    "Name": "小",
                                    "SId": 27423,
                                    "FId": 27527
                                }
                            ]
                        },
                        {
                            "Id": 4269,
                            "PId": 4256,
                            "Name": "正码四单双",
                            "TP": 4213,
                            "Child": [
                                {
                                    "Id": 27528,
                                    "Name": "单",
                                    "SId": 27424,
                                    "FId": 27528
                                },
                                {
                                    "Id": 27529,
                                    "Name": "双",
                                    "SId": 27425,
                                    "FId": 27529
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "Code": 0
}
o = {'Id': 1102, 'PId': 0, 'Name': '三码', 'Child': [{'N': '前三', 'C': [{'Id': 1440, 'PId': 1102, 'Name': '前三直选复式', 'TP': 1440, 'Child': [{'Id': 21044, 'Name': '前三直选复式', 'SId': 21044, 'FId': 21044}]}, {'Id': 1441, 'PId': 1102, 'Name': '前三直选单式', 'TP': 1441, 'Child': [{'Id': 21045, 'Name': '前三直选单式', 'SId': 21045, 'FId': 21045}]}, {'Id': 1442, 'PId': 1102, 'Name': '前三组选复式', 'TP': 1442, 'Child': [{'Id': 21046, 'Name': '前三组选复式', 'SId': 21046, 'FId': 21046}]}, {'Id': 1443, 'PId': 1102, 'Name': '前三组选单式', 'TP': 1443, 'Child': [{'Id': 21047, 'Name': '前三组选单式', 'SId': 21047, 'FId': 21047}]}]}]}
flag = get_json_value(temp,'/Data')
#print(flag)
# print(len(flag))
# "4269",
# "4268",
# "4267",
# "4266",
# "4265",
# "4264",
# "4263",
# "4262",
# "4261",
# "4260",
# "4259",
# "4258",
# "4257"
for i in flag:
  gameplay = []
  j = get_json_value(i,'/Child')
  play_name = get_json_value(i,'/Name')
  #print(play_name,j)
  #print(j)
  for k in j:
    l = get_json_value(k,'/C')
    play_n = get_json_value(k,'/N')
    #print(play_name,play_n,l)
    for y in l:
      #print(play_name,play_n,y)
      t = get_json_value(y,'/Child')
      play = get_json_value(y,'/Name')
      #print(play_name, play_n, play, t)
      for r in t:
        e = get_json_value(r,'/FId')
        #print(play_name, play_n, play,e)
#print(flag)
qqq = [
    4269,
    4268,
    4267,
    4266,
    4265,
    4264,
    4263,
    4262,
    4261,
    4260,
    4259,
    4258,
    4257
]
play_list = []
for data in flag:
    #print(data)
    play_name = data['Name']
    play_id = data['Id']
    #print(play_id)
    for datas in data['Child']:
        #print(datas)
        for dats1 in datas['C']:
            if dats1['Id'] not in qqq: # 过滤被禁用的玩法
                #print(dats1['Id'])
                for dats2 in dats1['Child']:
                    dic={}
                    #print(dats2['Name'],dats2['FId'])
                    dic.update({"{}:{}".format(play_name,play_id):{dats2['Name']: dats2['FId']}})

                    play_list.append(dic)
print(play_list)

    #print(play_list)


 # game_play_data = Http_Util.get_json_value(self.actual_result, '/Data')
 #        for data in game_play_data:
 #            print(data)
 #            for data_child in data['Child']:
 #                print(data_child)
 #                if data_child['Id'] in disabled_play_ids:
 #                    continue
 #                for data_child_child in data_child['Child']:
 #                    if data_child_child['Id'] in disabled_play_item_ids:
 #                        continue
 #                    print(data_child_child)

qq = {
    "Status": 'true',
    "Info": "",
    "Data": "{\"IsEnabled\":true,\"fisstopseles\":false,\"gameID\":198,\"fid\":178647971,\"fnumberofperiod\":20200628167,\"fnextperiod\":20200628168,\"fstatus\":1,\"fsettlefid\":178647970,\"fsettlenumber\":20200628166,\"fsettletime\":\"2020/06/28 13:50:12\",\"fbasegameid\":39,\"fnextstarttime\":\"2020/06/28 13:54:59\",\"fclosetime\":\"2020/06/28 13:54:53\",\"fstarttime\":\"2020/06/28 13:49:59\",\"flottostarttime\":\"2020/06/28 13:54:59\",\"ServerTime\":\"2020/06/28 13:53:44\",\"fpreviousperiod\":20200628166,\"fpreviousresult\":\"4,3,3\",\"fpreviousanimal\":null,\"fpreviouslottostarttime\":\"2020/06/28 13:49:59\"}",
    "Code": 0
}
# import json
# import time
# import datetime
# period_data = get_json_value(qq,'/Data')
# json_period_data = json.loads(period_data,encoding='utf-8')
# print(period_data)
# print(type(period_data))
# print(json_period_data['IsEnabled'])
# # 本期期数
# current_period = json_period_data["fnumberofperiod"]
# # 本期开盘时间
# start_time = json_period_data['fstarttime']
# # 本期封盘时间
# end_time = json_period_data['fclosetime']
# # 期数状态 （0未开盘，1开盘中，2已封盘，3已开奖，4、已结算，5、返还金额）
# period_status = json_period_data['fstatus']
# # 游戏是否停售 ：false代表开售中，true代表停售中
# is_off_stop = json_period_data['fisstopseles']
# # 期数ID
# fid = json_period_data['fid']
# print('本期期数:',current_period)
# print('本期开盘时间:',start_time)
# print('本期封盘时间:',end_time)
# print('期数状态:',period_status)
# print('游戏是否停售:',is_off_stop)
# print('期数ID：',fid)
# start = datetime.datetime.strptime(start_time[0:],"%Y/%m/%d %H:%M:%S")
# end = datetime.datetime.strptime(end_time,"%Y/%m/%d %H:%M:%S")
# num = (end-start).seconds
# print(num)

xiazhu = {"PeriodId":"178648032","OrderList":"[{\"a\":2.0,\"c\":\"大\",\"i\":25332,\"k\":\"0\",\"m\":1,\"n\":1,\"t\":1,\"ts\":1593341969}]","GameId":"198"}

qqq = [
    4269,
    4268,
    4267,
    4266,
    4265,
    4264,
    4263,
    4262,
    4261,
    4260,
    4259,
    4258,
    4257
]




















