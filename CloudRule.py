
class CloudRule:

    @staticmethod
    def is_with_cb(station_cloud):

        if station_cloud["cloud_group"][2] == "9" or station_cloud["cloud_group"][2] == "3" :
            return True
        else:
            return False

    @staticmethod
    def apply_135_no_cb(layers):
        all_layers = layers["all_layers"]

        if len(all_layers) == 1:
            return f"{layers["synop"]}="

        elif len(all_layers) == 2:
            amount_second_layer = int(all_layers[1][1])

            if amount_second_layer < 3:
                return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."
            else:
                return f"{layers["synop"]}="

        elif len(all_layers) == 3:
            amount_second_layer = int(all_layers[1][1])
            amount_third_layer = int(all_layers[2][1])

            if amount_second_layer < 3 or amount_third_layer < 5:
                return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."

            else:
                return f"{layers["synop"]}="

        elif len(all_layers) == 4:
            return f"{layers["synop"]}= Cloud layers should not exceed three when there's no Cb"


    @staticmethod
    def apply_135_with_cb(layers):
        all_layers = layers["all_layers"]
        if all_layers[0][2] == "9":
            if len(all_layers) == 1:
                return f"{layers["synop"]}="

            elif len(all_layers) == 2:
                amount_second_layer = int(all_layers[1][1])
                if amount_second_layer < 3:
                    return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."
                else:
                    return f"{layers["synop"]}="

            elif len(all_layers) == 3:
                    amount_second_layer = int(all_layers[1][1])
                    amount_third_layer = int(all_layers[2][1])

                    if amount_second_layer < 3 or amount_third_layer < 5:
                        return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."
                    else:
                        return f"{layers["synop"]}="

            elif len(all_layers) == 4:
                    amount_second_layer = int(all_layers[1][1])
                    amount_third_layer = int(all_layers[2][1])
                    amount_fourth_layer = int(all_layers[3][1])

                    if amount_second_layer < 3 or amount_third_layer < 5 or amount_fourth_layer <8:
                        return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."
                    else:
                        return f"{layers["synop"]}="
        else:
            if len(all_layers) <= 2:
                return f"{layers["synop"]}="

            elif len(all_layers) == 3:
                amount_third_layer = int(all_layers[2][1])

                if amount_third_layer < 3 :
                    return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."
                else:
                    return f"{layers["synop"]}="

            elif len(all_layers) == 4:
                amount_third_layer = int(all_layers[2][1])
                amount_fourth_layer = int(all_layers[3][1])


                if amount_third_layer < 3 or amount_fourth_layer < 5 :
                    return f"{layers["synop"]}= Cloud amount does not follow 135 Rule."

                else:
                    return f"{layers["synop"]}="
