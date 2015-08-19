import re
import csv
import os

arr = ["BillGates_tweets",
"timoreilly_tweets",
"Pogue_tweets",
"ericschmidt_tweets",
"waltmossberg_tweets",
"codinghorror_tweets",
"martinfowler_tweets",
"shanselman_tweets",
"spolsky_tweets",
"KentBeck_tweets",
"jack_tweets",
"masason_tweets",
"biz_tweets",
"notch_tweets",
"elonmusk_tweets",
"ev_tweets",
"TEDchris_tweets",
"Padmasree_tweets",
"kevinrose_tweets",
"dickc_tweets",
"noaheverett_tweets",
"Ghonim_tweets",
"om_tweets",
"kaifulee_tweets",
"jeb__tweets",
"tim_cook_tweets",
"karaswisher_tweets",
"marissamayer_tweets",
"MichaelDell_tweets",
"majornelson_tweets",
"kenichiromogi_tweets",
"alaa_tweets",
"onambiguity_tweets",
"Chad_Hurley_tweets",
"leolaporte_tweets",
"anildash_tweets",
"pierre_tweets",
"SethBling_tweets",
"Dinnerbone_tweets",
"mikeyk_tweets",
"mattcutts_tweets",
"satyanadella_tweets",
"saurik_tweets",
"stevewoz_tweets",
"johnmaeda_tweets",
"chadfowler_tweets",
"john_tweets",
"ginatrapani_tweets",
"jbernhardsson_tweets",
"zeldman_tweets",
"pod2g_tweets",
"evad3rs_tweets",
"finkd_tweets",
"bgurley_tweets",
"pmarca_tweets",
"tnatsu_tweets",
"DuvalMagic_tweets",
"rsarver_tweets",
"reidhoffman_tweets",
"Fwiz_tweets",
"durov_tweets",
"DavidVonderhaar_tweets",
"Gronkh_tweets",
"MichaelCondrey_tweets",
"sivers_tweets",
"therealcliffyb_tweets",
"jkottke_tweets",
"digiphile_tweets",
"jkalucki_tweets",
"paulg_tweets",
"HIDEO_KOJIMA_EN_tweets",
"iH8sn0w_tweets",
"ID_AA_Carmack_tweets",
"nzkoz_tweets",
"myspacetom_tweets",
"abdur_tweets",
"carlmanneh_tweets",
"bs_tweets",
"todsacerdoti_tweets",
"timberners_lee_tweets",
"mollstam_tweets",
"_tomcc_tweets",
"Kappische_tweets",
"vpieters_tweets",
"jeresig_tweets",
"JahKob_tweets",
"p0sixninja_tweets",
"danfrisk_tweets",
"bhorowitz_tweets",
"noobde_tweets",
"minliangtan_tweets",
"cdixon_tweets",
"Benioff_tweets",
"IGLevine_tweets",
"paul_irish_tweets",
"srlm_tweets",
"robhoward_tweets",
"pschiller_tweets",
"tconrad_tweets",
"jonkagstrom_tweets",
"preillyme_tweets",
"demandrichard_tweets",
"shoemoney_tweets",
"levie_tweets",
"dongatory_tweets",
"_grum_tweets",
"mezzoblue_tweets",
"a_tweets",
"dhh_tweets",
"JD_2020_tweets",
"rkmt_tweets",
"e_kaspersky_tweets",
"joebelfiore_tweets",
"i0n1c_tweets",
"KrisJelbring_tweets",
"chriscoyier_tweets",
"sundarpichai_tweets",
"xlson_tweets",
"jemimakiss_tweets",
"RiotPendragon_tweets",
"lukew_tweets",
"carnalizer_tweets",
"drewhouston_tweets",
"ZacheryNielson_tweets",
"paulsingh_tweets",
"austinnotduncan_tweets",
"scottgu_tweets",
"chpwn_tweets",
"RamyRaoof_tweets",
"jimmy_wales_tweets",
"JonCrawford_tweets",
"zephoria_tweets",
"rocket2guns_tweets",
"LoaiNagati_tweets",
"ZeinabSamir_tweets",
"Joi_tweets",
"pmolyneux_tweets",
"l2k_tweets",
"sorenmacbeth_tweets",
"mkapor_tweets",
"sarahcuda_tweets",
"anamitra_tweets",
"addyosmani_tweets",
"akirareiko_tweets",
"wol_lay_tweets",
"skonnard_tweets",
"jsa_tweets",
"AquaXetine_tweets",
"f_tweets",
"Swiftor_tweets",
"DaveSumter_tweets",
"RanaASaid_tweets",
"AkihiroHino_tweets",
"habibh_tweets",
"ChrisMetzen_tweets",
"gr33ndata_tweets",
"simplebits_tweets",
"andrewchen_tweets",
"EdmundMcMillenn_tweets",
"stanleytang_tweets",
"meyerweb_tweets",
"BomuBoi_tweets",
"ryan_tweets",
"Harada_TEKKEN_tweets",
"marcoarment_tweets",
"tha_rami_tweets",
"sama_tweets",
"willsmith_tweets",
"reckless_tweets",
"br_tweets",
"travisk_tweets",
"larryellison_tweets",
"harrymccracken_tweets",
"EvilSeph_tweets",
"ibogost_tweets",
"jeff_tweets",
"fart_tweets",
"photomatt_tweets",
"dens_tweets",
"Arubin_tweets",
"j_smedley_tweets",
"SamFURUKAWA_tweets",
"PG_kamiya_tweets",
"scottebales_tweets",
"aaronwall_tweets",
"chrismessina_tweets",
"tinyBuild_tweets",
"Jonathan_Blow_tweets",
"kevin_tweets",
"Goldman44_tweets",
"stephenlrose_tweets",
"pgeuder_tweets",
"JeremyCMorgan_tweets",
"Pentadact_tweets",
"t_tweets",
"Werner_tweets",
"tanakaryusaku_tweets",
"beep_tweets",
"chrisremo_tweets",
"petecashmore_tweets"	
]

