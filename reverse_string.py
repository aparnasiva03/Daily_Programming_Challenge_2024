def reverse_words(s):
    words = s.strip().split()

    reversed_words = words[::-1]
    
    result = ' '.join(reversed_words)
    
    return result


print(reverse_words("the sky is blue"))  
print(reverse_words("  hello world  "))  
print(reverse_words("a good   example"))  
print(reverse_words("    "))  
print(reverse_words("word"))  
