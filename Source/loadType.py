class LoadType:
    def __init__(self):
        self.load_name = ["Dead","Superdead","Live","Reducelive","Quake",
                                "Wind","Snow","Other","Move","Temperature","Rooflive",
                                "Notional","Patternlive","Wave","Braking","Centrifugal",
                                "Friction","Ice","Windonliveload","Horizontalearthpressure",
                                "Verticalearthpressure","Earthsurcharge","Downdrag","Vehiclecollision",
                                "Vesselcollision","Temperaturegradient","Settlement","Shrinkage","Creep",
                                "Waterloadpressure","Liveloadsurcharge","Lockedinforces",
                                "Pedestrianll","Prestress","Hyperstatic","Bouyancy","Streamflow","Impact","Construction"]
        self.load_types_tuple = (
            ("Dead", "D"),
            ("Superdead", "SD"),
            ("Live", "L"),
            ("Reducelive", "RL"),
            ("Quake", "Q"),
            ("Wind", "W"),
            ("Snow", "SN"),
            ("Other", "O"),
            ("Move", "M"),
            ("Temperature", "T"),
            ("Rooflive", "RFL"),
            ("Notional", "N"),
            ("Patternlive", "PL"),
            ("Wave", "WV"),
            ("Braking", "B"),
            ("Centrifugal", "CF"),
            ("Friction", "FR"),
            ("Ice", "IC"),
            ("Windonliveload", "WLL"),
            ("Horizontalearthpressure", "HEP"),
            ("Verticalearthpressure", "VEP"),
            ("Earthsurcharge", "ES"),
            ("Downdrag", "DD"),
            ("Vehiclecollision", "VC"),
            ("Vesselcollision", "VSC"),
            ("Temperaturegradient", "TG"),
            ("Settlement", "ST"),
            ("Shrinkage", "SHR"),
            ("Creep", "CR"),
            ("Waterloadpressure", "WLP"),
            ("Liveloadsurcharge", "LLS"),
            ("Lockedinforces", "LF"),
            ("Pedestrianll", "PDL"),
            ("Prestress", "PS"),
            ("Hyperstatic", "HS"),
            ("Bouyancy", "BY"),
            ("Streamflow", "SF"),
            ("Impact", "IM"),
            ("Construction", "CN")
        )

        self.DEAD = 1
        self.SUPERDEAD = 2
        self.LIVE = 3
        self.REDUCELIVE = 4
        self.QUAKE = 5
        self.WIND= 6
        self.SNOW = 7
        self.OTHER = 8
        self.MOVE = 9
        self.TEMPERATURE = 10
        self.ROOFLIVE = 11
        self.NOTIONAL = 12
        self.PATTERNLIVE = 13
        self.WAVE= 14
        self.BRAKING = 15
        self.CENTRIFUGAL = 16
        self.FRICTION = 17
        self.ICE = 18
        self.WINDONLIVELOAD = 19
        self.HORIZONTALEARTHPRESSURE = 20
        self.VERTICALEARTHPRESSURE = 21
        self.EARTHSURCHARGE = 22
        self.DOWNDRAG = 23
        self.VEHICLECOLLISION = 24
        self.VESSELCOLLISION = 25
        self.TEMPERATUREGRADIENT = 26
        self.SETTLEMENT = 27
        self.SHRINKAGE = 28
        self.CREEP = 29
        self.WATERLOADPRESSURE = 30
        self.LIVELOADSURCHARGE = 31
        self.LOCKEDINFORCES = 32
        self.PEDESTRIANLL = 33
        self.PRESTRESS = 34
        self.HYPERSTATIC = 35
        self.BOUYANCY = 36
        self.STREAMFLOW = 37
        self.IMPACT = 38
        self.CONSTRUCTION = 39