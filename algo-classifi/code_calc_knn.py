# calculate distance of features
def calc_distance(feature1, feature2, turn=4):
    tmp = 0
    for i in range(turn):
        tmp += (feature1[i] - feature2[i]) ** 2
    return tmp**0.5

def knn(lst_predict, k):
    # read file
    f = open('/home/lnphong/Documents/D-soft/Intern/Machine_Learning/iris-dataset/archive/IRIS.csv','r')
    data = f.read()

    # format data
    data_split = data.split('\n')
    data_split.pop(0)
    name_flower = []
    feature = []
    for i in range(len(data_split)):
        tmp_lst = []
        lst = data_split[i].split(',')
        name_flower.append(lst[-1])
        for i in range(len(lst) - 1):
            tmp_lst.append(float(lst[i]))
        feature.append(tmp_lst)
    feature.pop(-1)
    name_flower.pop(-1)
    lst_flower = [[]]
    for i,val in enumerate(name_flower):
        tmp = calc_distance(lst_predict, feature[i])
        lst_flower.append([tmp,val])
    lst_flower.pop(0)
    lst_flower.sort()

    max_elems = 0
    flag = 0
    
    lst_name_flowers = []
    for i in range(k):
        lst_name_flowers.append(lst_flower[i][1])
    max_elems = 0
    flag = 0
    for i,val in enumerate(lst_name_flowers):
        cnt = lst_name_flowers.count(val)
        if cnt > max_elems:
            max_elems = cnt
            flag = i
    return lst_name_flowers[flag]
    
def main():
    predict = [6.3, 3.3, 6, 2.5]
    k = int(input())
    print('Flower: {}'.format(knn(predict, k)))

if __name__ == '__main__':
    main()