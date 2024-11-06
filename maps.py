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


    # Gå direkt på lösning

    'hinder': {
        # Time Related
        r'\btid\w*|hinner|prioriter|kalender|fullboka|almanacka|för mycket att göra': 'Tidsbrist',
        
        # Stress
        r'stress|press|tempo|sprint|snabb|bråttom|rus': 'Stress & Tempo',
        
        # Work Environment
        r'möte|arbetsbelastning|deadline|leverans|jobb|arbetsdagen': 'Arbetssituation',
        
        # Distractions
        r'avbrott|störning|brus|mobil|skärm|distrah|social': 'Störningsmoment',
        
        # Mental State
        r'oro|ångest|trött|energi|orka|fokus|splittrad': 'Mentalt tillstånd',
        
        # Personal Discipline
        r'disciplin|självdisciplin|rutin|prioritering|tar sig inte|egen': 'Självdisciplin',
        
        # External Demands
        r'krav|måste|deadlines|förväntn|prestation': 'Externa krav',
        
        # Environmental
        r'miljö|plats|utrymme|ostörd|lugn': 'Miljöfaktorer',
        
        # Life Balance
        r'familj|liv|småbarn|privat|vardagen|logistik': 'Livspussel',
        
        # Organizational Culture
        r'\w*kultur|värde|förstå|acceptans|premierar|klassas': 'Organisationskultur',
        
        # Fear
        r'rädsla|våga|jobbigt|svår|upptäck|förändra': 'Rädsla & Motstånd',
        
        # No Blockers
        r'inga|inget|kan inte komma på några': 'Inga hinder'
    },


    'ja_nej_svar': {
        r'^ja\b|^ja\s|^ja,|^ja!|^ja\.|^absolut|^ja faktiskt|^oftast\b|^ganska nöjd|^(idag|nu) (gör|ja|jag) (det|de)': 'Ja',
        r'^nej\b|^nej\s|^nej,|^nej\.|^nope|^absolut inte\.?|^tyvärr inte\.?|skulle gärna|^för lite|kunde vara mer|önskar|^inte alltid|kan bli bättre': 'Nej',
        r'vet inte|vet ej|osäker|kanske|^nja\b|både och|olika|i perioder|ja och nej|ibland|^oftast inte|periodvis|skulle säkert': 'Vet ej'
    },



    'yrkesroller': {
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