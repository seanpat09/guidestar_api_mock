from flask import Flask, json

guidestar_info = {
  "code": 200,
  "message": "Request was processed successfully!",
  "took": 42,
  "errors": [],
  "data": {
    "took": 39,
    "total_hits": 1,
    "hits": [
      {
        "organization_id": "7831216",
        "bridge_id": "null",
        "ein": "54-1774039",
        "organization_name": "GuideStar USA",
        "also_known_as": "GuideStar",
        "mission": "GuideStar USA, Inc.'s mission is to revolutionize philanthropy and nonprofit practice by providing information that advances transparency, enables users to make better decisions, and encourages charitable giving.",
        "address_line_1": "4801 Courthouse St",
        "address_line_2": "Ste. 220",
        "city": "Williamsburg",
        "state": "VA",
        "zip": "23188",
        "county": "James City",
        "msa": "VA - Norfolk-Virginia Beach-Newport News, VA-NC",
        "lat_long": "37.3268,-76.7606",
        "ntee_code": "T50 Philanthropy / Charity / Voluntarism Promotion (General)",
        "profile_level": "PLATINUM",
        "public_report": "https://www.guidestar.org/profile/54-1774039",
        "subsection_code": "501(c)(3) Public Charity",
        "number_of_employees": "95",
        "form_type": "990",
        "website_url": "www.guidestar.org",
        "logo_url": "https://wwwguidestar.org/...",
        "foundation_code": "15",
        "parent_orgs": "",
        "bmf_gross_receipts": "11269539",
        "bmf_assets": "3965331",
        "form990_total_revenue": "11253739",
        "form990_total_expenses": "12792537",
        "form990_total_assets": "3965331",
        "contact_email": "jackie.enterline@guidestar.org",
        "contact_name": "Ms. Jackie Enterline",
        "contact_phone": "(202) 637-760",
        "contact_title": "Marketing & Communications Manager",
        "properties": {
          "parent": "false",
          "subordinate": "false",
          "independent": "true",
          "national_hq": "false",
          "revoked": "false",
          "defunct_or_merged": "false",
          "audit_a133_performed": "false",
          "bmf_status": "true",
          "pub78_verified": "true",
          "allow_online_giving": "true"
        }
      }
    ]
  }
}

app = Flask(__name__)

@app.route('/essentials/v1', methods=['POST'])
def get_guidestar():
  return json.dumps(guidestar_info)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)