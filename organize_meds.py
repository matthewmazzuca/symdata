import csv

def organize_meds(filename, filename_two):

	meds = []
	href = {}
	title = {}
	other_names = {}
	desc = {}
	diseases = {}
	side_effects = {}	

	with open(filename, 'r') as f:

		for row in f:

			rows = row.split('\r')
			for i in rows:
				currentrow =  i.split('\t')


				if currentrow[0] in meds:
					if currentrow[1] in href[currentrow[0]]:
						pass
					else:
						href[currentrow[0]].append(currentrow[1])

					# #####################################

					if currentrow[2] in title[currentrow[0]]:
						pass
					else:
						title[currentrow[0]].append(currentrow[2])

					# #####################################

					if currentrow[3] in other_names[currentrow[0]]:
						pass
					else:
						other_names[currentrow[0]].append(currentrow[3])

					# #####################################

					if currentrow[4] in desc[currentrow[0]]:
						pass
					else:
						desc[currentrow[0]].append(currentrow[4])

					# #####################################

					if currentrow[5] == '':
						pass
					else:	
						diseases[currentrow[0]].append(currentrow[5])

					# #####################################

					if currentrow[6] == '':
						pass
					else:
						side_effects[currentrow[0]].append(currentrow[6])

					# #####################################


				else:
					meds.append(currentrow[0])
					href[currentrow[0]] = []
					title[currentrow[0]]= []
					other_names[currentrow[0]] = []
					desc[currentrow[0]] = []
					diseases[currentrow[0]] = []
					side_effects[currentrow[0]] = []
					

					href[currentrow[0]].append(currentrow[1])
					title[currentrow[0]].append(currentrow[2])
					other_names[currentrow[0]].append(currentrow[3])
					desc[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						diseases[currentrow[0]].append(currentrow[5])

					# #####################################

					if currentrow[6] == '':
						pass
					else:
						side_effects[currentrow[0]].append(currentrow[6])

					# #####################################


					
	f.close()

	# testing(title, other_names, diseases, side_effects, test, ages, age_freq, sex, sex_freq, race, race_freq, meds)
	with open(filename_two, 'w') as f:
		for item in meds:
			for i in range(max(len(diseases[item]), len(side_effects[item]))):
				temp_title = title[item][0]
				temp_other_names = other_names[item][0]
				temp_desc = desc[item][0]

				if not diseases[item]:
					temp_symp = ''
				else:
					temp_symp = diseases[item][0]
					diseases[item].pop(0)

				if not side_effects[item]:
					temp_percentage = ''
				else:
					temp_percentage = side_effects[item][0]
					side_effects[item].pop(0)


				f.write(temp_title + '\t' + temp_other_names + '\t' + temp_desc + '\t' + temp_symp + '\t' + temp_percentage + '\n')





def testing(title, other_names, diseases, side_effects, test, ages, \
		age_freq, sex, sex_freq, race, race_freq, meds):

	print "Title: ", title["Common cold"]
	print "Other names: ", other_names["Common cold"] 
	print "diseases: ", diseases["Common cold"]
	print "side_effects: ", side_effects["Common cold"]
	print "Test: ", test["Common cold"]
	print "Ages: ", ages["Common cold"]
	print "Age Freq", age_freq["Common cold"]
	print "Sex: ", sex["Common cold"]
	print "Sex Freq: ", sex_freq["Common cold"]
	print "Race: ", race["Common cold"]
	print "Race Freq: ", race_freq["Common cold"]
	print "Meds: ", meds["Common cold"]

	print len(diseases["Common cold"]) == len(side_effects["Common cold"])
	print len(ages["Common cold"]) == len(age_freq["Common cold"])
	print len(sex["Common cold"]) == len(sex_freq["Common cold"])
	print len(race["Common cold"]) == len(race_freq["Common cold"])

