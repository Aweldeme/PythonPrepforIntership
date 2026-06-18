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
------testing logos------
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 340,
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
            "style": { "font-size": "12px", "color": "#777", "text-align": "center", "margin-bottom": "12px" },
            "txtContent": "=[$field_2] + ' • ' + [$field_7]"
          },
          {
            "elmType": "div",
            "style": { "display": "flex", "flex-direction": "row", "gap": "10px", "justify-content": "center" },
            "children": [
              {
                "elmType": "a",
                "attributes": {
                  "href": "='https://teams.microsoft.com/l/chat/0/0?users=' + [$field_4]",
                  "target": "_blank",
                  "title": "Chat on Teams"
                },
                "style": {
                  "width": "38px", "height": "38px", "border-radius": "50%", "background-color": "#4b53bc",
                  "display": "flex", "align-items": "center", "justify-content": "center", "text-decoration": "none", "cursor": "pointer"
                },
                "children": [
                  {
                    "elmType": "span",
                    "attributes": { "iconName": "Chat" },
                    "style": { "color": "white", "font-size": "17px" }
                  }
                ]
              },
              {
                "elmType": "a",
                "attributes": {
                  "href": "='https://teams.microsoft.com/l/call/0/0?users=' + [$field_4]",
                  "target": "_blank",
                  "title": "Call on Teams"
                },
                "style": {
                  "width": "38px", "height": "38px", "border-radius": "50%", "background-color": "#4b53bc",
                  "display": "flex", "align-items": "center", "justify-content": "center", "text-decoration": "none", "cursor": "pointer"
                },
                "children": [
                  {
                    "elmType": "span",
                    "attributes": { "iconName": "Phone" },
                    "style": { "color": "white", "font-size": "17px" }
                  }
                ]
              },
              {
                "elmType": "a",
                "attributes": {
                  "href": "=if([$field_4] != '', 'mailto:' + [$field_4], '')",
                  "title": "Email on Outlook"
                },
                "style": {
                  "width": "38px", "height": "38px", "border-radius": "50%", "background-color": "#0072c6",
                  "display": "flex", "align-items": "center", "justify-content": "center", "text-decoration": "none", "cursor": "pointer"
                },
                "children": [
                  {
                    "elmType": "span",
                    "attributes": { "iconName": "Mail" },
                    "style": { "color": "white", "font-size": "17px" }
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
--
Here’s the version with quick directory context up front:

Subject: Access to deploy PnP Modern Search

Hi [IT contact],

I’ve been building an employee directory in SharePoint on the Home site — a searchable page with photo contact cards pulling from the daily employee data. Danielle and leadership approved adding on-page search and Teams contact cards to it, using a tool called PnP Modern Search, a widely-used open-source web part from the Microsoft 365 PnP community.

Why it’s needed: SharePoint’s built-in card formatting can’t add a working search box or native Teams profile cards — those require a real web part, which must be deployed to an app catalog first.

I have site-admin but not tenant SharePoint admin, so I can’t reach the tenant catalog. Could you either:

a) Upload the package (.sppkg) to the tenant app catalog via the SharePoint admin center (More features → Apps → App Catalog → upload + “Enable for all sites”), or
b) Enable a site collection app catalog on the Home site so I can deploy it myself.

I can grab the official package and handle all the configuration — just need it in a catalog I can reach. It’s community-maintained rather than Microsoft-supported, so worth a quick review before approving.

Thanks!
Amanuel
Here’s the fuller version, walking the page top to bottom so you can point at each part of the example, describe what it is, and ask for its content in the same breath.

IT PAGE — MEETING CHEAT SHEET (Kerry, 2:30)

	1.	Open
“Thanks for the time, Kerry. We’re building a Meet the Teams section on the intranet so new hires can quickly see who each department is and what they do. I want to walk you through what the IT page will include and the few things I’ll need from you to build it out.”
	2.	Walk the example page, top to bottom
Pull up one of your screenshots (HR, Accounting, or Card Services) and point at each section as you go.
Intro (top of the page): “At the very top there’s a short intro, one or two paragraphs, that tells a brand-new hire what IT does day to day and when they’d reach out to you. That’s the overview I’ll need from you, written plainly for someone with zero context, not technical.”
Team members: “Below that, each person on your team gets their own profile. I’ve already pulled your team in from Paylocity, so the names and photos are in place. What I need is one line per person on what they’re the go-to for, 255 characters or less, something like ‘so-and-so is the primary contact for X.’ If you’ve got a few minutes we can go right down the list now, or you can send them to me after.”
Best ways to contact the team: “Then there’s a ‘best ways to contact us’ section, usually three options: a Teams message or group, an email group, and a number or extension to call. Just tell me which ones you want listed so people land in the right place instead of guessing.”
How IT supports the bank: “And at the bottom is a list of the main ways IT supports the bank and its clients, five to seven bullets, specifically the things your team handles that other departments don’t. It’s not meant to be every single thing, just the key ones a new hire should know to come to you for.”
	3.	Set the deadline
“To keep it moving, could you get that content back to me by [Friday, June 26, or a date about 1 to 3 weeks out]? I’ll also send you an email today listing exactly what I need, so you’ve got it all in writing to work from.”
	4.	Next steps
“Once I have your info, I’ll build the page out, then send it back to you to review. Nothing goes live until you’ve checked it and signed off, and then it gets released to The Lobby.”
	5.	Close
Thank them, confirm the deadline you landed on, and let them know the recap email is coming today.