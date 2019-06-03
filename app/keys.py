home_keywords = ['family', 'kids', 'children', 'child', 'event', 'events', 'activity', 'activities', 'things to do', 'search', 'find', 'days out', 'family hub', 'familyhub', 'Aalsmeer', 'Badhoevedorp','Bloemendaal', 'Cruquius', 'Haarlem', 'Heemstede', 'Hillegom', 'Hoofddorp', 'Lisse', 'Nieuw-Vennep', 'Santpoort-Noord', 'Uithorn', 'Zandvoort', 'Haarlemmermeer']

activities_keywords = ['activities for kids', 'kids', 'fun things to do', 'activity', 'kids sports', 'Creative kids', 'Science and Tech for kids', 'Cultural kids', 'Music for kids', 'kids Yoga', 'kids Mindfulnes', 'Museums and Exhibitions', 'Parks and playgrounds', 'in english', 'family hub', 'familyhub', 'Aalsmeer', 'Badhoevedorp','Bloemendaal', 'Cruquius', 'Haarlem', 'Heemstede', 'Hillegom', 'Hoofddorp', 'Lisse', 'Nieuw-Vennep', 'Santpoort-Noord', 'Uithorn', 'Zandvoort', 'Haarlemmermeer']

events_keywords = ['events for kids', 'kids', 'fun things to do', 'event', 'kids day out', 'family days out', 'family festival', 'music', 'kids events', 'in english', 'family hub', 'familyhub', 'Aalsmeer', 'Badhoevedorp','Bloemendaal', 'Cruquius', 'Haarlem', 'Heemstede', 'Hillegom', 'Hoofddorp', 'Lisse', 'Nieuw-Vennep', 'Santpoort-Noord', 'Uithorn', 'Zandvoort', 'Haarlemmermeer' ]

generic_keywords = ['events', 'activities', 'for kids', 'in haarlem', 'in haarlemmermeer', 'in hoofddorp', 'kids sports', 'after school clubs', 'kids adventures', 'netherlands', 'holland', 'nederland', 'dutch', 'kids', 'fun', 'out and about']

class Keywords:
    home = ', '.join(str(keyword) for keyword in home_keywords)
    activities = ', '.join(str(keyword) for keyword in activities_keywords)
    events = ', '.join(str(keyword) for keyword in events_keywords)
    generic = ', '.join(str(keyword) for keyword in generic_keywords)