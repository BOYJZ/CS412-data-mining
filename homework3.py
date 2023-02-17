def ord_prefixspan(input_file,min_support):
    input_seq=[]
    global fre
    fre=[]
    global fre_t
    fre_t=[]
    global alphabet
    #initialize alphabet
    alphabet=[]
    for i in range(26):
        alphabet.append(chr(i+97))
#input_file ->input_seq
    file=open(input_file)
    for line in file.readlines():
        input_seq.append(line.split(',')[1].replace('\n','').replace('<','').replace('>','').replace(' ',''))
    file.close()
    
    iteration('',input_seq,min_support)

    output={}
    for i in range(len(fre)):
        output[fre[i]]=fre_t[i]
    sorted(output.keys())
    print(output)
    return output

def iteration(pre_string,input_seq,min_support):
    return_flag=1
    for i in input_seq:
        if i!='':
            return_flag=0
    if return_flag==1:
        return
    
    #get the support of each character
    counter={}
    #calculate frequency of each character of alphabet
    for i in input_seq:
        for char in alphabet:
            if i.find(char)>=0:
                if char in counter:
                    counter[char]+=1
                else:
                    counter[char]=1
    
    
    #check if there is any frequent sequence, if not, return
    return_flag=1
    for character in counter:
        if counter[character]>=min_support:
            return_flag=0
    if return_flag==1:
        return 
    
    
    for character in counter:
        if counter[character]>=min_support:
            input_seq_copy=input_seq.copy()
            current_string=pre_string+character
            fre.append(current_string)
            fre_t.append(counter[character])
            #delete character from input_seq_copy
            for i in range(len(input_seq_copy)):
                if character in input_seq_copy[i]:
                    delete_index=input_seq_copy[i].find(character)
                else:
                    delete_index=len(input_seq_copy[i])
                input_seq_copy[i]=input_seq_copy[i][delete_index+1:]
            iteration(current_string,input_seq_copy,min_support)
            
ord_prefixspan('seqDB.txt',3)