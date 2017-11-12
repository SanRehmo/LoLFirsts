import sys, json
from sklearn import tree

RELEVANT_STATS = [
	'firstBlood'
	'firstTower',
	'firstInhibitor',
	'firstBaron',
	'firstDragon',
	'firstRiftHerald'
]

def get_input():

	def map_input(input):
		if input == 'y':
			return 1.0
		return 0.0

	def ask_yes_or_no(text):
		answer = ''
		while answer not in ['y', 'n']:
			answer = input('Did you get ' + text + "? ")
		return answer
	
	print("Your answer must be either 'y' or 'n'.")
	user_inputs = [map_input(ask_yes_or_no(stat)) for stat in RELEVANT_STATS]

	return user_inputs

def extract_data():

	matches = []
	for i in range(1, 11):
		with open('riot_games/matches' + str(i) + '.json', encoding = "ISO-8859-1") as json_data:
		    match_data = json.load(json_data)
		    matches.extend([match for match in match_data['matches']])

	def convert_bool(boolean):
		return 1.0 if boolean else 0.0

	def convert_win(win):
		return 1.0 if win == 'Win' else 0.0

	data = []
	labels = []
	for match in matches:
		for team in match['teams']:
			data.append([convert_bool(team[stat]) for stat in RELEVANT_STATS])
			labels.append(convert_win(team['win']))

	return (data, labels)

def train_descision_tree(X, Y):

	X_train = X[:-600]
	X_pred = X[-600:]

	Y_train = Y[:-600]
	Y_pred = Y[-600:]

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X_train, Y_train)

	print("Accuracy: {}".format(clf.score(X_pred, Y_pred)))

	return clf

if __name__ == "__main__":
   
	X, Y = extract_data()
	clf = train_descision_tree(X, Y)
	user_inputs = get_input()

	print(clf.predict([user_inputs]))
