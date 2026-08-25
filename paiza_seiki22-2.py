import re

s = input()
match = re.search(r'(\d{2})\.(\d{2})', s)
if match:
    target = match.group()
    replace_word = target.replace('.','/')
    ans = s.replace(target,replace_word,1)
    print(ans)