import sys
sys.path.insert(0, "/Volumes/Transcend/repositories/Aglaia/data_manip/")
import data_utils as dau

data = dau.Data_extraction(XML_input="/Volumes/Transcend/data_sets/Ch4+CN_no_relaxation_2.2.xml")
# data.molpro_to_qml_format("/Volumes/Transcend/data_sets/ccsd", "_uCCSD_avtz.out")

data.xml_to_qml()
