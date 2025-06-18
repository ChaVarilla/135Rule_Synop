from Filter import Filters
from CloudRule import CloudRule


class_filters = Filters("SMPH01_RPMM_150000.txt")
synop_data = class_filters.filter_synoptic_data()
cloud_data = class_filters.filter_with_cloud_group(synop_data)
class_cloud_rule = CloudRule()

output_text = ""

for key,value in cloud_data.items():
    if class_cloud_rule.is_with_cb(value):

        output_text += f"{class_cloud_rule.apply_135_with_cb(value)}\n"

    else:
        output_text += f"{class_cloud_rule.apply_135_no_cb(value)}\n"

with open("Corrected_Synop_135_Rule.txt","w") as data:
    data.write(output_text)

