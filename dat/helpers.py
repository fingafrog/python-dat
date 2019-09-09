import pandas as pd
from .dat import Session

class PandasWrapper(Session):
    @staticmethod
    def historicals_json_to_df(json):
        columns = ['origin_geography', 'destination_geography', 'miles',
            'origin_id', 'origin_text', 'destination_id', 'destination_text',
            'equipment_category', 'rate_type', 'average_linehaul',
            'high_linehaul', 'low_linehaul', 'average_fuel_surcharge',
            'contributors', 'contributions', 'days_back']
        data = []
        for idx in range(0, len(json['result'])):
            values = json['result'][idx]
            data.append(
                [values['originGeography'],
                values['destinationGeography'],
                values['miles'],
                values['actualLane']['origin']['id'],
                values['actualLane']['origin']['text'],
                values['actualLane']['destination']['id'],
                values['actualLane']['destination']['text'],
                values['actualLane']['equipmentCategory'],
                values['marketRate']['type'],
                values['marketRate']['averageLinehaulRate']['value'],
                values['marketRate']['highLinehaulRate']['value'],
                values['marketRate']['lowLinehaulRate']['value'],
                values['marketRate']['averageFuelSurcharge']['value'],
                values['marketRate']['contributors'],
                values['marketRate']['contributions'],
                values['daysBack']]
            )
        return pd.DataFrame(data=data, columns=columns)

    def search(self, origin_str, dest_str):
        """Using search_str ('city, state, zip') get dataframe of historical
        data from Dat."""
        origin_id = self.search_locations(origin_str)[0]['handle']
        dest_id = self.search_locations(dest_str)[0]['handle']
        historical_data = self.search_historicals(origin_id, dest_id)
        return self.historicals_json_to_df(historical_data)
