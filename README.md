---Working code----
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 300,
  "width": 240,
  "hideSelection": true,
  "formatter": {
    "elmType": "div",
    "style": {
      "display": "flex",
      "flex-direction": "column",
      "align-items": "center",
      "padding": "16px",
      "margin": "8px",
      "border-radius": "10px",
      "box-shadow": "0 2px 6px rgba(0,0,0,0.15)",
      "background-color": "white"
    },
    "children": [
      {
        "elmType": "img",
        "attributes": {
          "src": "=[$field_8]"
        },
        "style": {
          "display": "=if([$field_8] != '', 'block', 'none')",
          "width": "84px",
          "height": "84px",
          "border-radius": "50%",
          "object-fit": "cover",
          "margin-bottom": "10px"
        }
      },
      {
        "elmType": "div",
        "style": {
          "display": "=if([$field_8] != '', 'none', 'flex')",
          "width": "84px",
          "height": "84px",
          "border-radius": "50%",
          "background-color": "#0b3d66",
          "align-items": "center",
          "justify-content": "center",
          "color": "white",
          "font-size": "26px",
          "font-weight": "600",
          "margin-bottom": "10px"
        },
        "txtContent": "=substring([$Title], 0, 1) + substring([$field_1], 0, 1)"
      },
      {
        "elmType": "div",
        "style": {
          "font-size": "16px",
          "font-weight": "600",
          "color": "#0b3d66",
          "text-align": "center"
        },
        "txtContent": "=[$Title] + ' ' + [$field_1]"
      },
      {
        "elmType": "div",
        "style": {
          "font-size": "13px",
          "color": "#444",
          "text-align": "center",
          "margin-top": "2px"
        },
        "txtContent": "=[$field_3]"
      },
      {
        "elmType": "div",
        "style": {
          "font-size": "12px",
          "color": "#777",
          "text-align": "center",
          "margin-bottom": "8px"
        },
        "txtContent": "=[$field_2] + ' • ' + [$field_7]"
      },
      {
        "elmType": "a",
        "attributes": {
          "href": "=if([$field_4] != '', 'mailto:' + [$field_4], '')",
          "target": "_blank"
        },
        "style": {
          "font-size": "12px",
          "color": "#0b3d66",
          "text-decoration": "none",
          "margin-bottom": "2px"
        },
        "txtContent": "=[$field_4]"
      },
      {
        "elmType": "a",
        "attributes": {
          "href": "=if([$field_5] != '', 'tel:' + [$field_5], '')"
        },
        "style": {
          "font-size": "12px",
          "color": "#444",
          "text-decoration": "none"
        },
        "txtContent": "=[$field_5]"
      }
    ]
  }
}

