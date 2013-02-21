tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

formatterR = 'formated by  : %r'
formatterS = 'formated by  : %s'
formatter = '%s'

print '%r %r' % (1, '2')

print tabby_cat
print formatterR % tabby_cat
print formatterS % tabby_cat
print persian_cat
print backslash_cat
print fat_cat