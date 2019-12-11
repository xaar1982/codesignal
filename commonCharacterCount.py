def commonCharacterCount(s1, s2):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","q","x","y","z"]
    common_sum = 0
    num = 0
    
    for i in alphabet:
        s1_num = s1.count(i)
        s2_num = s2.count(i)
        num = min(s1_num,s2_num)
        common_sum+=num
        
    return common_sum
