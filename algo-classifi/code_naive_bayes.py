from sklearn.model_selection import train_test_split

def parse_data(data_path,features, labels):
    f = open(data_path)
    data = f.read() 
    data_split = data.split('\n')[1:-1]
    tmp_features = []
    for i in range(len(data_split)):
        lst_tmp = []
        tmp_features = data_split[i].split(',')
        labels.append(int(tmp_features[0]))
        for idx in range(1,len(tmp_features)):
            lst_tmp.append(int(tmp_features[idx]))
        features.append(lst_tmp)
    return features, labels


#==============================================================================


def probability_features(probability_number, features, labels):
    size_features = len(labels)
    for class_numbers in set(labels):
        cnt_numbers = labels.count(class_numbers)
        lst_tmp = []
        for idx_column in range(len(features[0])):
            tmp = 0
            for idx_row in range(len(labels)):
                if labels[idx_row] == class_numbers and features[idx_row][idx_column]:
                    tmp += 1
            lst_tmp.append(tmp / cnt_numbers)
        probability_number.append(lst_tmp)
    return


#==============================================================================


def predict(probability_number, feature, labels):
    lst_pred = []
    for class_numbers in set(labels):
        probability_number_pred = labels.count(class_numbers) / len(labels)
        for i in range(len(feature)):
            if feature[i] == 0:
                probability_number_pred *= (1 - probability_number[class_numbers][i])
            else:
                probability_number_pred *= probability_number[class_numbers][i]
        lst_pred.append(probability_number_pred)
    lst_sum = sum(lst_pred)
    lst_ans = []
    for i in range(len(lst_pred)):
        tmp = lst_pred[i] / lst_sum
        lst_ans.append([tmp, i])
    lst_ans = sorted(lst_ans)
    return lst_ans[len(lst_ans) - 1][1]


#==============================================================================


def predict_batch(probability_number, features, labels):
    pred_labels = []
    for feature in features:
        pred_labels.append(predict(probability_number, feature, labels))
    return pred_labels


#==============================================================================


def main():
    data_path = r'mnist_test.csv'
    features = []
    labels = []
    parse_data(data_path, features, labels)
    train_data, test_data, train_label, test_label = train_test_split(features, labels, test_size=0.1)
    probability_number = []
    probability_features(probability_number, train_data, train_label)
    preds = predict_batch(probability_number, test_data, test_label)
    correct = 0 
    for i in range(len(preds)):
        if preds[i] == test_label[i]:
            correct += 1
    print("Accuracy: {}%".format(100 * (correct / len(test_label))))


#==============================================================================


if __name__ == "__main__":
    main()
