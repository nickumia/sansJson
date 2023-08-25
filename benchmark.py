# with open('data.json', 'r') as jfile:
#     datasets = json.load(jfile)

# for dataset in datasets['dataset'][0:100]:
#     sansjson.sort(dataset)


a = [{
      "@type": "dcat:Dataset",
      "accessLevel": "public",
      "bureauCode": [
        "010:04"
      ],
      "contactPoint": {
        "@type": "vcard:Contact",
        "fn": "Bureau of Land Management",
        "hasEmail": "mailto:BLM_OC_GIS_Hub_UserSupport@blm.gov"
      },
      "description": "Wilderness Study Areas (WSA) for Idaho BLM as they were in 2008 (POLYGONS) This is a HISTORICAL polygon feature class for WSAs in Idaho BLM.***********************************************NOTE: December 2011. The NOC WSA implementation required that all inholdings be removed from the data. This dataset keeps the original WSA\'s that were later abolished by the 2009 Omnibus bill and also keeps the inholdings in case they are needed.************************************************",
      "distribution": [
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/json",
          "format": "ArcGIS GeoServices REST API",
          "accessURL": "https://services1.arcgis.com/KbxwQRRfWyEYLgp4/arcgis/rest/services/BLM_Idaho_NLCS_Wilderness_Study_Area_Historic_Poly/FeatureServer/0",
          "title": "ArcGIS GeoService"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/zip",
          "format": "ZIP",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly.zip?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "Shapefile"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/xml",
          "accessURL": "https://blm-egis.maps.arcgis.com/sharing/rest/content/items/31a4a169b61847c7bf3fac7b75c9e4f6/info/metadata/metadata.xml?format=iso19139",
          "title": "ISO-19139 metadata"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/csv",
          "format": "CSV",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly.csv?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "CSV"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/vnd.google-earth.kml+xml",
          "format": "KML",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly.kml?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "KML"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/html",
          "format": "Web Page",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/maps/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly",
          "title": "ArcGIS Hub Dataset"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/vnd.geo+json",
          "format": "GeoJSON",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly.geojson?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "GeoJSON"
        }
      ],
      "identifier": "https://www.arcgis.com/home/item.html?id=31a4a169b61847c7bf3fac7b75c9e4f6&sublayer=0",
      "issued": "2022-04-08T05:37:49Z",
      "keyword": [
        "planningCadastre",
        "Special Management Area",
        "biota",
        "Wilderness Study Area",
        "WSA",
        "National Landscape Conservation System",
        "Wilderness",
        "boundaries",
        "NLCS",
        "Management",
        "Idaho"
      ],
      "landingPage": "https://gbp-blm-egis.hub.arcgis.com/maps/BLM-EGIS::blm-idaho-nlcs-wilderness-study-area-historic-poly",
      "license": "http://www.usa.gov/publicdomain/label/1.0/",
      "modified": "2022-04-08T17:37:53.917Z",
      "programCode": [
        "010:000"
      ],
      "publisher": {
        "@type": "org:Organization",
        "name": "Bureau of Land Management",
        "subOrganizationOf": {
          "@type": "org:Organization",
          "name": "U.S. Department of the Interior",
          "subOrganizationOf": {
            "@type": "org:Organization",
            "name": "White House"
          }
        }
      },
      "spatial": "-117.0229,41.989,-111.0657,48.9318",
      "theme": [
        "geospatial"
      ],
      "title": "BLM Idaho NLCS Wilderness Study Area Historic Poly"
    },
    {
      "@type": "dcat:Dataset",
      "accessLevel": "public",
      "bureauCode": [
        "010:04"
      ],
      "contactPoint": {
        "@type": "vcard:Contact",
        "fn": "Bureau of Land Management",
        "hasEmail": "mailto:BLM_OC_GIS_Hub_UserSupport@blm.gov"
      },
      "description": "This feature class contains polygons and attributes describing Idaho Areas of Critical Environmental Concern that existed and were later removed.For more information contact us at blm_id_stateoffice@blm.gov.",
      "distribution": [
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/zip",
          "format": "ZIP",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-acec-historical-poly-hub.zip?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "Shapefile"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/vnd.google-earth.kml+xml",
          "format": "KML",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-acec-historical-poly-hub.kml?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "KML"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/vnd.geo+json",
          "format": "GeoJSON",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-acec-historical-poly-hub.geojson?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "GeoJSON"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/html",
          "format": "Web Page",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/maps/BLM-EGIS::blm-idaho-acec-historical-poly-hub",
          "title": "ArcGIS Hub Dataset"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "application/json",
          "format": "ArcGIS GeoServices REST API",
          "accessURL": "https://services1.arcgis.com/KbxwQRRfWyEYLgp4/arcgis/rest/services/BLM_Idaho_ACEC_Historical_Poly_Hub/FeatureServer/0",
          "title": "ArcGIS GeoService"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/csv",
          "format": "CSV",
          "accessURL": "https://gbp-blm-egis.hub.arcgis.com/datasets/BLM-EGIS::blm-idaho-acec-historical-poly-hub.csv?outSR=%7B%22latestWkid%22%3A8826%2C%22wkid%22%3A102605%7D",
          "title": "CSV"
        },
        {
          "@type": "dcat:Distribution",
          "mediaType": "text/xml",
          "accessURL": "https://blm-egis.maps.arcgis.com/sharing/rest/content/items/3953720f16744c18a99114c367778824/info/metadata/metadata.xml?format=iso19139",
          "title": "ISO-19139 metadata"
        }
      ],
      "identifier": "https://www.arcgis.com/home/item.html?id=3953720f16744c18a99114c367778824&sublayer=0",
      "issued": "2022-04-01T07:50:41Z",
      "keyword": [
        "BLM",
        "ONA",
        "RNA",
        "United States",
        "Land Use Planning",
        "Authorization",
        "Department of the Interior",
        "Area of Critical Environmental Concern",
        "boundaries",
        "Resource Framework Plan",
        "Relevant and Important Values",
        "RFP",
        "ACEC",
        "DOI",
        "geoscientificInformation",
        "FLPMA",
        "Land Management",
        "LUP",
        "Resource Management Plan",
        "Geospatial",
        "Management",
        "Outstanding Natural Area",
        "Geographic Information System",
        "GIS",
        "Jurisdiction",
        "environment",
        "Research Natural Area",
        "RMP",
        "Bureau of Land Management",
        "Federal Land Policy and Mangement Act",
        "location",
        "Land Use Plan",
        "Western States",
        "Idaho"
      ],
      "landingPage": "https://gbp-blm-egis.hub.arcgis.com/maps/BLM-EGIS::blm-idaho-acec-historical-poly-hub",
      "license": "http://www.usa.gov/publicdomain/label/1.0/",
      "modified": "2022-04-01T19:50:44.602Z",
      "programCode": [
        "010:000"
      ],
      "publisher": {
        "@type": "org:Organization",
        "name": "Bureau of Land Management",
        "subOrganizationOf": {
          "@type": "org:Organization",
          "name": "U.S. Department of the Interior",
          "subOrganizationOf": {
            "@type": "org:Organization",
            "name": "White House"
          }
        }
      },
      "spatial": "-116.7493,41.9293,-112.9168,46.235",
      "theme": [
        "geospatial"
      ],
      "title": "BLM Idaho ACEC Historical Poly Hub"
    }]

sansjson.sort(a)
