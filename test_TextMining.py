
# coding: utf-8

# In[2]:


#import pyodbc
import pandas as pd
import re
df = pd.read_csv("C:\\Users\\vzhang1\Documents\\tables\Close_Description.csv",header=0) 
df.head(10)


# In[6]:


pd.set_option('display.max_columns', None)  

textdata = list(df['Description'])
print(textdata[7]) ##Description as an email
len(textdata)


# In[73]:


#RE For Data Cleaning
textdata= [[re.sub(r'(\n)+|(\xa0)+|(\r)+', ' ',item.lower())] for item in textdata]
textdata= [[re.sub(r'[^\w\s]', ' ',item[0])] for item in textdata]
textdata= [[re.sub(r' +', ' ',item[0])] for item in textdata]


# In[74]:


'''
for i in range(4):
    print (textdata[i])'''


# In[75]:


#colelction of all words
collection_words = [" ".join(textdata[i]).split(" ") for i in range(len(textdata))]
#print(collection_words)
res = []
_ = 0
while _ < len(textdata):
    res += collection_words[_]
    _ += 1

res
    


# In[76]:


import matplotlib.pyplot as plt
import collections as CT

plt.hist(res, bins='auto')
plt.title("Histogram with 'auto' bins")
plt.show()
count = CT.Counter(res)
#print (sorted(set([i for i in res if res.count(i)>5])))


# In[77]:


sorted(count, key = lambda x: count[x])[::-1]


# In[78]:


#try nltk for word token
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
from nltk import word_tokenize, pos_tag, ne_chunk
sentence = 'Exam completed the commitment showing lots 15 16 but only one parcel for lot 16 title clearance initially spoke with the consumer on 2 1 the consumer stated that they had a deed prepared recorded that intended to grant lot 15 to his daughter laura preston this deed included the correct legal description in the body of the deed but the attached exhibit for both lots 15 16 the consumer verified that title source could prepare a deed to correct this situation and transfer lot 16 back to the consumer tc ordered a deed that incorrectly included the entire legal for lots 15 16 should have included lot 16 only and emailed the deed to laura preston to execute the legal description was hand corrected by laura and taken directly to the county to be recorded instead of being returned to title source for review 17 for deed recording was not removed from the cd the closing was pushed back twice on the day of closing first for delay in receiving closing docs from chase and the second for trouble securing a notary the consumer called from closing indicating that the legal description in the closing package was still incorrect listing both lots the file was placed in delay for hand corrections to the legal description and missing qcd notes from tc were not clear that the consumer had the deed recorded on their own and it had already been added to title the legal was corrected after closing and attached to the dot and sent to the county for recording sent coaching to exam title clearance and typing leadership '
print (ne_chunk(pos_tag(word_tokenize(sentence))))


# In[1]:


#allwords
strall = ''
for _ in textdata:
    strall += _[0]
#strall


# In[80]:


'''from collections import Counter
strall = ' '
for _ in range(len(textdata)):
    strall.join(textdata(_))
unique_words = list(set(" ".join(textdata).split(" ")))
def make_matrix(text, vocab):
    matrix = []
    for item in headlines:
        # Count each word in the headline, and make a dictionary.
        counter = Counter(headline.split())
        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w,0) for w in vocab]
        matrix.append(row)
    df = pd.DataFrame(matrix)
    df.columns = unique_words
    return df

print(make_matrix(headlines, unique_words))'''



# In[84]:


def findkeyword(string, words):
    return ([word for word in words if string.find(word) > -1]) #BOYER MOORE o(n+m+|Σ|)
i = 7
print(textdata[i][0])
print(findkeyword(textdata[i][0], [word.lower() for word in word_ProductCode]))
print(findkeyword(textdata[i][0], [word.lower() for word in word_documents]))
print(findkeyword(textdata[i][0], [word.lower() for word in word_teams]))


# In[15]:


#import nltk
#nltk.download('wordnet')

#find synonym
from nltk.corpus import wordnet as wn

print("Category name:", wn.synsets('angry'))

print("Synonyms:", wn.synset('angry.s.02').lemma_names())


# In[ ]:


ll = [1,2,3,3,3,2]
ll


# In[63]:


l = ['you are a good person','person']
m = list(map(lambda x: x.split(), l))
print (list(m))
print (list(set([5,5,3,4,6])))
def findkeyword(string, objs):
    return ([obj for obj in objs if string.find(obj) > -1])
findkeyword('you are a sb', ['sb','you','he'])
target = 'No sucker is a good sucker'
target.replace('sucker','')
#['fucker'] += 'sucker'


# In[7]:


def findkeyword(string, objs):
    return ([obj for obj in objs if string.find(obj) > -1]) #BOYER MOORE o(n+m+|Σ|)

