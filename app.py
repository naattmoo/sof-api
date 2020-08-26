from flask import Flask,  request
import json


app = Flask(__name__)


@app.route("/sof/", methods=['GET', 'POST'])
def sof():
    productName = request.args.get('productName')
    result=[{"product":"Virtual Remote Access Service","attributes":[{"name":"Submitter Emails","value":""},{"name":"Operational Contact","value":""},{"name":"Service Center Region","value":""},{"name":"Service Center Location","value":""},{"name":"NFH Point of Presence","value":""},{"name":"Customer VDOM Name","value":""},{"name":"Customer VDOM Short Name","value":""},{"name":"Syslog Server IP Address","value":""},{"name":"Interlink IP Address - Customer VDOM side","value":""},{"name":"Interlink IP Address - Inet VDOM side","value":""},{"name":"Network Mask","value":""},{"name":"Customer MPLS VPN","value":""},{"name":"Customer's Private IP Prefix","value":""},{"name":"Private IP Prefix Addresing","value":""},{"name":"Delegate's Private IP Prefix","value":""},{"name":"IP range start of users VPN SSL","value":""},{"name":"Ip range end of users VPN SSL","value":""},{"name":"Ip range start of users VPN IPSec","value":""},{"name":"Ip range end of users VPN IPSec","value":""},{"name":"Designated Fortinet Cluster","value":""},{"name":"Name of Interlink to Inet VDOM","value":""},{"name":"RAS Tunnel Termination Public IP Address","value":""},{"name":"SSL certificate","value":""}]}]
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
