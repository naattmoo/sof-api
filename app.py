from flask import Flask,  request
import json


app = Flask(__name__)


@app.route("/sof/", methods=['GET', 'POST'])
def sof():
    productName = request.args.get('productName')
    result=[{"product":"Policy Enforcement vRAS","attributes":["Number of Users"]},{"product":"Virtual Remote Access Service","attributes":["Submitter Emails","Operational Contact","Service Center Region","Service Center Location","NFH Point of Presence","Service Contract Term","Customer VDOM Name","Customer VDOM Short Name","Syslog Server IP Address","Interlink IP Address - Customer VDOM side","Interlink IP Address - Inet VDOM side","Network Mask","Customer MPLS VPN","Customer's Private IP Prefix","Private IP Prefix Addresing","Delegate's Private IP Prefix","VPN SSL Users","VPN IPSec Users","Traffic Shapping","BW User","IP range start of users VPN SSL","Ip range end of users VPN SSL","Ip range start of users VPN IPSec","Ip range end of users VPN IPSec","Designated Fortinet Cluster","Name of Interlink to Inet VDOM","RAS Tunnel Termination Public IP Address","SSL certificate"]}]
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
