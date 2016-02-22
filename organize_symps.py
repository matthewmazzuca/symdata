import csv

def organize_symps(filename, filename_two):

	symptoms = []
	href = {}
	title = {}
	other_names = {}
	desc = {}
	causes = {}
	percentages = {}
	related = {}
	related_p = {}
	test = {}
	meds = {}
	ages = {}
	age_freq = {}
	sex = {}
	sex_freq = {}
	race = {}
	race_freq = {}
	

	with open(filename, 'r') as f:

		for row in f:

			rows = row.split('\r')
			for i in rows:
				currentrow =  i.split('\t')


				if currentrow[0] in symptoms:
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
						causes[currentrow[0]].append(currentrow[5])

					# #####################################

					if currentrow[6] == '':
						pass
					else:
						percentages[currentrow[0]].append(currentrow[6])

					# #####################################

					if currentrow[7] == '':
						pass
					else:
						related[currentrow[0]].append(currentrow[7])

					# #####################################

					if currentrow[8] == '':
						pass
					else:
						related_p[currentrow[0]].append(currentrow[8])

					# #####################################

					if currentrow[9] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[9])

					# #####################################

					if currentrow[10] == '':
						pass
					else:
						meds[currentrow[0]].append(currentrow[10])

					# #####################################

					if currentrow[11] == '':
						pass
					else:
						ages[currentrow[0]].append(currentrow[11])

					# #####################################

					if currentrow[12] == '':
						pass
					else:
						age_freq[currentrow[0]].append(currentrow[12])

					# #####################################

					if currentrow[13] == '':
						pass
					else:
						sex[currentrow[0]].append(currentrow[13])

					# #####################################

					if currentrow[14] == '':
						pass
					else:
						sex_freq[currentrow[0]].append(currentrow[14])

					# #####################################

					if currentrow[15] == '':
						pass
					else:
						race[currentrow[0]].append(currentrow[15])

					# #####################################

					if currentrow[16] == '':
						pass
					else:
						race_freq[currentrow[0]].append(currentrow[16])

					


				else:
					symptoms.append(currentrow[0])
					href[currentrow[0]] = []
					title[currentrow[0]]= []
					other_names[currentrow[0]] = []
					desc[currentrow[0]] = []
					causes[currentrow[0]] = []
					percentages[currentrow[0]] = []
					related[currentrow[0]] = []
					related_p[currentrow[0]] = []
					test[currentrow[0]] = []
					meds[currentrow[0]] = []
					ages[currentrow[0]] = []
					age_freq[currentrow[0]] = []
					sex[currentrow[0]] = []
					sex_freq[currentrow[0]] = []
					race[currentrow[0]] = []
					race_freq[currentrow[0]] = []
					


					href[currentrow[0]].append(currentrow[1])
					title[currentrow[0]].append(currentrow[2])
					other_names[currentrow[0]].append(currentrow[3])
					desc[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						causes[currentrow[0]].append(currentrow[5])

					# #####################################

					if currentrow[6] == '':
						pass
					else:
						percentages[currentrow[0]].append(currentrow[6])

					# #####################################

					if currentrow[7] == '':
						pass
					else:	
						related[currentrow[0]].append(currentrow[7])

					# #####################################

					if currentrow[8] == '':
						pass
					else:	
						related_p[currentrow[0]].append(currentrow[8])

					# #####################################

					if currentrow[9] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[9])

					# #####################################

					if currentrow[10] == '':
						pass
					else:
						meds[currentrow[0]].append(currentrow[10])

					# #####################################

					if currentrow[11] == '':
						pass
					else:
						ages[currentrow[0]].append(currentrow[11])

					# #####################################

					if currentrow[12] == '':
						pass
					else:
						age_freq[currentrow[0]].append(currentrow[12])

					# #####################################

					if currentrow[13] == '':
						pass
					else:
						sex[currentrow[0]].append(currentrow[13])

					# #####################################

					if currentrow[14] == '':
						pass
					else:
						sex_freq[currentrow[0]].append(currentrow[14])

					# #####################################

					if currentrow[15] == '':
						pass
					else:
						race[currentrow[0]].append(currentrow[15])

					# #####################################

					if currentrow[16] == '':
						pass
					else:
						race_freq[currentrow[0]].append(currentrow[16])

					
	f.close()

	# testing(title, other_names, causes, percentages, test, ages, age_freq, sex, sex_freq, race, race_freq, meds)
	with open(filename_two, 'w') as f:
		for item in symptoms:
			for i in range(max(len(causes[item]), len(ages[item]), len(sex[item]), len(race[item]), len(meds[item]), len(related[item]))):
				temp_title = title[item][0]
				temp_other_names = other_names[item][0]
				temp_desc = desc[item][0]

				if not causes[item]:
					temp_symp = ''
				else:
					temp_symp = causes[item][0]
					causes[item].pop(0)

				if not percentages[item]:
					temp_percentage = ''
				else:
					temp_percentage = percentages[item][0]
					percentages[item].pop(0)

				if not related[item]:
					temp_related = ''
				else:
					temp_related = related[item][0]
					related[item].pop(0)

				if not related_p[item]:
					temp_related_p = ''
				else:
					temp_related_p = related_p[item][0]
					related_p[item].pop(0)

				if not test[item]:
					temp_test = ''
				else:
					temp_test = test[item][0]
					test[item].pop(0)

				if not meds[item]:
					temp_med = ''
				else:
					temp_med = meds[item][0]
					meds[item].pop(0)

				if not ages[item]:
					temp_age = ''
				else:
					temp_age =  ages[item][0]
					ages[item].pop(0)

				if not age_freq[item]:
					temp_age_freq = ''
				else:
					temp_age_freq = age_freq[item][0]
					age_freq[item].pop(0)

				if not sex[item]:
					temp_sex = ''
				else:
					temp_sex = sex[item][0]
					sex[item].pop(0)

				if not sex_freq[item]:
					temp_sex_freq = ''
				else:
					temp_sex_freq = sex_freq[item][0]
					sex_freq[item].pop(0)

				if not race[item]:
					temp_race = ''
				else:
					temp_race = race[item][0]
					race[item].pop(0)

				if not race_freq[item]:
					temp_race_freq = ''
				else:
					temp_race_freq = race_freq[item][0]
					race_freq[item].pop(0)

				

				f.write(temp_title + '\t' + temp_other_names + '\t' + temp_desc + '\t' + temp_symp + '\t' + temp_percentage \
						+ '\t' + temp_related + '\t' + temp_related_p +'\t' + temp_test + '\t' + temp_med + '\t' \
						+ temp_age + '\t' + temp_age_freq + '\t' + temp_sex \
						+ '\t' + temp_sex_freq + '\t' + temp_race + '\t' + temp_race_freq  + '\n')





def testing(title, other_names, causes, percentages, test, ages, \
		age_freq, sex, sex_freq, race, race_freq, meds):

	print "Title: ", title["Common cold"]
	print "Other names: ", other_names["Common cold"] 
	print "causes: ", causes["Common cold"]
	print "Percentages: ", percentages["Common cold"]
	print "Test: ", test["Common cold"]
	print "Ages: ", ages["Common cold"]
	print "Age Freq", age_freq["Common cold"]
	print "Sex: ", sex["Common cold"]
	print "Sex Freq: ", sex_freq["Common cold"]
	print "Race: ", race["Common cold"]
	print "Race Freq: ", race_freq["Common cold"]
	print "Meds: ", meds["Common cold"]

	print len(causes["Common cold"]) == len(percentages["Common cold"])
	print len(ages["Common cold"]) == len(age_freq["Common cold"])
	print len(sex["Common cold"]) == len(sex_freq["Common cold"])
	print len(race["Common cold"]) == len(race_freq["Common cold"])

