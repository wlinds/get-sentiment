maps = {

    'när_var': {
        # Specifika tider
        r'morgon\w*|morgnar': 'Morgon',
        r'kväll\w*|natt|nätter': 'Kväll',

        r'måndag\w*': 'Måndag',
        r'tisdag\w*': 'Tisdag',
        r'onsdag\w*': 'Onsdag',
        r'torsdag\w*': 'Torsdag',
        r'fredag\w*': 'Fredag',
        r'lördag\w*': 'Lördag',
        r'söndag\w*': 'Söndag',

        r'helg\w*|weekend\w*': 'Helg',
        r'arbetsvecka|veckovis|vecka|vecko\w*': 'Veckovis',

        # Specifika platser

        r'bil|kör|pendel|tåg|buss|cykel|cykling|cyklar|pendl|resan|tunnelbana': 'Transport',
        r'skog|natur|hav|fjäll|träd|trädgård\w*|promen\w*|vandrar|vandring|löp|spring\w*|utomhus|brygga|trän\w*': 'Natur & Motion',
        r'säng|soffa|fåtölj|hemma|frukost|sova|duschen|badet': 'Hemma',
        r'jobb|kontor|arbetsplats|möte|arbetsdag\w*|kalender|kontoret': 'Arbetsplats',
        r'bokad|avsatt|strukturerat|planerad|kalendern|schema|veckovis|fredagar': 'Planerad tid',
        r'tillsammans|kollegor|coach|grupp|team|andra|samtal|dialog': 'Social reflektion',
        r'skriv|anteckn|penna|papper|dagbok|bok': 'Skriftlig reflektion',
        r'tystnad|stillhet|kyrka|vila|meditation|yoga': 'Lugna platser',
        r'spontan|löpande|mellan|oplanerat|naturlig|process|kontinuerlig': 'Spontant'
    },

    'ämnen_frågor': {
        # Work Performance / Arbetsprestation (?)
        r'jobb\w*|arbet\w*|projekt|uppgift|möte|prestation|uppdrag': 'Arbetsprestation',
        
        # Ledarskap & Organisation
        r'ledarskap|chef|medarbetare|organisation|personal|team|grupp': 'Ledarskap & Organisation',
        
        # Personlig utveckling
        r'utveckling|beteende|agerande|förbättr\w*|lärande|förändring': 'Personlig utveckling',
        
        # Relationer & Kommunikation
        r'relation|kommunika|samtal|människor|dialog|kollegor': 'Relationer & Kommunikation',
        
        # Hälsa
        r'mående|hälsa|balans|energi|kropp|välbefinnande|vila': 'Hälsa & Välmående',
        
        # Planering & Mål (?)
        r'mål|planering|framtid|strategi|priorit|riktning|väg': 'Mål & Planering',
        
        # Analysis  Utvärdering?
        r'utvärder|analys\w*|resultat|utfall|gick bra|kunde gjort|annorlunda': 'Utvärdering',
        
        # Values
        r'värdering|mening|värde|syfte|varför|intention': 'Värderingar & Syfte',
        
        # Privatliv
        r'familj|privat|liv|vänner|fritid': 'Privatliv',
        
        # Känslor
        r'känsl|upplev|reagera|tankar|sinne': 'Känslor & Upplevelser',
        
        # Problemlösning
        r'problem|lösning|hinder|utmaning|dilemma|svår': 'Problemlösning',
        
        # Spontaneous/Unstructured
        r'spontan|fritt|ostrukturerad|kommer|dyker upp|flöda': 'Spontan reflektion'
    },


    'värde': {
        # Personlig utveckling
        r'utveckl|väx|förbättr|lär|fortbild|mognad': 'Personlig utveckling',
        
        # Decision Making & Problem Solving | Beslutsfattande
        r'beslut|lösning|val|klok|perspektiv': 'Beslutsfattande',
        
        # Mental Health | Välmående
        r'lugn|ro|harmoni|må bättre|stress|mental|återhämtning|hållbar': 'Välmående',
        
        # Insikt & Förståelse
        r'insikt|förstå|klokhet|självinsikt|kunskap|begrip': 'Insikt & Förståelse',
        
        # Struktur & Klarhet
        r'struktur|sorter|rensa|klar|ordning|samla': 'Struktur & Klarhet',
        
        # Essential Value
        r'nödvändig|avgörande|livsviktig|superviktig|stort värde|enormt värde|allt värde|allt för mig|värdefullt|jätteviktigt|överlevnad': 'Fundamentalt värde',
        
        # Self-awareness & Identity
        r'själv|inre|kompass|värdering|grund': 'Självkännedom',
        
        # Processing & Integration
        r'bearbeta|integrera|landa|släppa|processa': 'Bearbetning',
        
        # Growth & Motivation
        r'motivation|drivkraft|framåt|möjlighet|potential': 'Drivkraft & Tillväxt',
        
        # Quality
        r'kvalitet|bättre|utveckla|förbättr': 'Kvalitet & Förbättring',
        
        # Pause & Reflection
        r'stanna upp|paus|vila|tid|broms': 'Paus & Eftertanke',
        
        # Leadership Development
        r'ledar\w*|chef|profession|ledarskap|mitt ledarskap|ledarutveckl\w*': 'Ledarutveckling'
    },


    'hinder': {
        # Time Related
        r'(?:har )?(?:inte )?(?:alltid )?(?:hinn\w+|tar sig tid|tid(?:en)?|tidsbrist)|' + 
        r'arbetsbelastning|arbetstempo|fullboka\w*|almanacka|möten|tidspress|' +
        r'spring\w* (?:för )?fort|tar sig inte tid|mellanrum|upptagen|inboka\w*|' +
        r'under(?:\s)?arbets(?:dag\w*)?|undermålig planering|går (?:för )?fort|' +
        r'det ena till det andra': 'Tidsrelaterade hinder',

        # Stress
        r'stress|press|tempo|bråttom|rus|högt tempo|för mycket|många|belastning|' +
        r'mycket annat|fullt upp|överbelastad|kör(?:-|\s)?bara(?:-|\s)?kör': 'Stress',

        # Emotional
        r'oro|ångest|rädsla|skam|skuld|rädd|jobbigt|orka|energi|låg energi|' +
        r'rädslor|osäkerhet|våga|trött\w*|skav|fragmentarisk': 'Emotionella hinder',

        # Distractions
        r'fokus|distraktion|splittring|brus|mobil|skärm|sociala medier|närvaro|' +
        r'mentalt|hjärnan|snurra|intryck|koncentration|störning|förmåga|bubbla|' +
        r'ostörd|avbruten|avbrott': 'Mental närvaro, fokus',

        # Prioritize
        r'priorit\w*|annat kommer före|mycket annat|andra saker|väljer bort|' +
        r'tar sig inte|kommer inte till|skjuter upp': 'Prioritering',

        # Personal Discipline
        r'självdisciplin|disciplin|självledarskap|egen|rutiner|tar mig inte|' +
        r'beteende|vana|öva|svårt att skapa|ny vana': 'Självdisciplin',

        # "Ältande"
        r'ältande|konstruktiv\w*|definitiva slutsatser|fullständig bild|' +
        r'fragmentarisk|svårt att agera': 'Process & Ältande',

        # Saknar stöd/struktur
        r'ingen att reflektera med|saknar någon|ensam|struktur saknas|' +
        r'behöver stöd|saknar forum': 'Saknar stöd/struktur',

        # Livspusslet
        r'familj|småbarn|barn|livspusslet|livet|vardagen|privat|logistik|' +
        r'balans|livets|familjeliv': 'Livspusslet',

        # Actions
        r'action|prestationshets|leverans|prioriterar action|agerande|' +
        r'snabb action|fokus framåt|resultat|konkret|checka av|att-göra': 'Action-orienterade hinder',

        # No blockers
        r'(?:^|\s|,)(?:inga|ingen)(?:\s|\.|,|$)|kan inte komma på|nej|finns inga': 'Inga hinder'
    },


    'ja_nej_svar': {
        # Strong negatives (check first)
        r'(?:^|\s|,)(absolut\s+inte|tyvärr\s+inte|såklart\s+inte)(?:\s|\.|,|$)|' +
        r'(?:^|\s)(nej|nope|näe)(?:\s|\.|,|$)|' +
        r'inte\s+(?:alltid|för|nog)|' +
        r'oftast\s+inte|' +
        r'troligtvis\s+inte|' +
        r'gör\s+(?:jag|det)\s+(?:nog|troligtvis)\s+inte': 'Nej',
        
        # Standard negatives (check second)
        r'skulle\s+(?:gärna|kunna|vilja|behöva)|' +
        r'kan\s+(?:nog\s+)?(?:lägga|bli|göra)\s+(?:mer|bättre)|' +
        r'önskar|borde|kunde\s+vara\s+mer|' +
        r'mindre\s+tid\s+än\s+önskat|' +
        r'inte\s+tillräckligt|' +
        r'sällan|aldrig': 'Nej',
        
        # Uncertainty (check third)
        r'(?:^|\s)vet\s+(?:inte|ej)(?:\s|\.|,|$)|' +
        r'(?:^|\s)nja\b(?!\s*\.|[^\.]*tillräckligt)|' +  # "nja" om inte "tillräckligt" följer
        r'(?:^|\s)både\s+och(?:\s|\.|,|$)|' +
        r'osäker': 'Vet ej',
        
        # Strong positives (check fourth)
        r'(?:^|\s|,)(japp|yes)(?:\s|\.|,|!|$)|' +
        r'(?:idag|nu)\s+gör\s+(?:jag|det)|' +
        r'(?:^|\s)ofta\b|' +
        r'(?:^|\s)oftast(?!\s+inte)|' +  # "oftast" om inte "inte" följer
        r'absolut(?!\s+inte)|' +  # "absolut" om inte "inte" följer
        r'ganska\s+nöjd|' +
        r'god\s+tid|' +
        r'(?:^|\s)joo\b': 'Ja',
        
        # Standard positives (check last)
        r'(?:^|\s|,)ja(?:\s|\.|,|!|$)|' +
        r'tillfreds|' +
        r'tillräckligt|' +
        r'nöjd\s+med|' +
        r'fungerar\s+bra|' +
        r'räcker': 'Ja'
    },

    'kön': {
        r'kvinna|Kvinna' : "Kvinna",
        r'man|Man' : "Man"
    },



    'yrkesroll': {
        # Top management
        r'vd|ceo|generalsekreterare|': 'VD/CEO',
        r'regionchef|regionsdirektör': 'Chef',
        
        # Middle management
        r'chef\b|manager|ledare|kontorschef|enhetschef|lagerchef|hotell chef': 'Chef',

        r'ekonomichef|cfo|finance': 'Chef',
        r'kommunikationschef|marknadchef|marknad': 'Chef',
        r'produktchef|director product|utvecklingsansvarig': 'Chef',
        
        # Project/Process roles
        r'projektledare|processledare': 'Chref',
        r'utvecklingsledare|verksamhetsutvecklare': 'Utvecklingsledare',
        
        # Specialist roles
        r'hr-generalist|hr\b': 'HR-specialist',
        r'kommunikatör|skribent': 'Kommunikatör', # Utan chefsansvar?
        r'konsult|rådgivare': 'Konsult/Rådgivare',
        r'coach|faciliterare': 'Coach',
    
        # Education
        r'rektor|biträdande rektor': 'Rektor/Biträdande rektor',
        r'lärare': 'Lärare',
        
        # Business owners
        r'egenföretagare|företagare|entreprenör': 'Egenföretagare',
        
        # Specific industry roles
        r'begravningsrådgivare|begravningsentreprenör': 'Begravningsrådgivare',
        
        # Other
        r'strateg': 'Strateg',
        r'pensionär': 'Pensionär'
    },

    'reflektion': {
        # Lärande & Utveckling
        r'utveckl\w*|lära\w*|förbättr\w*|insikt\w*': 'Lärande & Utveckling',
        
        # Thinking Process (?)
        r'tänka|tänker|tanke|fundera|analysera|begrunda|klura|metatänk': 'Tankeproccess',
        
        # Tid & Paus
        r'tid|paus|stanna upp|vila|återhämtning|landa|avslappning|slappna av': 'Tid & Paus',
        
        # Utvärdering
        r'utvärder|återkoppling|tillbakablick|genomgång|resumé': 'Utvärdering',
        
        # Mindfulness (?)
        r'själv|medveten|känna|självkännedom|inre': 'Självmedvetenhet',
        
        # Decision Making (?)
        r'beslut|problem|lös|prioriter|val': 'Beslutsfattande',
        
        # Perspecktiv & Förståelse (?)
        r'perspektiv|förstå|helikoptervy|zooma ut|överblick': 'Perspektiv',
        
        # Emotional / Mental state?
        r'lugn|stillhet|ro|känsl|klarhet|sinnesro': 'Sinnestillstånd',
        
        # Metodik
        r'struktur|metod|systematisk|ordning': 'Struktur & Metod',
        
        # Värde / Betydelse (?)
        r'viktig|värde|nödvändig|avgörande': 'Betydelse'
    },

}

def printDict(inDict, print_key=True):
    for k, v in inDict.items():
        if print_key:
            print(f"{k}:\n")
        
        if isinstance(v, dict):
            printDict(v, print_key=False)
        else:
            print(v)
    print("\n")


if __name__ == "__main__":
    printDict(maps)