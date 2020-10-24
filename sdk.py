import requests
class VRClient:
    baseURL = "http://api.vedicrishiastro.com/v1/"

    def __init__(self, uid, key):
        self.userID = uid
        self.apiKey = key

    def getUrl(cls):
        return cls.baseURL

    def getResponse(self, resource, data):
        # print(self.userID)
        url = self.getUrl() + resource
        resp = requests.post(url, data=data, auth=(self.userID, self.apiKey))
        return resp

    def packageHoroData(self, date, month, year, hour, minute, latitude, longitude, timezone):
        return {
            'day': date,
            'month': month,
            'year': year,
            'hour': hour,
            'min': minute,
            'lat': latitude,
            'lon': longitude,
            'tzone': timezone
        }

    def packageNumeroData(self, date, month, year, name):
        return {
            'day': date,
            'month': month,
            'year': year,
            'name': name
        }

    def packageMatchMakingData(self, maleBirthData, femaleBirthData):
        mData = {
            'm_day': maleBirthData['date'],
            'm_month': maleBirthData['month'],
            'm_year': maleBirthData['year'],
            'm_hour': maleBirthData['hour'],
            'm_min': maleBirthData['minute'],
            'm_lat': maleBirthData['latitude'],
            'm_lon': maleBirthData['longitude'],
            'm_tzone': maleBirthData['timezone']
        }

        fData = {
            'f_day': femaleBirthData['date'],
            'f_month': femaleBirthData['month'],
            'f_year': femaleBirthData['year'],
            'f_hour': femaleBirthData['hour'],
            'f_min': femaleBirthData['minute'],
            'f_lat': femaleBirthData['latitude'],
            'f_lon': femaleBirthData['longitude'],
            'f_tzone': femaleBirthData['timezone']
        }
        tempData = dict(mData.items() | fData.items())
        return tempData

    def birthDetailsData(self, astrodata):
        return {
            'day': astrodata['day'],
            'month': astrodata['month'],
            'year': astrodata['year'],
            'hour': astrodata['hour'],
            'min': astrodata['min'],
            'lat': astrodata['lat'],
            'lon': astrodata['lon'],
            'tzone': astrodata['tzone']
        }
    def astroDetailsData(self, astrodata):
        return {
            'day': astrodata['day'],
            'month': astrodata['month'],
            'year': astrodata['year'],
            'hour': astrodata['hour'],
            'min': astrodata['min'],
            'lat': astrodata['lat'],
            'lon': astrodata['lon'],
            'tzone': astrodata['tzone'],
        }
    def varshapalDetailsData(self, varshaphal_data):
        return {
            'day': varshaphal_data['day'],
            'month': varshaphal_data['month'],
            'year': varshaphal_data['year'],
            'hour': varshaphal_data['hour'],
            'min': varshaphal_data['min'],
            'lat': varshaphal_data['lat'],
            'lon': varshaphal_data['lon'],
            'tzone': varshaphal_data['tzone'],
            'varshaphal_year': varshaphal_data['varshaphal_year']
        }

    def geodetails_data(self, geo_data):
        return{
            'place':geo_data['place'],
            'max_rows':geo_data['max_rows'],
            'country_code':geo_data['country_code'],
            'isDst':geo_data['isDst'],
            'latitude':geo_data['latitude'],
            'longitude':geo_data['longitude'],
            'date':geo_data['date']
        }

    def call(self, resource, date, month, year, hour, minute, latitude, longitude, timezone):
        data = self.packageHoroData(date, month, year, hour, minute, latitude, longitude, timezone)
        return self.getResponse(resource, data)

    def matchMakingCall(self, resource, maleBirthData, femaleBirthData):
        data = self.packageMatchMakingData(maleBirthData, femaleBirthData)
        return self.getResponse(resource, data)

    def numeroCall(self, resource, date, month, year, name):
        data = self.packageNumeroData(date, month, year, name)
        return self.getResponse(resource, data)

    def birthDetailsCall(self, resource, astro_data):
        data = self.birthDetailsData(astro_data)
        return self.getResponse(resource, data)

    def astroDetailsCall(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def planetDetailsCall(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def planetDetailsExtendedCall(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def Bhav_madhya(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def ayanamsha(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def tropical(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def house_cusps_tropical(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def natalWheelChart(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def general_house_report(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def general_rashi_report(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def general_report(self, resource, astro_data):
        data = self.astroDetailsData(astro_data)
        return self.getResponse(resource, data)

    def varshaphal_report(self, resource, varshaphal_data):
        data = self.astroDetailsData(varshaphal_data)
        return self.getResponse(resource, data)

    def geodata_report(self, resource, geo_data):
        data = self.astroDetailsData(geo_data)
        return self.getResponse(resource, data)
