_text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than compalicated.
Flat is better than nested.
Sprase is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicity silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


#1
text=_text.replace('better','worse')
print (text)

#2
words=text.split()
filtered=[]
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print(filtered)

#3
swapcased=[a.swapcase() for a in filtered]
print(swapcased)

#4
print(sorted(swapcased))