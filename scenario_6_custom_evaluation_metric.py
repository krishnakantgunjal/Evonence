def weighted_accuracy(y_true, y_pred):
    total_weight = 0
    correct_weight = 0

    for yt, yp in zip(y_true, y_pred):
        if yt == 1:
            weight = 2
        else:
            weight = 1

        total_weight += weight

        if yt == yp:
            correct_weight += weight

    return correct_weight / total_weight
