import MySQLdb
from math import sqrt

def pearson(data, name1, name2):
    sumX=0
    sumY=0
    sumPowX=0
    sumPowY=0
    sumXY=0
    count=0
    for i in data[name1]:
        if i in data[name2]:
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
    result = 0
    try:
        result = (sumXY-((sumX*sumY)/count))/sqrt((sumPowX-(pow(sumX,2)/count))*(sumPowY-(pow(sumY,2)/count)))
    except:
        result = 0
    return result

def euclidean(data, name1, name2):
    sum=0
    for i in data[name1]:
        if i in data[name2]:
            sum+=pow(data[name1][i]- data[name2][i],2)
    return 1/(1+sqrt(sum))

def match_users(data, name, index=5, sim1=pearson, sim2=euclidean):
    li=[]
    for i in data: 
        if name!=i:
            li.append((sim1(data,name,i)+sim2(data,name,i),i))
    li.sort() 
    li.reverse() 
    return li[:index]

def get_Recommend (data,person):
    result = match_users(data, person ,len(data))
    print(result)
    score=0
    li=[]
    score_dic={}
    sim_dic={} 
    for sim,name in result:
        if sim < 0 : continue 
        for cloth in data[name]: 
            if cloth not in data[person]:
                score+=sim*data[name][cloth]
                score_dic.setdefault(cloth,0) 
                score_dic[cloth]+=score 
                sim_dic.setdefault(cloth,0) 
                sim_dic[cloth]+=sim
            score=0  
            
    for key in score_dic: 
        if sim_dic[key] is not 0:
            score_dic[key]=score_dic[key]/sim_dic[key]
            li.append((score_dic[key],key))
    li.sort()
    li.reverse()
    return li


class Recommend():
    def __init__(self):
        self.result = 0
    
    def get_recommend_list(self, name):
        user_eval = {}
        connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT userid, title, score FROM service_review")
            for row in cursor:
                if row[0] not in user_eval:
                    user_eval[row[0]] = {}        
                    user_eval[row[0]][row[1]] = row[2]
                elif row[0] in user_eval:
                    user_eval[row[0]][row[1]] = row[2]
        except MySQLdb._exceptions.OperationalError:
            print("error occurred")
        
        recommend_result = []
        result_list = get_Recommend(user_eval, name)
        print(result_list)
        i = 0
        for li in result_list:
            recommend_result.append([])
            recommend_result[i].append(li[0])
            recommend_result[i].append(li[1])
            st = "SELECT image, designer, price FROM service_review WHERE title=" + "'" + li[1] + "'"
            try:
                cursor.execute(st)
                for row in cursor:
                    recommend_result[i].append(row[0])
                    recommend_result[i].append(row[1])
                    recommend_result[i].append(row[2])
                    break
            except MySQLdb._exceptions.OperationalError:
                print("error occurred")
            i=i+1
        
        '''
        recommend = {}
        categ = ""

        for rl in recommend_result:        
            st = "SELECT category FROM clothes WHERE name=" + "'" + rl[1] + "'"
            try: 
                cursor.execute(st)
                for row in cursor:
                    categ = row[0]
                    break
            except MySQLdb._exceptions.OperationalError:
                print("error occurred")
            if categ not in recommend:
                recommend[categ] = {}

            recommend[categ][rl[1]] = {} # rl[1] 이 title일 경우
            recommend[categ][rl[1]]['image'] = rl[2]
            recommend[categ][rl[1]]['designer'] = rl[3]
            recommend[categ][rl[1]]['score'] = rl[0]
        '''
        return recommend_result

