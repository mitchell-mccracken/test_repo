import fnmatch

fn='2020-05-05.tsv'
x=0

if fnmatch.fnmatch(fn, '*[10-100]*') ==True:
    print ('file found')

else:
    print ('file not found')



'''

if fnmatch.fnmatch(fn, '*2020*')==True:
    if fnmatch.fnmatch(fn, '*[10-31]*') == True:
        if fnmatch.fnmatch(fn, '*[03-12]*') == True:
            print (fn)
        else:
            print ('files searched')
    else:
        print ('files searcher')
else:
    print ('no files found')
    

print(x)

'''
