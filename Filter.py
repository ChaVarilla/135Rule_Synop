import re

class Filters:
    def __init__(self,text_file):
        self.SYNOPTIC_STATIONS = ['98134', '98223', '98232', '98325', '98328', '98336',
                                 '98429', '98430', '98431', '98440', '98444', '98526',
                                 '98531', '98536', '98543', '98618', '98630', '98646',
                                 '98653', '98741', '98753', '98755', '98836', '98132',
                                 '98133', '98222', '98233', '98324', '98327', '98334',
                                 '98426', '98427', '98428', '98432', '98433', '98434',
                                 '98435', '98446', '98538', '98546', '98548', '98553',
                                 '98558', '98642', '98644', '98648', '98746', '98751',
                                 '98752', '98851', '98329', '98332', '98422', '98425',
                                 '98437', '98545', '98550', '98602', '98643', '98748']

        self.text_file = text_file


    def filter_synoptic_data(self):
        observations = []
        with open(self.text_file) as data:
            for line in data:
                if str(line[0:5]) in self.SYNOPTIC_STATIONS:
                    synop_split = re.split(r'[=;RHTtsrS]',line)
                    synop_data = synop_split[0]
                    observations.append(synop_data)

        return observations


    @staticmethod
    def filter_with_cloud_group(filtered_obs):
        stations_with_clouds = {}

        for synop in filtered_obs:
            list_synop = synop.split(" ")

            try:
                all_clouds = [item for item in list_synop if item[0]=="8" and list_synop.index(item) != 2]

            except IndexError:
                pass

            else:
                stations_with_clouds[list_synop[0]] = {}
                stations_with_clouds[list_synop[0]]["cloud_group"] = all_clouds[0]
                stations_with_clouds[list_synop[0]]["all_layers"] = all_clouds[1:]
                stations_with_clouds[list_synop[0]]["synop"] = synop

        return stations_with_clouds

