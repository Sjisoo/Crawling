import requests
import json
from collections import OrderedDict

file_data = OrderedDict()

arr = [ 'stdrYmCd', 'alleyTrdarNo', 'alleyTrdarNm', 'svcIndutyCd', 'svcIndutyCdNm', #0~4
        'alleyTrdarAr', 'alleyTrdarHilndAr', 'alleyTradarHilndTyCdNm', #5~7
        'storCo1', #8
        'signguCdNm', 'signguIdexSctnName', 'signguIdexValue', #9~11
        'adstrdCdNm', 'adstrdIdexSctnName', 'adstrdIdexValue', #12~14
        'trdarIdexSctnName', 'trdarIdexValue', #15~16
        'beingRt1', 'beingRt12', 'beingRt23', 'beingRt3', #17~20
        'storCo1', 'thsmonSelngCo1', 'thsmonSelngAmt1', #21~23
        'storCo2', 'thsmonSelngCo2', 'thsmonSelngAmt2', #24~26
        'storCo3', 'thsmonSelngCo3', 'thsmonSelngAmt3', #27~29
        'avrgBsnYycnt', #30
        'code1', 'sebu1', 'storNum1', 'salesCount1', 'avgSales1', #31~35
        'code2', 'sebu2', 'storNum2', 'salesCount2', 'avgSales2', #36~40
        'code3', 'sebu3', 'storNum3', 'salesCount3', 'avgSales3', #41~45
        'code4', 'sebu4', 'storNum4', 'salesCount4', 'avgSales4', #46~50
        'code5', 'sebu5', 'storNum5', 'salesCount5', 'avgSales5', #51~55
        'code6', 'sebu6', 'storNum6', 'salesCount6', 'avgSales6', #56~60
        'code7', 'sebu7', 'storNum7', 'salesCount7', 'avgSales7', #61~65
        'code8', 'sebu8', 'storNum8', 'salesCount8', 'avgSales8', #66~70
        'code9', 'sebu9', 'storNum9', 'salesCount9', 'avgSales9', #71~75
        'code10', 'sebu10', 'storNum10', 'salesCount10', 'avgSales10', #76~80

        'MflpopCo', 'MrepopCo', 'MwrcPopltnCo', #81~83
        'WflpopCo', 'WrepopCo', 'WwrcPopltnCo', #84~86

        'entrprsLtrsCo', 'entrprsSmlpzCo', 'entrprsEtcCo', 'pblofcCo', 'bankCo', 'hsptlCo', 'schCo', 'distbCo', 'clturCo', 'stayngFcltyCo', 'viatrFcltyCo'] #87~97

attribute = ['stdrYmCd', 'alleyTrdarNo', 'alleyTrdarNm', 'svcIndutyCd', 'svcIndutyCdNm', #0~4
             'alleyTrdarAr', 'alleyTrdarHilndAr', 'alleyTradarHilndTyCdNm',  #5~7
             'storCo1', #8
             'signguCdNm', 'signguIdexSctnName', 'signguIdexValue', #9~11
             'adstrdCdNm', 'adstrdIdexSctnName', 'adstrdIdexValue', #12~14
             'trdarIdexSctnName', 'trdarIdexValue', #15~16
             'beingRt', 'beingRt', 'beingRt', 'beingRt', #17~20
             'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #21~23
             'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #24~26
             'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #27~29
             'avrgBsnYycnt', #30

             'svcIndutyCd1', 'svcIndutyCdNm1', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #31~35 1
             'svcIndutyCd2', 'svcIndutyCdNm2', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #36~40 2
             'svcIndutyCd3', 'svcIndutyCdNm3', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #41~45 3
             'svcIndutyCd4', 'svcIndutyCdNm4', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #46~50 4
             'svcIndutyCd5', 'svcIndutyCdNm5', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #51~55 5
             'svcIndutyCd6', 'svcIndutyCdNm6', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #56~60 6
             'svcIndutyCd7', 'svcIndutyCdNm7', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #61~65 7
             'svcIndutyCd8', 'svcIndutyCdNm8', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #66~70 8
             'svcIndutyCd9', 'svcIndutyCdNm9', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #71~75 9
             'svcIndutyCd10', 'svcIndutyCdNm', 'storCo', 'thsmonSelngCo', 'thsmonSelngAmt', #76~80 10

             'flpopCo', 'repopCo', 'wrcPopltnCo', #81~83
             'flpopCo', 'repopCo', 'wrcPopltnCo', #84~86

             'entrprsLtrsCo', 'entrprsSmlpzCo', 'entrprsEtcCo', 'pblofcCo', 'bankCo', 'hsptlCo', 'schCo', 'distbCo', 'clturCo', 'stayngFcltyCo', 'viatrFcltyCo'] #87~97

