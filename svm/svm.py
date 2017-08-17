import re
import math
from collections import Counter
import pickle
import gib_detect_train
from sklearn import svm
from sklearn.externals import joblib


def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False


def get_feature(domain):
    arr=domain.split('\n')
    domain=arr[0]
    lens=len (domain)
    separator=0.0
    bt_alpha=0.0
    max_alpha=0.0
    digit=0.0
    bt_digit=0.0
    max_digit=0.0
    special=0.0
    trans=0.0
    bt_separator=0.0
    bt=0.0
    flag=0
    upper=0.0
    hasip=0.0
    for i in range (lens):
        try:
            x=domain[i]
            #print x
            bt=bt+1
            if (bt_alpha>max_alpha):
                max_alpha=bt_alpha
            if (bt_digit>max_digit):
                max_digit=bt_digit

            if (x=='-'):
                bt_alpha=0.0
                bt_digit=0.0
                separator=separator+1
                if (bt-1>bt_separator and flag==1):
                    bt_separator=bt-1
                bt=0.0
                flag=1
            elif (x.isalpha()):
                bt_alpha=bt_alpha+1
                bt_digit=0

            elif (x.isdigit()):
                digit=digit+1
                bt_digit=bt_digit+1
                bt_alpha=0.0
                j=i+1
                while (j<=lens)and(domain[j].isdigit()or domain[j]=='.'):
                    j=j+1
                    if checkip(domain[i:j]):
                        hasip=1.0

            elif (not(x=='.')):
                #print x
                bt_alpha=0.0
                bt_digit=0.0
                special=special+1
            else:
                bt_alpha=0.0
                bt_digit=0.0
            if (x.isupper()):
                upper=upper+1
            if ((i>=1) and (not(x=='.'))):
                j=i-1
                while(domain[j]=='.'):
                    j=j-1
                if ((x.isalpha() and domain[j].isdigit()) or (x.isdigit() and domain[j].isalpha())):
                    trans=trans+1
        except :
            print 'URLError:'+domain
    f_len = float(len(domain))
    count = Counter(i for i in domain).most_common()
    entropy = -sum(j/f_len*(math.log(j/f_len)) for i,j in count)
    model_data = pickle.load(open('/home/ubuntu/svm/gib_model.pki', 'rb'))
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    gib_value = int(gib_detect_train.avg_transition_prob(domain, model_mat) > threshold)

    if (not lens==0):
        rates=float(digit)/float(lens)
        trans_rates=float(trans)/float(lens)
    else:
        rates=0.0
        trans_rates=0.0
    #print trans
    #print lens,hasip,entropy,separator,special,digit,rates,trans_rates,upper,bt_separator,max_digit,max_alpha
    return (float (lens),hasip,entropy,separator,special,digit,rates,trans_rates,upper,bt_separator,max_digit,max_alpha,float (gib_value))


def loadWhite(whiteList):
    dataMat = []
    fr = open(whiteList )
    fw = open('whiteFeaturesAll.txt','w')
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        domain = lineArr[0]
        (lens,hasip,entropy,separator,special,digit,rates,trans_rates,upper,bt_separator,max_digit,max_alpha,gib_value)=get_feature(domain)
        for i in range(9):
            fw.write(lineArr[i]+'\t')
        fw.write(str(lens)+'\t')
        fw.write(str(hasip)+'\t')
        fw.write(str(entropy)+'\t')
        fw.write(str(separator)+'\t')
        fw.write(str(special)+'\t')
        fw.write(str(digit)+'\t')
        fw.write(str(rates)+'\t')
        fw.write(str(trans_rates)+'\t')
        fw.write(str(upper)+'\t')
        fw.write(str(bt_separator)+'\t')
        fw.write(str(max_digit)+'\t')
        fw.write(str(max_alpha)+'\t')
        fw.write(str(gib_value)+'\t')
        fw.write('1'+'\n')


