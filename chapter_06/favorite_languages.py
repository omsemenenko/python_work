favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")


# favorite_languages = ['jen', 'sarah', 'edward', 'phil', 'jim']
# friends = ['jen', 'john']

# for name in favorite_languages:
#     if name in friends:
#         print(f"{name.title()}, please, take a pool.")
#     else:
#         print(f"Thank you for your answer {name.title()}.")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }


# print("The following languages have been mentiones:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, that you for taking the pool.")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# for name in favorite_languages.keys():
#     print(name.title())

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")