---------test jsons--------------
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 310,
  "width": 240,
  "hideSelection": true,
  "formatter": {
    "elmType": "div",
    "style": {
      "display": "flex",
      "flex-direction": "column",
      "align-items": "center",
      "padding": "0",
      "margin": "8px",
      "border-radius": "10px",
      "overflow": "hidden",
      "box-shadow": "0 2px 8px rgba(0,0,0,0.18)",
      "background-color": "white"
    },
    "children": [
      {
        "elmType": "div",
        "style": {
          "width": "100%",
          "height": "96px",
          "flex-shrink": "0",
          "display": "flex",
          "align-items": "center",
          "justify-content": "center",
          "background-color": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|Loans|', '|' + [$field_2] + '|') > -1, '#0f8a7e', if([$field_2] == 'Business Banking', '#b8742a', if(indexOf('|Accounting|Human Resources|Compliance|IT|Operations|Marketing|Facilities|Nashwauk Downtown|', '|' + [$field_2] + '|') > -1, '#6a4c93', '#5b6b7d'))))"
        },
        "children": [
          {
            "elmType": "img",
            "attributes": { "src": "=[$field_8]" },
            "style": {
              "display": "=if([$field_8] != '', 'block', 'none')",
              "width": "72px", "height": "72px", "border-radius": "50%", "object-fit": "cover",
              "border": "3px solid white"
            }
          },
          {
            "elmType": "div",
            "style": {
              "display": "=if([$field_8] != '', 'none', 'flex')",
              "width": "72px", "height": "72px", "border-radius": "50%",
              "background-color": "rgba(255,255,255,0.25)",
              "border": "3px solid white",
              "align-items": "center", "justify-content": "center", "color": "white", "font-size": "24px", "font-weight": "700"
            },
            "txtContent": "=substring([$Title], 0, 1) + substring([$field_1], 0, 1)"
          }
        ]
      },
      {
        "elmType": "div",
        "style": { "display": "flex", "flex-direction": "column", "align-items": "center", "padding": "14px", "width": "100%", "box-sizing": "border-box" },
        "children": [
          {
            "elmType": "div",
            "style": { "font-size": "16px", "font-weight": "600", "color": "#1b3a6b", "text-align": "center" },
            "txtContent": "=[$Title] + ' ' + [$field_1]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "13px", "color": "#444", "text-align": "center", "margin-top": "2px" },
            "txtContent": "=[$field_3]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "12px", "color": "#777", "text-align": "center", "margin-bottom": "8px" },
            "txtContent": "=[$field_2] + ' • ' + [$field_7]"
          },
          {
            "elmType": "a",
            "attributes": { "href": "=if([$field_4] != '', 'mailto:' + [$field_4], '')", "target": "_blank" },
            "style": { "font-size": "12px", "color": "#1b3a6b", "text-decoration": "none", "margin-bottom": "2px" },
            "txtContent": "=[$field_4]"
          },
          {
            "elmType": "a",
            "attributes": { "href": "=if([$field_5] != '', 'tel:' + [$field_5], '')" },
            "style": { "font-size": "12px", "color": "#444", "text-decoration": "none" },
            "txtContent": "=[$field_5]"
          }
        ]
      }
    ]
  }
}
----chat functionality test scripts-----
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 350,
  "width": 240,
  "hideSelection": true,
  "formatter": {
    "elmType": "div",
    "style": {
      "display": "flex",
      "flex-direction": "column",
      "align-items": "center",
      "padding": "0",
      "margin": "8px",
      "border-radius": "10px",
      "overflow": "hidden",
      "box-shadow": "0 2px 8px rgba(0,0,0,0.18)",
      "background-color": "white"
    },
    "children": [
      {
        "elmType": "div",
        "style": {
          "width": "100%",
          "height": "96px",
          "flex-shrink": "0",
          "display": "flex",
          "align-items": "center",
          "justify-content": "center",
          "background-color": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|', '|' + [$field_2] + '|') > -1, '#0f8a7e', if([$field_2] == 'Business Banking', '#b8742a', if(indexOf('|Accounting|Human Resources|Compliance|IT|Operations|Marketing|Facilities|Nashwauk Downtown|', '|' + [$field_2] + '|') > -1, '#6a4c93', '#5b6b7d'))))"
        },
        "children": [
          {
            "elmType": "img",
            "attributes": { "src": "=[$field_8]" },
            "style": {
              "display": "=if([$field_8] != '', 'block', 'none')",
              "width": "72px", "height": "72px", "border-radius": "50%", "object-fit": "cover", "border": "3px solid white"
            }
          },
          {
            "elmType": "div",
            "style": {
              "display": "=if([$field_8] != '', 'none', 'flex')",
              "width": "72px", "height": "72px", "border-radius": "50%",
              "background-color": "rgba(255,255,255,0.25)", "border": "3px solid white",
              "align-items": "center", "justify-content": "center", "color": "white", "font-size": "24px", "font-weight": "700"
            },
            "txtContent": "=substring([$Title], 0, 1) + substring([$field_1], 0, 1)"
          }
        ]
      },
      {
        "elmType": "div",
        "style": { "display": "flex", "flex-direction": "column", "align-items": "center", "padding": "14px", "width": "100%", "box-sizing": "border-box" },
        "children": [
          {
            "elmType": "div",
            "style": { "font-size": "16px", "font-weight": "600", "color": "#1b3a6b", "text-align": "center" },
            "txtContent": "=[$Title] + ' ' + [$field_1]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "13px", "color": "#444", "text-align": "center", "margin-top": "2px" },
            "txtContent": "=[$field_3]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "12px", "color": "#777", "text-align": "center", "margin-bottom": "10px" },
            "txtContent": "=[$field_2] + ' • ' + [$field_7]"
          },
          {
            "elmType": "div",
            "style": { "display": "flex", "flex-direction": "row", "gap": "6px", "width": "100%", "justify-content": "center" },
            "children": [
              {
                "elmType": "a",
                "attributes": {
                  "href": "='https://teams.microsoft.com/l/chat/0/0?users=' + [$field_4]",
                  "target": "_blank"
                },
                "style": {
                  "flex": "1", "text-align": "center", "padding": "6px 4px", "border-radius": "6px",
                  "background-color": "#1b3a6b", "color": "white", "font-size": "12px", "font-weight": "600",
                  "text-decoration": "none", "cursor": "pointer"
                },
                "txtContent": "Chat"
              },
              {
                "elmType": "a",
                "attributes": {
                  "href": "='https://teams.microsoft.com/l/call/0/0?users=' + [$field_4]",
                  "target": "_blank"
                },
                "style": {
                  "flex": "1", "text-align": "center", "padding": "6px 4px", "border-radius": "6px",
                  "background-color": "#0f8a7e", "color": "white", "font-size": "12px", "font-weight": "600",
                  "text-decoration": "none", "cursor": "pointer"
                },
                "txtContent": "Call"
              }
            ]
          },
          {
            "elmType": "a",
            "attributes": { "href": "=if([$field_4] != '', 'mailto:' + [$field_4], '')", "target": "_blank" },
            "style": { "font-size": "11px", "color": "#777", "text-decoration": "none", "margin-top": "8px" },
            "txtContent": "=[$field_4]"
          }
        ]
      }
    ]
  }
}
----Stackable functionality for chats and calls-----------
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 370,
  "width": 240,
  "hideSelection": true,
  "formatter": {
    "elmType": "div",
    "style": {
      "display": "flex",
      "flex-direction": "column",
      "align-items": "center",
      "padding": "0",
      "margin": "8px",
      "border-radius": "10px",
      "overflow": "hidden",
      "box-shadow": "0 2px 8px rgba(0,0,0,0.18)",
      "background-color": "white"
    },
    "children": [
      {
        "elmType": "div",
        "style": {
          "width": "100%",
          "height": "96px",
          "flex-shrink": "0",
          "display": "flex",
          "align-items": "center",
          "justify-content": "center",
          "background-color": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|', '|' + [$field_2] + '|') > -1, '#0f8a7e', if([$field_2] == 'Business Banking', '#b8742a', if(indexOf('|Accounting|Human Resources|Compliance|IT|Operations|Marketing|Facilities|Nashwauk Downtown|', '|' + [$field_2] + '|') > -1, '#6a4c93', '#5b6b7d'))))"
        },
        "children": [
          {
            "elmType": "img",
            "attributes": { "src": "=[$field_8]" },
            "style": {
              "display": "=if([$field_8] != '', 'block', 'none')",
              "width": "72px", "height": "72px", "border-radius": "50%", "object-fit": "cover", "border": "3px solid white"
            }
          },
          {
            "elmType": "div",
            "style": {
              "display": "=if([$field_8] != '', 'none', 'flex')",
              "width": "72px", "height": "72px", "border-radius": "50%",
              "background-color": "rgba(255,255,255,0.25)", "border": "3px solid white",
              "align-items": "center", "justify-content": "center", "color": "white", "font-size": "24px", "font-weight": "700"
            },
            "txtContent": "=substring([$Title], 0, 1) + substring([$field_1], 0, 1)"
          }
        ]
      },
      {
        "elmType": "div",
        "style": { "display": "flex", "flex-direction": "column", "align-items": "center", "padding": "14px", "width": "100%", "box-sizing": "border-box" },
        "children": [
          {
            "elmType": "div",
            "style": { "font-size": "16px", "font-weight": "600", "color": "#1b3a6b", "text-align": "center" },
            "txtContent": "=[$Title] + ' ' + [$field_1]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "13px", "color": "#444", "text-align": "center", "margin-top": "2px" },
            "txtContent": "=[$field_3]"
          },
          {
            "elmType": "div",
            "style": { "font-size": "12px", "color": "#777", "text-align": "center", "margin-bottom": "10px" },
            "txtContent": "=[$field_2] + ' • ' + [$field_7]"
          },
          {
            "elmType": "a",
            "attributes": {
              "href": "='https://teams.microsoft.com/l/chat/0/0?users=' + [$field_4]",
              "target": "_blank"
            },
            "style": {
              "width": "100%", "box-sizing": "border-box", "text-align": "center", "padding": "8px",
              "border-radius": "6px", "background-color": "#4b53bc", "color": "white", "font-size": "13px",
              "font-weight": "600", "text-decoration": "none", "cursor": "pointer", "margin-bottom": "6px"
            },
            "txtContent": "Chat on Teams"
          },
          {
            "elmType": "a",
            "attributes": {
              "href": "='https://teams.microsoft.com/l/call/0/0?users=' + [$field_4]",
              "target": "_blank"
            },
            "style": {
              "width": "100%", "box-sizing": "border-box", "text-align": "center", "padding": "8px",
              "border-radius": "6px", "background-color": "#4b53bc", "color": "white", "font-size": "13px",
              "font-weight": "600", "text-decoration": "none", "cursor": "pointer"
            },
            "txtContent": "Call on Teams"
          },
          {
            "elmType": "a",
            "attributes": { "href": "=if([$field_4] != '', 'mailto:' + [$field_4], '')", "target": "_blank" },
            "style": { "font-size": "11px", "color": "#777", "text-decoration": "none", "margin-top": "10px" },
            "txtContent": "=[$field_4]"
          }
        ]
      }
    ]
  }
}