# http://golmok.seoul.go.kr/sgmc/reprt/get_rpct0104.json?trdarNo=13126&trdarSeCd=A&svcIndutyCd=CS100001&upperSvcIndutyCd=CS10000&stdrYmCd=201708

svcInduty = ['한식음식점', '중국집', '일식집', '양식집', '분식집', '패스트푸드', '치킨집', '제과점', '커피음료', '호프간이주점']


def find_exception(list,res,num) :
    if res == [] :
        for j in num :
            list.append("0")


def val(trCd,IndutyCd) :





    answer = []

    url1 = "https://golmok.seoul.go.kr/sgmc/reprt/get_rpct0101.json"
    url2 = "https://golmok.seoul.go.kr/sgmc/reprt/get_rpct0102.json"
    url3 = "https://golmok.seoul.go.kr/sgmc/reprt/get_rpct0103.json"
    url4 = "https://golmok.seoul.go.kr/sgmc/reprt/get_rpct0104.json"

    upperSvcIndutyCd = 'CS10000'

    induty = upperSvcIndutyCd + str(IndutyCd)

    if(IndutyCd == 10) :
        induty = "CS100010"


    params = {
        'trdarNo' : str(trCd),
        'trdarSeCd' : 'A',
        'svcIndutyCd' : induty,
        'upperSvcIndutyCd' : upperSvcIndutyCd,
        'stdrYmCd' : '201708'
    }

    params2 = {
        'svcSeCd' : 'CS',
        'upperSvcIndutyCd' : 'CS100000',
        'trdarNo' : str(trCd),
        'trdarSeCd' : 'A',
        'svcIndutyCd' : induty,
        'stdrYmCd' : '201708'
    }

    json_string1 = requests.get(url1,params=params).text
    json_string2 = requests.get(url2,params=params2).text
    json_string3 = requests.get(url3,params=params).text
    json_string4 = requests.get(url4,params=params).text

    result_dict1 = json.loads(json_string1)
    result_dict2 = json.loads(json_string2)
    result_dict3 = json.loads(json_string3)
    result_dict4 = json.loads(json_string4)

    result010102 = result_dict1['rpct010102']
    res010102 = result010102['rows']
    if res010102.__len__() == 0 :
        return None

    for data in res010102:
        answer.append("201708")
        answer.append(str(data[attribute[1]]))
        answer.append(str(data[attribute[2]]))
        answer.append(upperSvcIndutyCd + str(IndutyCd))
        answer.append(svcInduty[IndutyCd-1])

    result010103 = result_dict1['rpct010103']
    res010103 = result010103['rows']
    if res010103 == [] :
        answer.append("0")
        answer.append("0")
        answer.append("")
    else :
        for data in res010103 :
            answer.append(str(data[attribute[5]]))
            answer.append(str(data[attribute[6]]))
            answer.append(str(data[attribute[7]]))


    result010104 = result_dict1['rpct010104']
    res010104 = result010104['rows']
    if res010104 == [] :
        answer.append("0")
    else :
        for data in res010104 :
            answer.append(str(data[attribute[8]]))

    result010106 = result_dict1['rpct010106']
    res010106 = result010106['rows']
    if res010106 == [] :
        answer.append("")
        answer.append("")
        answer.append("0")
        answer.append("")
        answer.append("")
        answer.append("0")
        answer.append("")
        answer.append("0")
    else :
        for data in res010106:
            answer.append(str(data[attribute[9]]))
            answer.append(str(data[attribute[10]]))
            answer.append(str(data[attribute[11]]))
            answer.append(str(data[attribute[12]]))
            answer.append(str(data[attribute[13]]))
            answer.append(str(data[attribute[14]]))

            if not data.get(attribute[15]):
                attr15 = "0"
            else :
                attr15 = str(data[attribute[15]])
            answer.append(attr15)

            if not data.get(attribute[16]):
                attr16 = ""
            else :
                attr16 = str(data[attribute[16]])
            answer.append(attr16)


    result010113 = result_dict1['rpct010113']
    res010113 = result010113['rows']
    if res010113 == [] :
        answer.append("0")
        answer.append("0")
        answer.append("0")
        answer.append("0")
    else :
        for data in res010113:
            attr17 = "0"
            # print("ddd")
            if not data.get('beingRt'):
                None
                # print("no")
            else :
                attr17 = str(data['beingRt'])
                # print("yes")
            answer.append(attr17)
        #17~20


    result010203 = result_dict2['rpct010203']
    res010203 = result010203['rows']
    # print(res010203.__len__())

    if res010203.__len__() != 3 :
        for data in res010203:
            answer.append(str(data[attribute[21]]))
            answer.append(str(data[attribute[22]]))
            answer.append(str(data[attribute[23]]))
        for i in range(3-res010203.__len__()) :
            answer.append("0")
            answer.append("0")
            answer.append("0")
    else :
        for data in res010203:
            answer.append(str(data[attribute[21]]))
            answer.append(str(data[attribute[22]]))
            answer.append(str(data[attribute[23]]))
        #21~29



    result010212 = result_dict2['rpct010212']
    res010212 = result010212['rows']
    if res010212 == [] :
        answer.append("0")
    else :
        for data in res010212:
            answer.append(str(data[attribute[30]]))
            break
        #30



    result010206 = result_dict2['rpct010206']
    res010206 = result010206['rows']
    for i in range(10):
        for data in res010206:
            check = 0
            # if str(data[attribute[10]]) == "CS1000"+str(i+1) :
            #     check = 2
            if (str(data[attribute[31]]) == (upperSvcIndutyCd + str(i+1))) or (str(data[attribute[31]]) == "CS1000"+str(i+1)):
                check = 1
                break
        if check == 1:
            answer.append(str(data[attribute[31]]))
            answer.append(str(data[attribute[32]]))
            answer.append(str(data[attribute[33]]))
            answer.append(str(data[attribute[34]]))
            answer.append(str(data[attribute[35]]))
        else:
            if str(data[attribute[31]]) == "CS1000"+str(i+1) :
                answer.append("CS100010")
            else :
                answer.append(upperSvcIndutyCd + str(i +1))
            answer.append(svcInduty[i])
            answer.append("0")
            answer.append("0")
            answer.append("0")
            #31~80

    result010302 = result_dict3['rpct010302']
    res010302 = result010302['rows']
    if res010302 == [] :
        answer.append("0")
        answer.append("0")
        answer.append("0")
        answer.append("0")
        answer.append("0")
        answer.append("0")
    else :
        for data in res010302:
            answer.append(str(data[attribute[81]]))
            answer.append(str(data[attribute[82]]))
            answer.append(str(data[attribute[83]]))
        # 81~86



    result010411 = result_dict4['rpct010411']
    res010411 = result010411['rows']
    for data in res010411 :
        answer.append(str(data[attribute[87]]))
        answer.append(str(data[attribute[88]]))
        answer.append(str(data[attribute[89]]))
        answer.append(str(data[attribute[90]]))
        answer.append(str(data[attribute[91]]))
        answer.append(str(data[attribute[92]]))
        answer.append(str(data[attribute[93]]))
        answer.append(str(data[attribute[94]]))
        answer.append(str(data[attribute[95]]))
        answer.append(str(data[attribute[96]]))
        answer.append(str(data[attribute[97]]))


    return answer