def loadBlack(blackList):
    dataMat = []
    fr = open(blackList)
    fw = open('blackFeaturesAll.txt','w')
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        domain = lineArr[0]
        (lens,hasip,entropy,separator,special,digit,rates,trans_rates,upper,bt_separator,max_digit,max_alpha,gib_value)=get_feature(domain)
        for i in range(9):
            fw.write(lineArr[i]+'\t')
        fw.write(str(lens)+'\t')
        fw.write(str(hasip)+'\t')
        fw.write(str(entropy)+'\t')
        fw.write(str(separator)+'\t')
        fw.write(str(special)+'\t')
        fw.write(str(digit)+'\t')
        fw.write(str(rates)+'\t')
        fw.write(str(trans_rates)+'\t')
        fw.write(str(upper)+'\t')
        fw.write(str(bt_separator)+'\t')
        fw.write(str(max_digit)+'\t')
        fw.write(str(max_alpha)+'\t')
        fw.write(str(gib_value)+'\t')
        fw.write('-1'+'\n')


def loadReal(realList):
    dataMat = []
    x = 0
    fr = open(realList)
    fw = open('realFeaturesAll.txt','w')
    for line in fr.readlines():
        lineArr = line.strip().split(' ')
        domain = lineArr[0]
        (lens,hasip,entropy,separator,special,digit,rates,trans_rates,upper,bt_separator,max_digit,max_alpha,gib_value)=get_feature(domain)

        if len(lineArr) >= 9:
            for i in range(9):
                fw.write(lineArr[i]+'\t')
            fw.write(str(lens)+'\t')
            fw.write(str(hasip)+'\t')
            fw.write(str(entropy)+'\t')
            fw.write(str(separator)+'\t')
            fw.write(str(special)+'\t')
            fw.write(str(digit)+'\t')
            fw.write(str(rates)+'\t')
            fw.write(str(trans_rates)+'\t')
            fw.write(str(upper)+'\t')
            fw.write(str(bt_separator)+'\t')
            fw.write(str(max_digit)+'\t')
            fw.write(str(max_alpha)+'\t')
            fw.write(str(gib_value)+'\n')


def loadData():
    fi = open('whiteFeaturesAll.txt','r')
    fw = open('dnsData3.txt','w')
    features = []
    labels = []
    index = 0
    for f in fi:
        lineArr = f.strip().split('\t')
        temp = []
        for i in range(1,22):
            temp.append(float(lineArr[i]))
        features.append(temp)
        if index >= 1400:
            fw.writelines(f)
        labels.append(int(lineArr[22]))
        index += 1
        if index == 2100:
            break
    fi.close()

    fi = open('blackFeaturesAll.txt','r')
    index = 0
    for f in fi:
        if index >= 1400:
            fw.writelines(f)
        lineArr = f.strip().split('\t')
        temp = []
        for i in range(1,22):
            temp.append(float(lineArr[i]))
        features.append(temp)
        labels.append(int(lineArr[22]))
        index += 1
        if index == 2100:
            break
    fi.close()
    fw.close()
    #clf = svm.SVC()
    #clf.fit(features,labels)
    #joblib.dump(clf, "train_model.m")

def predict_domain(feature):
	clf = joblib.load("/home/ubuntu/svm/train_model.m")
	features = [float(feature[1])]
	for i in range(2,22):
                features.append(float(feature[i]))
	return clf.predict([features])

	

def predictReal():
    fi = open('feature','r')
    fw = open('toVirustotal.txt','w')
    fw1 = open('malFeatures.txt','w')
    clf = joblib.load("train_model.m")
    features = []
    index = 0
    for f in fi:
        try:
            line = f.strip().split('\t')
            features = [float(line[1])]
            for i in range(2,22):
                features.append(float(line[i]))
            if (clf.predict([features]) == -1):
                fw.writelines(line[0])
                fw1.writelines(f)
                fw.writelines('\n')
            index = index + 1
        except:
            print index

    fi.close()


    fw.close()
    fw1.close()


if __name__ == '__main__':
    predictReal()










