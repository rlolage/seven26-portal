from pathlib import Path
import argparse, xml.etree.ElementTree as E
parser=argparse.ArgumentParser(description="Configure test-org portal admin and sender.")
parser.add_argument("--admin-username",required=True)
parser.add_argument("--sender-email",required=True)
a=parser.parse_args()
if "@" not in a.admin_username or "@" not in a.sender_email: parser.error("Provide a Salesforce username and email address.")
base=Path(__file__).resolve().parent/"portal-src/main/default"
uri="http://soap.sforce.com/2006/04/metadata"; ns={"m":uri};E.register_namespace("",uri)
for rel,values in [("sites/seven26fitness.site-meta.xml",{"siteAdmin":a.admin_username,"siteGuestRecordDefaultOwner":a.admin_username}),("networks/seven26fitness.network-meta.xml",{"emailSenderAddress":a.sender_email})]:
 f=base/rel;t=E.parse(f);r=t.getroot()
 for tag,value in values.items():r.find("m:"+tag,ns).text=value
 E.indent(t,space="    ");t.write(f,encoding="UTF-8",xml_declaration=True)
print("Portal admin and email configured. No Salesforce changes were made.")