# def find_null() :



OpenInSeoul = []
#11947,11997 1 //
#11997,12047 2 //
#12047,12097 3 //
#12097,12147 4 //
#12147,12197 5 //
#12197,12247 6 //
#12247,12297 7 // 까지
#12297,12347 8 //02-1
#12347,12397 9 //02-2
#12397,12447 10 //02-3
#12447,12497 11 //4
#12497,12547 12 //5
#12547,12597 13 //6
#12597,12647 14 // 까지
#12647,12697 15 //
#12697,12747 16 //
#12747,12797 17 //
#12797,12847 18 //
#12847,12897 19 //
#12897,12947 20 //
#12947,12997 21 // 까지
#12997,13047 22 //4-1
#13047,13097 23 //2
#13097,13147 24 //3
#13147,13197 25 //4
#13197,13247 26 //5
#13247,13297 27 //6
#13297,13347 28 //7
#13347,13397 29 //5-1
#13397,13447 30 //2
#13447,13497 31 //3
#13497,13547 32 //
#13547,13597 33 //5
#13597,13652 34 //6

#13651까지 데이터 
#13502 같은 에러


for i in range(11947,13652):
    value = val(i, 2)
    if value == None :
        None
    else :
        for k in range(value.__len__()) :
            file_data[arr[k]] = value[k]
            print(k,"번째 ",value[k])

        OpenInSeoul.append(file_data)
        file_data = {}

    print(i, " OK")

print(json.dumps(OpenInSeoul,ensure_ascii=False, indent="\t"))

with open('Dataset2.json','w',encoding="utf-8") as make_file:
    json.dump(OpenInSeoul, make_file, ensure_ascii=False, indent="\t")