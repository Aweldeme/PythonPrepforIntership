no{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 320,
  "width": 260,
  "hideSelection": true,
  "fillHorizontally": true,
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
      "background-color": "white",
      "width": "220px"
    },
    "children": [
      {
        "elmType": "div",
        "attributes": {
          "class": "=if(@currentField.title == '', 'ms-bgColor-themePrimary', '')"
        },
        "style": {
          "width": "84px",
          "height": "84px",
          "border-radius": "50%",
          "background-size": "cover",
          "background-position": "center",
          "background-image": "=if([$Photo] != '', 'url(' + [$Photo] + ')', '')",
          "background-color": "=if([$Photo] != '', 'transparent', '#0b3d66')",
          "display": "flex",
          "align-items": "center",
          "justify-content": "center",
          "color": "white",
          "font-size": "26px",
          "font-weight": "600",
          "margin-bottom": "10px"
        },
        "txtContent": "=if([$Photo] != '', '', substring([$Title],0,1) + substring([$LastName],0,1))"
      },
      {
        "elmType": "div",
        "style": { "font-size": "16px", "font-weight": "600", "text-align": "center", "color": "#0b3d66" },
        "txtContent": "=[$Title] + ' ' + [$LastName]"
      },
      {
        "elmType": "div",
        "style": { "font-size": "13px", "text-align": "center", "color": "#444", "margin-top": "2px" },
        "txtContent": "=[$JobTitle]"
      },
      {
        "elmType": "div",
        "style": { "font-size": "12px", "text-align": "center", "color": "#777", "margin-bottom": "8px" },
        "txtContent": "=[$Department] + ' • ' + [$Location]"
      },
      {
        "elmType": "a",
        "attributes": { "href": "=if([$Email] != '', 'mailto:' + [$Email], '')", "target": "_blank" },
        "style": { "font-size": "12px", "color": "#0b3d66", "text-decoration": "none", "margin-bottom": "2px" },
        "txtContent": "=[$Email]"
      },
      {
        "elmType": "a",
        "attributes": { "href": "=if([$Telephone] != '', 'tel:' + [$Telephone], '')" },
        "style": { "font-size": "12px", "color": "#444", "text-decoration": "none" },
        "txtContent": "=[$Telephone]"
      }
    ]
  }
}
-------------------
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/tile-formatting.schema.json",
  "height": 300,
  "width": 240,
  "hideSelection": true,
  "formatter": {
    "elmType": "div",
    "customCardStyleForHover": true,
    "style": {
      "display": "flex",
      "flex-direction": "column",
      "align-items": "center",
      "padding": "0",
      "margin": "8px",
      "border-radius": "10px",
      "overflow": "hidden",
      "box-shadow": "0 2px 6px rgba(0,0,0,0.15)",
      "background-color": "white",
      "cursor": "default",
      "--cardColor": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|', '|' + [$field_2] + '|') > -1, '#2e7d8f', if([$field_2] == 'Business Banking', '#3a5a8c', '#5b6b7d')))"
    },
    "children": [
      {
        "elmType": "div",
        "style": {
          "width": "100%",
          "height": "8px",
          "background-color": "=@currentWebPart.htmlElement ? '' : ''",
          "flex-shrink": "0"
        },
        "attributes": { "class": "" },
        "forEach": ""
      },
      {
        "elmType": "div",
        "style": {
          "width": "100%",
          "height": "8px",
          "background-color": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|', '|' + [$field_2] + '|') > -1, '#2e7d8f', if([$field_2] == 'Business Banking', '#3a5a8c', '#5b6b7d')))",
          "flex-shrink": "0"
        }
      },
      {
        "elmType": "div",
        "style": { "display": "flex", "flex-direction": "column", "align-items": "center", "padding": "16px", "width": "100%", "box-sizing": "border-box" },
        "children": [
          {
            "elmType": "img",
            "attributes": { "src": "=[$field_8]" },
            "style": {
              "display": "=if([$field_8] != '', 'block', 'none')",
              "width": "84px", "height": "84px", "border-radius": "50%", "object-fit": "cover", "margin-bottom": "10px"
            }
          },
          {
            "elmType": "div",
            "style": {
              "display": "=if([$field_8] != '', 'none', 'flex')",
              "width": "84px", "height": "84px", "border-radius": "50%",
              "background-color": "=if(indexOf('|Retail|Deposit Operations|Deposit Ops|', '|' + [$field_2] + '|') > -1, '#1b3a6b', if(indexOf('|Mortgage|Loan Operations|Loans|Credit|', '|' + [$field_2] + '|') > -1, '#2e7d8f', if([$field_2] == 'Business Banking', '#3a5a8c', '#5b6b7d')))",
              "align-items": "center", "justify-content": "center", "color": "white", "font-size": "26px", "font-weight": "600", "margin-bottom": "10px"
            },
            "txtContent": "=substring([$Title], 0, 1) + substring([$field_1], 0, 1)"
          },
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