arr1 = ["BillGates",
"timoreilly",
"Pogue",
"ericschmidt",
"waltmossberg",
"codinghorror",
"martinfowler",
"shanselman",
"spolsky",
"KentBeck",
"jack",
"masason",
"biz",
"notch",
"elonmusk",
"ev",
"TEDchris",
"Padmasree",
"kevinrose",
"dickc",
"noaheverett",
"Ghonim",
"om",
"kaifulee",
"jeb_",
"tim_cook",
"karaswisher",
"marissamayer",
"MichaelDell",
"majornelson",
"kenichiromogi",
"alaa",
"onambiguity",
"Chad_Hurley",
"leolaporte",
"anildash",
"pierre",
"SethBling",
"Dinnerbone",
"mikeyk",
"mattcutts",
"satyanadella",
"saurik",
"stevewoz",
"johnmaeda",
"chadfowler",
"john",
"ginatrapani",
"jbernhardsson",
"zeldman",
"pod2g",
"evad3rs",
"finkd",
"bgurley",
"pmarca",
"tnatsu",
"DuvalMagic",
"rsarver",
"reidhoffman",
"Fwiz",
"durov",
"DavidVonderhaar",
"Gronkh",
"MichaelCondrey",
"sivers",
"therealcliffyb",
"jkottke",
"digiphile",
"jkalucki",
"paulg",
"HIDEO_KOJIMA_EN",
"iH8sn0w",
"ID_AA_Carmack",
"nzkoz",
"myspacetom",
"abdur",
"carlmanneh",
"bs",
"todsacerdoti",
"timberners_lee",
"mollstam",
"_tomcc",
"Kappische",
"vpieters",
"jeresig",
"JahKob",
"p0sixninja",
"danfrisk",
"bhorowitz",
"noobde",
"minliangtan",
"cdixon",
"Benioff",
"IGLevine",
"paul_irish",
"srlm",
"robhoward",
"pschiller",
"tconrad",
"jonkagstrom",
"preillyme",
"demandrichard",
"shoemoney",
"levie",
"dongatory",
"_grum",
"mezzoblue",
"a",
"dhh",
"JD_2020",
"rkmt",
"e_kaspersky",
"joebelfiore",
"i0n1c",
"KrisJelbring",
"chriscoyier",
"sundarpichai",
"xlson",
"jemimakiss",
"RiotPendragon",
"lukew",
"carnalizer",
"drewhouston",
"ZacheryNielson",
"paulsingh",
"austinnotduncan",
"scottgu",
"chpwn",
"RamyRaoof",
"jimmy_wales",
"JonCrawford",
"zephoria",
"rocket2guns",
"LoaiNagati",
"ZeinabSamir",
"Joi",
"pmolyneux",
"l2k",
"sorenmacbeth",
"mkapor",
"sarahcuda",
"anamitra",
"addyosmani",
"akirareiko",
"wol_lay",
"skonnard",
"jsa",
"AquaXetine",
"f",
"Swiftor",
"DaveSumter",
"RanaASaid",
"AkihiroHino",
"habibh",
"ChrisMetzen",
"gr33ndata",
"simplebits",
"andrewchen",
"EdmundMcMillenn",
"stanleytang",
"meyerweb",
"BomuBoi",
"ryan",
"Harada_TEKKEN",
"marcoarment",
"tha_rami",
"sama",
"willsmith",
"reckless",
"br",
"travisk",
"larryellison",
"harrymccracken",
"EvilSeph",
"ibogost",
"jeff",
"fart",
"photomatt",
"dens",
"Arubin",
"j_smedley",
"SamFURUKAWA",
"PG_kamiya",
"scottebales",
"aaronwall",
"chrismessina",
"tinyBuild",
"Jonathan_Blow",
"kevin",
"Goldman44",
"stephenlrose",
"pgeuder",
"JeremyCMorgan",
"Pentadact",
"t",
"Werner",
"tanakaryusaku",
"beep",
"chrisremo",
"petecashmore"	
]

count=[0 for i in range(200)]
Matrix = [[0 for x in range(200)] for x in range(200)]
for k in range(0,200):
	for j in range(0,200):
		userfname = os.path.join('../tweets', str(arr[j]) + '.csv')
		with open (userfname, "r") as myfile:
   			data=myfile.read().replace(',', ' ').replace("!", ' ').replace(":", ' ').replace("\"", ' ').replace("'",' ').replace(".",' ').replace("#",' ').replace("$",' ').replace("%",' ').replace("^",' ').replace("&",' ').replace("*",' ').replace("(",' ').replace(")",' ').replace("[",' ').replace("]",' ').replace("{",' ').replace("}",' ').replace(";",' ').replace("<",' ').replace(">",' ').replace("?",' ').replace("/",' ').replace("\\",' ').upper()
    	
		x = 0	
		count[j] = 0	
		for i in data.split():
			str1 = arr1[k].upper()
			str1 = '@' + str1
			if i==str1 and x==1: 
				count[j] = count[j] + 1
			if i=='RT':
				x = 1
			else:
				x =0
		Matrix[j][k] = count[j]
		#params = (count[j])
		#f.write("%d\n" % params)

	cou = 0
	for i in range(200):
		cou = cou + count[i]

	#print count
	#print cou
	#params = (cou)
	#f.write("%d\n" % params)

with open("acc3.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(Matrix)