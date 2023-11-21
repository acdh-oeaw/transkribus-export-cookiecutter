import os
import glob
from saxonche import PySaxonProcessor
from transkribus_utils.transkribus_utils import ACDHTranskribusUtils


# user = os.environ.get("TR_USER")
# pw = os.environ.get("TR_PW")
XSLT = "https://csae8092.github.io/page2tei/page2tei-0.xsl"
METS_DIR = "./mets"
TEI_DIR = "./tei"
os.makedirs(METS_DIR, exist_ok=True)
os.makedirs(TEI_DIR, exist_ok=True)


def getcreds(filename):
    user = pw = ''
    if os.path.isfile(filename):
        with open(filename) as secret:
            for line in secret.readlines():
                element = line.split("=")
                if element[0].strip() == "TR_USER":
                    user = element[1].strip().strip('"')
                elif element[0].strip() == "TR_PW":
                    pw = element[1].strip().strip('"')
    # # Interactive
    # if not (user and pw):
        # user = input("User?\n")
        # pw = input("Password?\n")
        # # An smarter solution would require an additional lib:
        # import getpass
        # pw = getpass.getpass("Password?\n")
    return (user, pw)


user, pw = getcreds('secret.env')

transkribus_client = ACDHTranskribusUtils(
    user=user,
    password=pw,
    transkribus_base_url="https://transkribus.eu/TrpServer/rest"
)


with open('col_ids.txt', 'r') as f:
    lines = lines = [line.rstrip() for line in f.readlines()]
print(lines)

for y in lines:
    col_id = y.strip()
    print(f"processing collection: {col_id}")
    mpr_docs = transkribus_client.collection_to_mets(col_id,
                                                     file_path='./mets')
    print(f"{METS_DIR}/{col_id}*.xml")
    files = glob.glob(f"{METS_DIR}/{col_id}/*_mets.xml")
    for x in files:
        tail = os.path.split(x)[-1]
        doc_id = tail.split('_')[0]
        tei_file = f"{doc_id}.xml"
        print(f"transforming mets: {x} to {tei_file}")
        with PySaxonProcessor(license=False) as proc:
            xsltproc = proc.new_xslt30_processor()
            xsltproc.set_parameter("combine", proc.make_boolean_value(True))
            xsltproc.set_parameter("ab", proc.make_boolean_value(True))
            document = proc.parse_xml(xml_file_name=x)
            executable = xsltproc.compile_stylesheet(stylesheet_file=XSLT)
            output = executable.transform_to_string(xdm_node=document)
            output = output.replace(' type=""', '')
            with open(os.path.join(TEI_DIR, tei_file), "w") as f:
                f.write(output)
