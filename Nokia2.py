choice = True
while(choice):

	main_menu = """

	================Menu functions=================
	Press

	1. Phone book
	2. Messages
	3. Chat
	4. Call register
	5. Tones
	6. Settings
	7. Call divert
	8. Music
	9. Games
	10. Calculator
	11. Reminders
	12. Clock
	13. Profiles
	14. Service
	15. SIM service
	0. main_menu
	"""
	print(main_menu)

	main_menu = input("Select option: ")

	match main_menu:
		case "1":
			print("Phone book")

			phone_book= """
	1. Search
	2. Service Nos
	3. Add name
	4. Erase
	5. Edit
	6. Copy
	7. Assign
	8. Send b'card
	9. Options
	10. Speed dails
	11. Voice
		"""
			print(phone_book)		
			
			phone_book = input("Select option: ")
			
			match phone_book:
				case "1":
					print ("Search")
				case "2":
					print ("Service Nos")
				case "3":
					print ("Add name")
				case "4":
					print ("Erase")
				case "5":
					print ("Edit")
				case "6":
					print ("Copy")
				case "7":
					print ("Assign")
				case "8":
					print ("Send b'card")
				case "9":
					print ("Options")
					options = """
	1. Memory in use
	2. Type of view
	3. Memory status				

			"""
					print (options)
					
					options = input("Select option: ")
					
					match options: 
						case "1":
							print ("Memory in use")
						case "2":
							print ("Type of view")
						case "3":
							print (" Memory status")
						case _:
							print ("Invalid selection")	
			
					
				case "10":
					print ("Speed dails")
				case "11":
					print ("Voice")
				case _:
					print ("Invalid selection")		
			
			
			
			
			
			
			
			
		case "2":
			print ("Messages")
			message = """
	1. Write message
	2. Inbox
	3. Outbox
	4. Picture Messages
	5. Templates
	6. Smileys
	7. Message settings
	8. Info service
	9. Voice mailbox number
	10. Service command editor		

			"""
			print (message)
			
			message =  input("Select option: ")
			
			match message:
				case "1":
					print("Write message")
				case "2":
					print("Inbox")
				case "3":
					print("Outbox")
				case "4":
					print("Picture message")
				case "5":
					print("Templates")
				case "6":
					print("Smileys")
				case "7":
					print("message settings")
					message_settings ="""
					
	1. Set 1
	2. Common 				
	"""
					print (message_settings)
					
					message_settings =  input("Select option: ")
					
					match message_settings:
						case "1":
							print("Set 1")
							set1 ="""
	1. Message centre number
	2. Message sent as
	3. Message validity						
	"""						
							print(set1)
							
							set1 = input("Select option")
							
							match set1:
								case "1":
									print("Message centre number")
								case "2":
									print("Message sent as")
								case "3":
									print("Message validity")
								case _:
									print ("Invalid selection")
							
							
						case "2":
							print("Common")
							common = """
							
	1. Delivery reports
	2. Reply via same centre
	3. Character support						
	"""						
							print(common)
							
							common = input("Select option")
							
							match common:
								case "1":
									print("Delivery reports")
								case "2":
									print("reply via same centre")
								case "3":
									print("Character support")
								case _:
									print ("Invalid selection")
					
					
				case "8":
					print ("Info service")
				case "9":
					print ("Voice mailbox number")
				case "10":
					print ("Service command editor")
				case _:
					print ("Invalid selection") 
			
			
			
			
		case "3":
			print ("Chat")
		case "4":
			print ("Call register")
			callregister = """
					
	1. Missed calls
	2. Recieved calls
	3. Dailled numbers
	4. Erase recent calls
	5. Show call duration
	6. Show call cost
	7. Call cost settings
	8. Prepaid credit		
			
	"""		
			print(callregister)
			
			callregister = input("Select option: ")
				
			match callregister:
				case "1":
					print("Missed calls")
				case "2":
					print("Recieved calls")
				case "3":
					print("Dailled number")
				case "4":
					print("Erase recent calls")
				case "5":
					print("Show call duration")
					show_call_duration = """
					  					  	
	1. Last call duration
	2. All calls' duration
	3. Recieved calls' duration
	4. Dailled calls' duration
	5. Clear timers				  	
			"""
							  	
					print(show_call_duration)
								
					show_call_duration_menu = input("Select optin: ")
								
					match show_call_duration:
							case "1":
								print("Last call duration")
							case "2":
					  			print("All calls' duration")
							case "3":
					  			print("Recieved calls' duration")
							case "4":
					  			print(" Dailled calls' duration")
							case "5":
					  			print("Clear timers")
							case _:
								print ("Invalid selection")	  	
					  	
					  	
				case "6":
					print("Show call cost")
					Show_call_cost = """
					
	1. Last calls' cost
	2. All calls' cost
	3. Clear counters					
	"""					
						
					print(Show_call_cost)
						
					Show_call_cost = input("Select option: ")
						
					match Show_call_cost:
							case "1":
								print("Last call cost")
							case "2":
					  			print("All calls' cost")
							case "3":
					  			print("Clear counters")
							case _:
								print ("Invalid selection")


				case "7":
					print("Call cost settings")
					Call_cost_settings = """
						
	1. Call cost limit
	2. Show coat in				
	"""					
					print(Call_cost_settings)
						
					Call_cost_settings = input("Select option")
						
					match Call_cost_settings:
							case "1":
								print("Call cost limit")
							case "2":
					  			print("Show coat in")
						
						
				case "8":
					print("Prepaid credit")
				case _:
					print ("Invalid selection")
					
			
		case "5":
			print ("Tones")
			tones = """
	1. Ringing tone
	2. Ringing volume
	3. Incoming alert
	4. Message alert tone
	5. Keypad tones
	6. Warning tones
	7. Vibrating alert
	8. Screen saver			
	"""

			print(tones)
			
			tones = input("Select option: ")
			
			match tones:
				case "1":
					print("Ringing tone")
				case "2":
					print("Ringing volume")
				case "3":
					print("Incoming alert")
				case "4":
					print(" Message alert tone")
				case "5":
					print("Keypad tones")  	
				case "6":
					print("Warning tones")
				case "7":
					print("Vibrating alert")
				case "8":
					print("Screen saver")
				case _:
					print ("Invalid selection")	  	


			
			
		case "6":
			print ("Settings")
			settings = """
			
	1. Call settings
	2. Phone settings
	3. Security settings
	4. Restor factory settings			
	"""		
			
			print(settings)
			
			settings = input("Select option: ")
			
			match settings:
				case "1":
					print("Call settings")
					call_settings = """
					
	1. Automatic redial
	2. Speed dailling
	3. Call waiting options
	4. Own number sending
	5. Phone line in use
	6. Automatic answer				
	"""			
		
					print (call_settings)
					
					call_settings = input("Select option: ")
					
					match call_settings:
						case "1":
							print("Automatic redial")
						case "2":
							print("Speed dailling")
						case "3":
							print("Call waiting options")
						case "4":
							print("Own number sending")
						case "5":
							print("Phone line in use")  	
						case "6":
							print("Automatic answer")
						case _:
							print ("Invalid selection")
					
					
					
				case "2":
					print("Phone settings")
					phone_setting = """
					
	1. Language
	2. Cell info display
	3. Welcome note
	4. Network selection
	5. Confirm SIM service action	  				
	"""
					print(phone_setting)
					
					phone_settings_choice = input("Select option: ")
					
					match phone_settings_choice:
						case "1":
							print("Language")
						case "2":
							print("Cell info display")
						case "3":
							print("Welcome note")
						case "4":
							print(" Network selection")
						case "5":
							print("Confirm SIM service action")
						case _:
							print ("Invalid selection") 			
		                

					
				case "3":
					print("Security settings")
					security_settings = """
					
	1. PIN code request
	2. Call barring service
	3. Fixed dailling
	4. Closed up group
	5. Security level
	6. Change acces codes
	"""		

					print (security_settings)
					security_settings = input("Select option")
									
					match security_settings:
						case "1":
							print("PIN code request")
						case "2":
							print("Call barring service")
						case "3":
							print("Fixed dailling")
						case "4":
							print("Closed up group")
						case "5":
							print("Security level")  	
						case "6":
							print("Change acces codes")
						case _:
							print ("Invalid selection")
					
					
							
				case "4":
					print("Restor factory settings")
				case _:
					print ("Invalid selection")


		case "7":
			print ("Call divert")
		case "8":
			print ("Music")
			music = """
			
	1. Music player
	2. Radio
	3. Recorder
	4. Track list		
	"""		

			print (music)
			music = input("Select option: ")
				
			match music:
				case "1":
					print("Music player")
				case "2":
					print("Radio")
				case "3":
					print("Recorder")
				case "4":
					print("Track list")
				case _:
					print ("Invalid selection")	
			
			
			
			
		case "9":
			print ("Games")
		case "10":
			print ("Calculator")
		case "11":
			print ("Reminders")
		case "12":
			print ("Clock")
			clock = """
			
	1. Alarm clock
	2. Clock settings			
	3. Date setting
	4. Stopwatch
	5. Countdown timer
	6. Auto update of date and time				 		
	"""		
			
			print(clock)
			clock = input("Select option")
			
			match clock:
				case "1":
					print("Alarm clock")
				case "2":
					print("Clock settings")
				case "3":
					print("Date setting")
				case "4":
					print("Stopwatch")	
				case "5":
					print(" Countdown timer")
				case "6":
					print(" Auto update of date and time")
				case _:
					print ("Invalid selection")	
			
		case "13":
			print ("Profiles")
		case "14":
			print ("Services")
		case "15":
			print ("SIM services")
		case "0":
			choice = False
		case _:
			print ("Invalid selection")