#we will want to grab objs with most words first
from collections import defaultdict
def SearchOrder(List_Of_Obj, target):
    list_of_length = list(map(lambda x: len(x),list(map(lambda x: x.split(), List_Of_Obj))))
    dic = defaultdict(list)
    for index, item in enumerate(list_of_length):
        dic[item].append(List_Of_Obj[index])
    #t_of_length, dic)
    
    list_of_length_1 = list(set(list_of_length))
    res = []
    while len(list_of_length_1):
        length = list_of_length_1.pop()
        obj_to_search = dic[length]
        print (obj_to_search)
        searched = findkeyword(target.lower(), [obj.lower() for obj in obj_to_search])
        if searched:
            res.append(searched)
        print (searched)
        for _ in searched:
            target = target.replace(_ , '')
    return [item[0] for item in res]
        
        
    
SearchOrder(['you are a good person','He is a just bad','person','sb is always sb','you','good person','are','good'],
            'You are not a good person')


# In[94]:


#breaking by punctuations(,.?!)
import re
sample = 'The consumer was very confused and was unwilling to provide his full divorce decree. On 5/20 he was advised multiple times that the entire document was required. It appears as though the consumer was upset with Machelle Parker, as she was unable to clearly communicate to the consumer the reason for the requirement. Leadership has confirmed that coaching has been provided to Machelle.  The consumer is transferred to the Team Captain, Brittney Vaughn who provides the same information; still frustrated Andrew requests that the Team leader contact him. Brittney reaches out to Team Leader, Chris Layton via phone advising him of the issue and requests that he e-mail the consumer. Brittney provides detailed notes in ATLAS noting it for leadership review; Brittney states in her note that she advised the consumer   leadership would reach out via an email. This is a Valid NRCC, no recording of outgoing communication to Andrew was located.'
def sentence_break(s):
    s_new = re.sub(r'[.|,|?|!|;|:]+[\s]*','^',s)
    return [item for item in s_new.split('^') if item != '']

sentence_break(sample)


# In[103]:


def Position_Matrix(sentences):
    matrix = [[] for sentence in sentences]
    for i, item in enumerate(sentences):
        length = len(item.split())
        #print (length)
        for _ in range(length):
            matrix[i].append(0)
        for j, word in enumerate(item.split()):
            matrix[i][j] = format(j*1.0/(length-1),'.2f')
    return matrix
            

Position_Matrix(['1223 33 33 33 333333333333333333333','2 4'])


# In[9]:


from difflib import SequenceMatcher

s = SequenceMatcher(lambda x: x == " ",
                'Cali is good',
                'California is good')

print(round(s.ratio(), 3))
                    
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)

    
    
import re    
def Name_Abbr_Detector(name):
    #abbr first name/last name/middle name but is not allowed to abbr all
    re.sub(r'[^/s/w]]*','',name)
    if len(name.split()) == 1:
        name_to_search = name[0].upper() + name.lower()[1:]
    elif len(name.split()) == 2: # no middle name
        first = name.split()[0]
        last = name.split()[-1]
        name_to_search = [first[0].upper + ' ' + last, first+ ' ' +last[0]]
    elif len(name.split()) == 3:
        name_to_search = []
        for pos in range(len(name.split()):
            name_to_search.append(name.split()[:pos] + name.split()[pos][0].uppper + name.split()[pos+1:])
    return name_to_search
        


# In[52]:


#preliminary design
import re    
def Name_Abbr_Detector(name):
    #abbr first name/last name/middle name but is not allowed to abbr all
    re.sub(r'[^/s/w]]*','',name)
    if len(name.split()) == 1:
        name_to_search = name[0].upper() + name.lower()[1:]
    elif len(name.split()) == 2: # no middle name
        first = name.split()[0]
        last = name.split()[-1]
        print (first, last)
        name_to_search = [first[0].upper() + ' ' + last, first +  ' ' + last[0].upper()]
    elif len(name.split()) == 3:
        name_to_search = []
        for pos in range(len(name.split())):
            
            temp_name = name.split()[:pos] + [name.split()[pos][0].upper()] + name.split()[pos+1:]
            s=''
            for item in temp_name:
                s +=  ' ' + item
            name_to_search.append(s)
    return name_to_search
Name_Abbr_Detector('Victor Henry Zhang')            
    


# In[40]:


'Victor Henry Handsome Zhang'.split()[:2] +['Zhang']


# In[ ]:


#advanced design
def Name_Abbr_Detector_Advanced(name):
    n = length(name.split())
    k = n - 1 #No.of Initials


# In[53]:


[1,2,3][:0]


# In[18]:


import inspect #The basic idea is to find
    #the longest contiguous matching subsequence that contains no "junk"
    #elements (R-O doesn't address junk)
    #As a rule of thumb, a .ratio() value over 0.6 means the
    #sequences are close matches
lines = inspect.getsourcelines(SequenceMatcher)
print("".join(lines[0]))


# In[11]:


#from abresolver import Text

