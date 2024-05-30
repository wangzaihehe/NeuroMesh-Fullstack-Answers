def min_subsequences(source, target):
    subseq_count = 0
    source_len = len(source)

    while target:
        temp = ''
        source_index, target_index = 0, 0

        while source_index < source_len and target_index < len(target):
            if source[source_index] == target[target_index]:
                temp += target[target_index]
                target_index += 1
            source_index += 1

        if not temp:
            return -1

        subseq_count += 1
        target = target[len(temp):]

    return subseq_count

#Test cases
print(min_subsequences("abc", "abcbc"))  
print(min_subsequences("abc", "acdbc"))  
print(min_subsequences("xyz", "xzyxz"))  
