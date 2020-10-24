#####  API documentation reference ===     https://www.astrologyapi.com/docs/indian-astrology

import sdk
import json

class BasicAstroDetails:
    def __init__(self, userID, apiKey, dateOfBirth, monthOfBirth, yearOfBirth,hour, min, lat, lon, tzone):
        self.userID = userID
        self.apiKey = apiKey
        self.dateOfBirth = dateOfBirth
        self.monthOfBirth = monthOfBirth
        self.yearOfBirth = yearOfBirth
        self.hour = hour
        self.min = min
        self.lat = lat
        self.lon = lon
        self.tzone = tzone

    def astro_data(self):
        astro_data = dict()
        astro_data['day'] = self.dateOfBirth,
        astro_data['month'] = self.monthOfBirth,
        astro_data['year'] = self.yearOfBirth,
        astro_data['hour'] = self.hour,
        astro_data['min'] = self.min,
        astro_data['lat'] = self.lat,
        astro_data['lon'] = self.lon,
        astro_data['tzone'] = self.tzone
        return astro_data

    def varshaphal_astro_data(self, varshaphal_year):
        astro_data = dict()
        astro_data['day'] = self.dateOfBirth,
        astro_data['month'] = self.monthOfBirth,
        astro_data['year'] = self.yearOfBirth,
        astro_data['hour'] = self.hour,
        astro_data['min'] = self.min,
        astro_data['lat'] = self.lat,
        astro_data['lon'] = self.lon,
        astro_data['tzone'] = self.tzone
        astro_data['varshaphal_year'] = varshaphal_year
        return astro_data

    def birth_details(self, resource = 'birth_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_details = self.astro_data()
        birthData = vedicRishi.birthDetailsCall(resource, astro_details)
        loaded_json = json.loads(birthData.text)
        return {
            'year': loaded_json['year'],
            'month': loaded_json['month'],
            'day': loaded_json['day'],
            'hour': loaded_json['hour'],
            'minute': loaded_json['minute'],
            'latitude': loaded_json['latitude'],
            'longitude': loaded_json['longitude'],
            'timezone': loaded_json['timezone'],
            'sunrise': loaded_json['sunrise'],
            'sunset': loaded_json['sunset'],
            'ayanamsha': loaded_json['ayanamsha']
        }

    def astro_details(self, resource = 'astro_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_details = self.astro_data()
        astroData = vedicRishi.astroDetailsCall(resource,astro_details)
        loaded_json = json.loads(astroData.text)
        return {
            "ascendant": loaded_json['ascendant'],
            "Varna": loaded_json['Varna'],
            "Vashya": loaded_json['Vashya'],
            "Yoni": loaded_json['Yoni'],
            "Gan": loaded_json['Gan'],
            "Nadi": loaded_json['Nadi'],
            "SignLord": loaded_json['SignLord'],
            "sign": loaded_json['sign'],
            "Naksahtra": loaded_json['Naksahtra'],
            "NaksahtraLord": loaded_json['NaksahtraLord'],
            "Charan": loaded_json['Charan'],
            "Yog": loaded_json['Yog'],
            "Karan": loaded_json['Karan'],
            "Tithi": loaded_json['Tithi'],
            "yunja": loaded_json['yunja'],
            "tatva": loaded_json['tatva'],
            "name_alphabet": loaded_json['name_alphabet'],
            "paya": loaded_json['paya']
        }

    def planet_details(self, resource = 'planets'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.planetDetailsCall(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json,indent=2)

    def planet_details_extended(self, resource='planets/extended'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.planetDetailsExtendedCall(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def bhav_madhya(self, resource='bhav_madhya'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.Bhav_madhya(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def ayanamsha(self, resource='ayanamsha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.ayanamsha(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def tropical(self, resource='ayanamsha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.tropical(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def house_cusps_tropical(self, resource='house_cusps/tropical'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.house_cusps_tropical(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    # Not subsribed
    def natal_wheel_chart(self, resource='natal_wheel_chart'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.natalWheelChart(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

class Life_reports:
    def __init__(self, userId, apiKey, dateOfBirth, monthOfBirth, yearOfBirth,hour, min, lat, lon, tzone):
        self.userID = userID
        self.apiKey = apiKey
        self.dateOfBirth = dateOfBirth
        self.monthOfBirth = monthOfBirth
        self.yearOfBirth = yearOfBirth
        self.hour = hour
        self.min = min
        self.lat = lat
        self.lon = lon
        self.tzone = tzone

    def astro_data(self):
        astro_data = dict()
        astro_data['day'] = self.dateOfBirth,
        astro_data['month'] = self.monthOfBirth,
        astro_data['year'] = self.yearOfBirth,
        astro_data['hour'] = self.hour,
        astro_data['min'] = self.min,
        astro_data['lat'] = self.lat,
        astro_data['lon'] = self.lon,
        astro_data['tzone'] = self.tzone
        return astro_data

    def general_house_report(self, resource='general_house_report/'):
        planets = ['sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn']
        for i in range(len(planets)):
            resource += str(planets[i])
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_house_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def general_rashi_report(self, resource='general_rashi_report/'):
        planets = ['moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn']
        for i in range(len(planets)):
            resource += str(planets[i])
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def general_ascendant_report(self, resource='general_ascendant_report'):
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def general_nakshatra_report(self, resource='general_nakshatra_report'):
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def planet_nature(self, resource='planet_nature'):
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def kalsarpa_details(self, resource='kalsarpa_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def manglik(self, resource='manglik'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def sadhesati_current_status(self, resource='sadhesati_current_status'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def sadhesati_life_details(self, resource='sadhesati_life_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def pitra_dosha_report(self, resource='pitra_dosha_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def lalkitab_horoscope(self, resource='lalkitab_horoscope'):
        planets = ['sun','moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn']
        for i in range(len(planets)):
            resource += str(planets[i])
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def lalkitab_debts(self, resource='lalkitab_debts'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def lalkitab_remedies(self, resource='lalkitab_remedies/sun'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def lalkitab_houses(self, resource='lalkitab_houses'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def lalkitab_planets(self, resource='lalkitab_planets'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def biorhythm(self, resource='biorhythm'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def moon_biorhythm(self, resource='moon_biorhythm'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def puja_suggestion(self, resource='puja_suggestion'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def basic_gem_suggestion(self, resource='basic_gem_suggestion'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def rudraksha_suggestion(self, resource='rudraksha_suggestion'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sadhesati_remedies(self, resource='sadhesati_remedies'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def daily_nakshatra_prediction(self, resource='daily_nakshatra_prediction'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def daily_nakshatra_prediction_next(self, resource='daily_nakshatra_prediction/next'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def daily_nakshatra_prediction_previous(self, resource='daily_nakshatra_prediction/previous'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def custom_nakshatra_prediction(self, resource='custom_nakshatra_prediction'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def daily_nakshatra_consolidated(self, resource='daily_nakshatra_consolidated'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def planet_ashtak(self, resource='planet_ashtak'):
        planets = ['sun','moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn','ascendant']
        for i in range(len(planets)):
            resource += str(planets[i])
            vedicRishi = sdk.VRClient(self.userID, self.apiKey)
            astro_data = self.astro_data()
            astroData = vedicRishi.general_report(resource, astro_data)
            loaded_json = json.loads(astroData.text)
            return json.dumps(loaded_json, indent=2)

    def sarvashtak(self, resource='sarvashtak'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)


    def current_vdasha_all(self, resource='current_vdasha_all'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def major_vdasha(self, resource='major_vdasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def current_vdasha(self, resource='current_vdasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def current_vdasha_date(self, resource='current_vdasha_date'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_vdasha_md(self, resource='sub_vdasha/:md'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_sub_vdasha(self, resource='sub_sub_vdasha/:md/:ad'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_sub_sub_vdasha(self, resource='sub_sub_sub_vdasha/:md/:ad/:pd'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_sub_sub_sub_vdasha(self, resource='sub_sub_sub_sub_vdasha/:md/:ad/:pd/:sd'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def kp_planets(self, resource='kp_planets'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def kp_house_cusps(self, resource='kp_house_cusps'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def kp_birth_chart(self, resource='kp_birth_chart'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def kp_house_significator(self, resource='kp_house_significator'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def kp_planet_significator(self, resource='kp_planet_significator'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def major_chardasha(self, resource='major_chardasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def current_chardasha(self, resource='current_chardasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_chardasha(self, resource='sub_chardasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_sub_chardasha(self, resource='sub_sub_chardasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def major_yogini_dasha(self, resource='sub_sub_chardasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_yogini_dasha_dashaCycle_dashaName(self, resource='sub_yogini_dasha/:dashaCycle/:dashaName'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def sub_yogini_dasha(self, resource='sub_yogini_dasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def current_yogini_dasha(self, resource='current_yogini_dasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_table(self, resource='numero_table'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_report(self, resource='numero_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_fav_time(self, resource='numero_fav_time'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_place_vastu(self, resource='numero_place_vastu'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_fasts_report(self, resource='numero_fasts_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_fav_lord(self, resource='numero_fav_lord'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_fav_mantra(self, resource='numero_fav_mantra'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def numero_prediction_daily(self, resource='numero_prediction/daily'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    ###########     Panchang ##############

    def basic_panchang_sunrise(self, resource='basic_panchang/sunrise'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def basic_panchang(self, resource='basic_panchang'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def advanced_panchang_sunrise(self, resource='advanced_panchang/sunrise'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def advanced_panchang(self, resource='advanced_panchang'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def planet_panchang_sunrise(self, resource='planet_panchang/sunrise'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def planet_panchang(self, resource='planet_panchang'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def chaughadiya_muhurta(self, resource='chaughadiya_muhurta'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def hora_muhurta(self, resource='hora_muhurta'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def hora_muhurta_dinman(self, resource='hora_muhurta_dinman'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def panchang_chart(self, resource='panchang_chart'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def panchang_chart_sunrise(self, resource='panchang_chart/sunrise'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def find_nakshatra(self, resource='find_nakshatra/:nakshatraName'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def tamil_panchang(self, resource='tamil_panchang'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def tamil_month_panchang(self, resource='/tamil_month_panchang'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

class matchMakingData:
    def __init__(self,userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone):
        self.userID = userID
        self.apiKey = apiKey
        self.maleData = {}
        self.femaleData = {}
        self.maleData['date'] = mday
        self.maleData['month'] = mmonth
        self.maleData['year'] = myear
        self.maleData['hour'] = mhour
        self.maleData['minute'] = mmin
        self.maleData['latitude'] = mlat
        self.maleData['longitude'] = mlon
        self.maleData['timezone'] = mtzone
        self.femaleData['date'] = fday
        self.femaleData['month'] = fmonth
        self.femaleData['year'] = fyear
        self.femaleData['hour'] = fhour
        self.femaleData['minute'] = fmin
        self.femaleData['latitude'] = flat
        self.femaleData['longitude'] = flon
        self.femaleData['timezone'] = ftzone

    def match_astro_details(self, resource='match_astro_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_planet_details(self, resource='match_planet_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_manglik_report(self, resource='match_manglik_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_making_report(self, resource='match_making_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_simple_report(self, resource='match_simple_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_making_detailed_report(self, resource='match_making_detailed_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_dashakoot_points(self, resource='match_dashakoot_points'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_percentage(self, resource='match_percentage'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def partner_report(self, resource='partner_report'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def custom_match_profiles(self, resource='custom_match_profiles'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def custom_match_profiles_xml(self, resource='custom_match_profiles_xml'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def papasamyam_details(self, resource='papasamyam_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_ashtakoot_points(self, resource='match_ashtakoot_points'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_birth_details(self, resource='match_birth_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

    def match_obstructions(self, resource='match_obstructions'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        maleData = self.maleData
        femaleData = self.femaleData
        matchMakingData = vedicRishi.matchMakingCall(resource, maleData, femaleData)
        loaded_json = json.loads(matchMakingData.text)
        return json.dumps(loaded_json, indent=2)

class Varshaphal:
    def __init__(self, userId, apiKey, dateOfBirth, monthOfBirth, yearOfBirth,hour, min, lat, lon, tzone, varshaphal_year):
        self.userID = userID
        self.apiKey = apiKey
        self.dateOfBirth = dateOfBirth
        self.monthOfBirth = monthOfBirth
        self.yearOfBirth = yearOfBirth
        self.hour = hour
        self.min = min
        self.lat = lat
        self.lon = lon
        self.tzone = tzone
        self.varshaphal_year = varshaphal_year

    def astro_data(self):
        astro_data = dict()
        astro_data['day'] = self.dateOfBirth,
        astro_data['month'] = self.monthOfBirth,
        astro_data['year'] = self.yearOfBirth,
        astro_data['hour'] = self.hour,
        astro_data['min'] = self.min,
        astro_data['lat'] = self.lat,
        astro_data['lon'] = self.lon,
        astro_data['tzone'] = self.tzone
        astro_data['varshaphal_year'] = self.varshaphal_year
        return astro_data


    def varshaphal_year_chart(self, resource='varshaphal_year_chart'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_month_chart(self, resource='varshaphal_month_chart'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_details(self, resource='varshaphal_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_planets(self, resource='varshaphal_planets'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_muntha(self, resource='varshaphal_muntha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_mudda_dasha(self, resource='varshaphal_mudda_dasha'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_panchavargeeya_bala(self, resource='varshaphal_panchavargeeya_bala'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_harsha_bala(self, resource='varshaphal_harsha_bala'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_saham_points(self, resource='varshaphal_saham_points'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def varshaphal_yoga(self, resource='varshaphal_yoga'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

class GeoDetails:
    def __init__(self, user_id,apiKey,place,max_rows, country_code, isDst, latitude, longitude,date):
        self.userID = user_id
        self.apiKey = apiKey
        self.place = place
        self.max_rows = max_rows
        self.country_code = country_code
        self.isDst = isDst
        self.latitude = latitude
        self.longitude = longitude
        self.date = date

    def astro_data(self):
        astro_data = dict()
        astro_data['place'] = self.place,
        astro_data['max_rows'] = self.max_rows,
        astro_data['country_code'] = self.country_code,
        astro_data['isDst'] = self.isDst,
        astro_data['latitude'] = self.latitude,
        astro_data['longitude'] = self.longitude,
        astro_data['date'] = self.date

    def geo_details(self, resource='geo_details'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def timezone(self, resource='timezone'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

    def timezone_with_dst(self, resource='timezone_with_dst'):
        vedicRishi = sdk.VRClient(self.userID, self.apiKey)
        astro_data = self.astro_data()
        astroData = vedicRishi.general_report(resource, astro_data)
        loaded_json = json.loads(astroData.text)
        return json.dumps(loaded_json, indent=2)

#############   Test data #####################
dateOfBirth = 25
monthOfBirth = 12
yearOfBirth = 1994
hour = 12
min = 32
lat = 25.31668
lon = 83.01042
tzone = 5.5
varshaphal_year = 2017
userID = "Your user ID here"
apiKey = "Your API key here"
resource = 'birth_details'
place = 'mumbai'
max_rows = 6
country_code = 91
isDst = True
latitude = lat
longitude = lon
date = "12-05-1993"

####################    Basic Astro details ####################
birth_details = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).birth_details()
astro_details = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).astro_details()
planet_details = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).planet_details()
planet_details_extended = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).planet_details_extended()
bhav_madhya = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).bhav_madhya()
ayanamsha = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).ayanamsha()
tropical = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).tropical()
house_cusps_tropical = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).house_cusps_tropical()
natal_wheel_chart = BasicAstroDetails(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).natal_wheel_chart()

################    life reports ####################
general_house_reports = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).general_house_report()
general_rashi_reports = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).general_rashi_report()
general_ascendant_report = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).general_ascendant_report()
general_nakshatra_report = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).general_nakshatra_report()
planet_nature = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).general_rashi_report()

###############           Horoscope Dasha  #############################
kalsarpa_details = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kalsarpa_details()
manglik = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).manglik()
sadhesati_current_status = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sadhesati_current_status()
sadhesati_life_details = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sadhesati_life_details()
pitra_dosha_report = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).pitra_dosha_report()

#################           Lalkitab  ######################################
lalkitab_horoscope = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).lalkitab_horoscope()
lalkitab_remedies = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).lalkitab_remedies()
lalkitab_houses = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).lalkitab_houses()
lalkitab_planets = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).lalkitab_planets()

################            Birhythm  ######################
biorhythm = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).biorhythm()
moon_biorhythm = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).moon_biorhythm()

##################          Suggestions and Remedies ########################
puja_suggestion = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).puja_suggestion()
basic_gem_suggestion = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).basic_gem_suggestion()
rudraksha_suggestion = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).rudraksha_suggestion()
sadhesati_remedies = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sadhesati_remedies()

##################          Ashtakvarga  ##########################
planet_ashtak = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).planet_ashtak()
sarvashtak = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sarvashtak()

##################          Vimshotti dasha ###########################
current_vdasha_all = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).current_vdasha_all()
major_vdasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).major_vdasha()
current_vdasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).current_vdasha()
current_vdasha_date = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).current_vdasha_date()
sub_vdasha_md = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_vdasha_md()
sub_sub_vdasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_sub_vdasha()
sub_sub_sub_vdasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_sub_sub_vdasha()
sub_sub_sub_sub_vdasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_sub_sub_vdasha()

##################          Daily Nakshatra Predictions   #############################
daily_nakshatra_prediction = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).daily_nakshatra_prediction()
daily_nakshatra_prediction_next = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).daily_nakshatra_prediction_next()
daily_nakshatra_prediction_previous = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).daily_nakshatra_prediction_previous()
custom_nakshatra_prediction = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).custom_nakshatra_prediction()
daily_nakshatra_consolidated = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).daily_nakshatra_consolidated()

##################              krishnamurthi Paddati    #############################
kp_planets = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kp_planets()
kp_house_cusps = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kp_house_cusps()
kp_birth_chart = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kp_birth_chart()
kp_house_significator = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kp_house_significator()
kp_planet_significator = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).kp_planet_significator()

###################         Char dasha  ############################3
major_chardasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).major_chardasha()
current_chardasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).current_chardasha()
sub_chardasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_chardasha()
sub_sub_chardasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_sub_chardasha()

###########                 Yogini Dasha  ################
major_yogini_dasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).major_yogini_dasha()
#sub_yogini_dasha_dashaCycle_dashaName = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_yogini_dasha_dashaCycle_dashaName()
sub_yogini_dasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).sub_yogini_dasha()
current_yogini_dasha = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).current_yogini_dasha()

##################          Numerology  ##############################
numero_table = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_table()
numero_report = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_report()
numero_fav_time = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_fav_time()
numero_place_vastu = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_place_vastu()
numero_fasts_report = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_fasts_report()
numero_fav_lord = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_fav_lord()
numero_fav_mantra = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_fav_mantra()
numero_prediction_daily = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).numero_prediction_daily()

#######################         Varshapal ################################
varshaphal_year_chart = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_year_chart()
varshaphal_month_chart = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_month_chart()
varshaphal_details = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_details()
varshaphal_planets = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_planets()
varshaphal_muntha = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_muntha()
varshaphal_mudda_dasha = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_mudda_dasha()
varshaphal_panchavargeeya_bala = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_panchavargeeya_bala()
varshaphal_harsha_bala = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_harsha_bala()
varshaphal_saham_points = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_saham_points()
varshaphal_yoga = Varshaphal(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone,varshaphal_year).varshaphal_yoga()


###############    Panchang ##########################
basic_panchang_sunrise = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).basic_panchang_sunrise()
basic_panchang = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).basic_panchang()
advanced_panchang_sunrise = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).advanced_panchang_sunrise()
advanced_panchang = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).advanced_panchang()
planet_panchang_sunrise = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).planet_panchang_sunrise()
planet_panchang = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).planet_panchang()
chaughadiya_muhurta = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).chaughadiya_muhurta()
hora_muhurta = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).hora_muhurta()
hora_muhurta_dinman = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).hora_muhurta_dinman()
panchang_chart = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).panchang_chart()
panchang_chart_sunrise = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).panchang_chart_sunrise()
tamil_month_panchang = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).tamil_month_panchang()
#find_nakshatra = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).find_nakshatra()
tamil_panchang = Life_reports(userID,apiKey,dateOfBirth,monthOfBirth,yearOfBirth,hour,min,lat,lon,tzone).tamil_panchang()


#######  Match making test data #############
mday= 25
mmonth=12
myear=1988
mhour=4
mmin=0
mlat=25.123
mlon=82.34
mtzone=5.5
fday=27
fmonth=1
fyear=1990
fhour=13
fmin=36
flat=25.123
flon= 82.34
ftzone= 5.5
match_astro_details = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_astro_details()
match_planet_details = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_planet_details()
match_manglik_report = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_manglik_report()
match_making_report = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_making_report()
match_simple_report = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_simple_report()
match_making_detailed_report = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_making_detailed_report()
match_dashakoot_points = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_dashakoot_points()
match_percentage = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_percentage()
partner_report = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).partner_report()
custom_match_profiles = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).custom_match_profiles()
custom_match_profiles_xml = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).custom_match_profiles_xml()
papasamyam_details = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).papasamyam_details()
match_birth_details = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_birth_details()
match_ashtakoot_points = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_ashtakoot_points()
match_obstructions = matchMakingData(userID,apiKey,mday,mmonth,myear,mhour,mmin,mlat,mlon,mtzone,fday,fmonth,fyear,fhour,fmin,flat,flon,ftzone).match_obstructions()

###############            Geo details   #####################
# geo_details = GeoDetails(userID,apiKey,place,max_rows,country_code,isDst,latitude,longitude,date).geo_details()
# timezone = GeoDetails(userID,apiKey,place,max_rows,country_code,isDst,latitude,longitude,date).timezone()
# timezone_with_dst = GeoDetails(userID,apiKey,place,max_rows,country_code,isDst,latitude,longitude,date).timezone_with_dst()


#############      Testdata    #########################
# vedicRishi = sdk.VRClient(userID, apiKey)
# birthData = vedicRishi.birthDetailsCall(resource, dateOfBirth, monthOfBirth, yearOfBirth, hour, min, lat, lon, tzone)
# loaded_json = json.loads(birthData.text)
# print(birth_details)
# print(tropical)
# print(house_cusps_tropical)
# print(natal_wheel_chart)
#print(lalkitab_horoscope_dasha)
# print(daily_nakshatra_prediction_next)
# print(sarvashtak)
#print(kp_house_significator)


