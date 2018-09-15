usr_input = input("Enter a State ")
state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                    'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
capital=state_dictionary.get(usr_input)
if capital == None:
    print("Unknown")
else:
    print(capital)
   