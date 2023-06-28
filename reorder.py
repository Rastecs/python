def reorder(lst):
    return [lst[i] for i in range(0, len(lst), 2)] + [lst[i] for i in range(1, len(lst), 2)]