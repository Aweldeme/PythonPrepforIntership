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
test
