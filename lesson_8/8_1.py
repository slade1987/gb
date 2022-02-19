import re

def email_parse(txt):
    re_email = re.compile(r'([a-zA-Z]{1}[^..&?]{0,}[@]\S{0,}[.][a-zA-Z]{2,3})')
    if not re_email.match(txt):
        raise ValueError
    else:
        pars_string = str(re_email.findall(txt)[0]).split('@')
        emal_diction['username'] = pars_string[0]
        emal_diction['domain'] = pars_string[1]


emal_diction ={}
try:
    email_parse("paran87@mail.ru")
except ValueError:
    print("e-mal указан неверно")

print(emal_diction)