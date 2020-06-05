def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i, x in enumerate(weights):
        if limit - x in weights:
            cache[i] = limit - x
    result = list(cache.items())
    result.sort(reverse=True)
    pair = [x[0] for x in result] if len(result) == 2 else None
    return pair


if __name__ == '__main__':
    weights_3 = [4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    print(answer_3)
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
    print(answer_4)
    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2)
    weights_1 = [9]
    answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
    print(answer_1)
