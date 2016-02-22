import csv
import random

def final_diseases(read_diseases, read_symptoms, final_write):

	conditions = []
	full_symptoms = []
	href = {}
	title = {}
	other_names = {}
	test = {}
	meds = {}
	symps = {}
	percentages = {}
	attr = {}
	freq = {}
	ages = {}
	sex = {}
	ethnicity = {}

	age_strings = ['< 1 years', '1-4 years', '5-14 years', '15-29 years', \
					'30-44 years', '45-59 years', '60-74 years', '75+ years']
	sex_strings = ['Male', 'Female']
	ethnicity_strings = ['Hispanic', 'Other', 'Black', 'White']

	with open(read_symptoms, 'r') as s:

		for row in s:
			rows = row.split('\r')
			for i in rows:
				if i=='symptoms':
					pass
				else:
					full_symptoms.append(i)


	s.close()

	with open(read_diseases, 'r') as f:

		for row in f:

			rows = row.split('\r')
			for i in rows:
				currentrow =  i.split('\t')

				if currentrow[0] in conditions:
					if currentrow[1] in href[currentrow[0]]:
						pass
					else:
						href[currentrow[0]].append(currentrow[1])

					if currentrow[2] in title[currentrow[0]]:
						pass
					else:
						title[currentrow[0]].append(currentrow[2])

					if currentrow[3] in other_names[currentrow[0]]:
						pass
					else:
						other_names[currentrow[0]].append(currentrow[3])

					if currentrow[4] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						meds[currentrow[0]].append(currentrow[5])

					if currentrow[6] == '':
						pass
					else:
						symps[currentrow[0]].append(currentrow[6])

					if currentrow[7] == '':
						pass
					else:
						percentages[currentrow[0]].append([currentrow[6], currentrow[7]])

					if currentrow[8] == '':
						pass
					else:
						if currentrow[8] in age_strings:
							ages[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						elif currentrow[8] in sex_strings:
							sex[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						elif currentrow[8] in ethnicity_strings:
							ethnicity[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						else:
							attr[currentrow[0]].append(currentrow[8])
							freq[currentrow[0]].append(currentrow[9])


				else:
					if currentrow[0] == 'conditions':
						pass
					else:
						conditions.append(currentrow[0])
					href[currentrow[0]] = []
					title[currentrow[0]]= []
					other_names[currentrow[0]] = []
					test[currentrow[0]] = []
					meds[currentrow[0]] = []
					symps[currentrow[0]] = []
					percentages[currentrow[0]] = []
					attr[currentrow[0]] = []
					freq[currentrow[0]] = []
					ages[currentrow[0]] = []
					sex[currentrow[0]] = []
					ethnicity[currentrow[0]] = []


					href[currentrow[0]].append(currentrow[1])
					title[currentrow[0]].append(currentrow[2])
					other_names[currentrow[0]].append(currentrow[3])

					if currentrow[4] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						meds[currentrow[0]].append(currentrow[5])

					if currentrow[6] == '':
						pass
					else:
						symps[currentrow[0]].append(currentrow[6])

					if currentrow[7] == '':
						pass
					else:
						percentages[currentrow[0]].append([currentrow[6], currentrow[7]])

					if currentrow[8] == '':
						pass
					else:
						if currentrow[8] in age_strings:
							ages[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						elif currentrow[8] in sex_strings:
							sex[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						elif currentrow[8] in ethnicity_strings:
							ethnicity[currentrow[0]].append([currentrow[8], float(currentrow[9][0:-1])])
						else:
							attr[currentrow[0]].append(currentrow[8])
							freq[currentrow[0]].append(currentrow[9])


	f.close()
	
	# ages, sex, ethnicity = set_percentages(conditions, ages, sex, ethnicity)
	# def print_row(condition, full_symptoms, href, title, other_names, test, meds, symps, \
				# percentages, attr, freq, ages, sex, ethnicity, age_strings, sex_strings, ethnicity_strings):
	# print percentages["Common cold"]


	
	# testing(title, other_names, symps, percentages, test, ages, age_freq, sex, sex_freq, race, race_freq, meds)


	with open(final_write, 'w') as f:
		row = 'title'
		for s in full_symptoms:
			row = row + '\t' + s

		row = row + '\n'
		f.write(row)

		for item in conditions:
			for i in range(100):
				row = print_row(item, full_symptoms, href, title, other_names, test, meds, symps, \
				percentages, attr, freq, ages, sex, ethnicity, age_strings, sex_strings, ethnicity_strings)
				f.write(row)


	f.close
	# 		for i in range(max(len(symps[item]), len(ages[item]), len(sex[item]), len(race[item]), len(meds[item]))):
	# 			temp_title = title[item][0]
	# 			temp_other_names = other_names[item][0]
	# 			temp_desc = desc[item][0]

	# 			if not symps[item]:
	# 				temp_symp = ''
	# 			else:
	# 				temp_symp = symps[item][0]
	# 				symps[item].pop(0)

	# 			if not percentages[item]:
	# 				temp_percentage = ''
	# 			else:
	# 				temp_percentage = percentages[item][0]
	# 				percentages[item].pop(0)

	# 			if not test[item]:
	# 				temp_test = ''
	# 			else:
	# 				temp_test = test[item][0]
	# 				test[item].pop(0)

	# 			if not ages[item]:
	# 				temp_age = ''
	# 			else:
	# 				temp_age =  ages[item][0]
	# 				ages[item].pop(0)

	# 			if not age_freq[item]:
	# 				temp_age_freq = ''
	# 			else:
	# 				temp_age_freq = age_freq[item][0]
	# 				age_freq[item].pop(0)

	# 			if not sex[item]:
	# 				temp_sex = ''
	# 			else:
	# 				temp_sex = sex[item][0]
	# 				sex[item].pop(0)

	# 			if not sex_freq[item]:
	# 				temp_sex_freq = ''
	# 			else:
	# 				temp_sex_freq = sex_freq[item][0]
	# 				sex_freq[item].pop(0)

	# 			if not race[item]:
	# 				temp_race = ''
	# 			else:
	# 				temp_race = race[item][0]
	# 				race[item].pop(0)

	# 			if not race_freq[item]:
	# 				temp_race_freq = ''
	# 			else:
	# 				temp_race_freq = race_freq[item][0]
	# 				race_freq[item].pop(0)

	# 			if not meds[item]:
	# 				temp_med = ''
	# 			else:
	# 				temp_med = meds[item][0]
	# 				meds[item].pop(0)

	# 			f.write(temp_title + '\t' + temp_other_names + '\t' + temp_desc + '\t' + temp_symp + '\t' + temp_percentage \
	# 					+ '\t' + temp_test + '\t' + temp_age + '\t' + temp_age_freq + '\t' + temp_sex \
	# 					+ '\t' + temp_sex_freq + '\t' + temp_race + '\t' + temp_race_freq + '\t' + temp_med + '\n')


def print_row(condition, full_symptoms, href, title, other_names, test, meds, symps, \
				percentages, attr, freq, ages, sex, ethnicity, age_strings, sex_strings, ethnicity_strings):
	
	row = condition
	for s in full_symptoms:
		if s in symps[condition]:

			percent = 1

			for item in percentages[condition]:
				if item[0] == s:
					percent = float(item[1])
					break

			row = row + '\t' + str(decision(percent))
			
		else:
			row = row + '\t' + str(-1)

	row = row + '\n'
	return row


		


def set_percentages(conditions, ages, sex, ethnicity):
	for dis in conditions:
		if dis == 'conditions':
			pass
		else:
			temp_ages = []
			temp_sex = []
			temp_ethn = []

			for age_list in ages[dis]:
				# print age_list[1]
				temp_ages.append(age_list[1])

			max_age = 1.33*max(temp_ages)
			
			for age_list in ages[dis]:
				age_list[1] = (age_list[1]/max_age)*100

			##########sex

			for s_list in sex[dis]:
				temp_sex.append(s_list[1])

			max_sex = 1.33*max(temp_sex)

			for s_list in sex[dis]:
				s_list[1] =(s_list[1]/max_sex)*100

			##########eethnicity	
			for ethn_list in ethnicity[dis]:
				temp_ethn.append(ethn_list[1])
			
			max_ethn = 1.33*max(temp_ethn)

			for ethn_list in ethnicity[dis]:
				ethn_list[1] = (ethn_list[1]/max_ethn)*100

	return ages, sex, ethnicity

def decision(probability):
    if random.random() < probability:
    	return 1
    else:
    	return -1


def organize_symps(filename, filename_two):

	conditions = []
	href = {}
	title = {}
	other_names = {}
	desc = {}
	symps = {}
	percentages = {}
	test = {}
	ages = {}
	age_freq = {}
	sex = {}
	sex_freq = {}
	race = {}
	race_freq = {}
	meds = {}

	with open(filename, 'r') as f:

		for row in f:

			rows = row.split('\r')
			for i in rows:
				currentrow =  i.split('\t')


				if currentrow[0] in conditions:
					if currentrow[1] in href[currentrow[0]]:
						pass
					else:
						href[currentrow[0]].append(currentrow[1])

					if currentrow[2] in title[currentrow[0]]:
						pass
					else:
						title[currentrow[0]].append(currentrow[2])

					if currentrow[3] in other_names[currentrow[0]]:
						pass
					else:
						other_names[currentrow[0]].append(currentrow[3])

					if currentrow[4] in desc[currentrow[0]]:
						pass
					else:
						desc[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						symps[currentrow[0]].append(currentrow[5])

					if currentrow[6] == '':
						pass
					else:
						percentages[currentrow[0]].append(currentrow[6])

					if currentrow[7] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[7])

					if currentrow[8] == '':
						pass
					else:
						ages[currentrow[0]].append(currentrow[8])

					if currentrow[9] == '':
						pass
					else:
						age_freq[currentrow[0]].append(currentrow[9])

					if currentrow[10] == '':
						pass
					else:
						sex[currentrow[0]].append(currentrow[10])

					if currentrow[11] == '':
						pass
					else:
						sex_freq[currentrow[0]].append(currentrow[11])

					if currentrow[12] == '':
						pass
					else:
						race[currentrow[0]].append(currentrow[12])

					if currentrow[13] == '':
						pass
					else:
						race_freq[currentrow[0]].append(currentrow[13])

					if currentrow[14] == '':
						pass
					else:
						meds[currentrow[0]].append(currentrow[14])


				else:
					conditions.append(currentrow[0])
					href[currentrow[0]] = []
					title[currentrow[0]]= []
					other_names[currentrow[0]] = []
					desc[currentrow[0]] = []
					symps[currentrow[0]] = []
					percentages[currentrow[0]] = []
					test[currentrow[0]] = []
					ages[currentrow[0]] = []
					age_freq[currentrow[0]] = []
					sex[currentrow[0]] = []
					sex_freq[currentrow[0]] = []
					race[currentrow[0]] = []
					race_freq[currentrow[0]] = []
					meds[currentrow[0]] = []


					href[currentrow[0]].append(currentrow[1])
					title[currentrow[0]].append(currentrow[2])
					other_names[currentrow[0]].append(currentrow[3])
					desc[currentrow[0]].append(currentrow[4])

					if currentrow[5] == '':
						pass
					else:	
						symps[currentrow[0]].append(currentrow[5])

					if currentrow[6] == '':
						pass
					else:
						percentages[currentrow[0]].append(currentrow[6])

					if currentrow[7] == '':
						pass
					else:
						test[currentrow[0]].append(currentrow[7])

					if currentrow[8] == '':
						pass
					else:
						ages[currentrow[0]].append(currentrow[8])

					if currentrow[9] == '':
						pass
					else:
						age_freq[currentrow[0]].append(currentrow[9])

					if currentrow[10] == '':
						pass
					else:
						sex[currentrow[0]].append(currentrow[10])

					if currentrow[11] == '':
						pass
					else:
						sex_freq[currentrow[0]].append(currentrow[11])

					if currentrow[12] == '':
						pass
					else:
						race[currentrow[0]].append(currentrow[12])

					if currentrow[13] == '':
						pass
					else:
						race_freq[currentrow[0]].append(currentrow[13])

					if currentrow[14] == '':
						pass
					else:
						meds[currentrow[0]].append(currentrow[14])
	f.close()

	# testing(title, other_names, symps, percentages, test, ages, age_freq, sex, sex_freq, race, race_freq, meds)
	with open(filename_two, 'w') as f:
		for item in conditions:
			for i in range(max(len(symps[item]), len(ages[item]), len(sex[item]), len(race[item]), len(meds[item]))):
				temp_title = title[item][0]
				temp_other_names = other_names[item][0]
				temp_desc = desc[item][0]

				if not symps[item]:
					temp_symp = ''
				else:
					temp_symp = symps[item][0]
					symps[item].pop(0)

				if not percentages[item]:
					temp_percentage = ''
				else:
					temp_percentage = percentages[item][0]
					percentages[item].pop(0)

				if not test[item]:
					temp_test = ''
				else:
					temp_test = test[item][0]
					test[item].pop(0)

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

				if not meds[item]:
					temp_med = ''
				else:
					temp_med = meds[item][0]
					meds[item].pop(0)

				f.write(temp_title + '\t' + temp_other_names + '\t' + temp_desc + '\t' + temp_symp + '\t' + temp_percentage \
						+ '\t' + temp_test + '\t' + temp_age + '\t' + temp_age_freq + '\t' + temp_sex \
						+ '\t' + temp_sex_freq + '\t' + temp_race + '\t' + temp_race_freq + '\t' + temp_med + '\n')





def testing(title, other_names, symps, percentages, test, ages, \
		age_freq, sex, sex_freq, race, race_freq, meds):

	print "Title: ", title["Common cold"]
	print "Other names: ", other_names["Common cold"] 
	print "Symps: ", symps["Common cold"]
	print "Percentages: ", percentages["Common cold"]
	print "Test: ", test["Common cold"]
	print "Ages: ", ages["Common cold"]
	print "Age Freq", age_freq["Common cold"]
	print "Sex: ", sex["Common cold"]
	print "Sex Freq: ", sex_freq["Common cold"]
	print "Race: ", race["Common cold"]
	print "Race Freq: ", race_freq["Common cold"]
	print "Meds: ", meds["Common cold"]

	print len(symps["Common cold"]) == len(percentages["Common cold"])
	print len(ages["Common cold"]) == len(age_freq["Common cold"])
	print len(sex["Common cold"]) == len(sex_freq["Common cold"])
	print len(race["Common cold"]) == len(race_freq["Common cold"])

