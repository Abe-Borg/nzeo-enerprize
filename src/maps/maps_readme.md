### MAPS APP
- this app is responsible for managing the mapsfor different locations
for the different web pages.
- this app serves map data to different user types
- this app and the markups app coordinate to correctly display the markups on the correct map.
- templates are interactive maps with clickable school and district locations, and even clickable buildings
- the app is responsible for saving all markups placed on maps by different users. it is responsible for tracking all edits. this app also keeps a record of all meta data for a given markup.
- each site (schools, or singular buildings, district) can be marked up. this app
manages the annotations for all schools and all buildings. as well as any 
operations by/on the markups.
- In summary: this app serves the map to different users, tracks all metadata for all markups, and implements all interactivity features.

- handles saving, retrieving, and processing annotion data
- even though the visual map is rendered in the html templates, the maps app acts as the backend service provider for all map-related data.

- the maps app provides api endpoints to save and retrieve annotations. wen a user adds an annotation, js/ajax is used to 
  send the annotation deaitls to those endpoints.