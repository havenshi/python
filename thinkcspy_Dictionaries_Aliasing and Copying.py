opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

# alias



acopy = opposites.copy()
acopy['right'] = 'left'    # does not change opposites

# copy
